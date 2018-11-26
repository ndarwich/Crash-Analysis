#Authors: Nabil Darwich, Hamza Mughal
import numpy
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import os
import os.path
import scipy.sparse as sp
from matplotlib.colors import rgb2hex
import matplotlib as mpl
import seaborn as sns
from imblearn import under_sampling, over_sampling
from imblearn.combine import SMOTETomek
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_selection import SelectKBest, SelectPercentile, chi2, SelectFdr, f_regression, mutual_info_classif, RFE
from imblearn import over_sampling


#data splitting for training data
def splitTraining(X, y):
    #0.28 split produced great results
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.28, random_state=0)
    return X_train, X_test, y_train, y_test


def main():
    '''
    crashes_df = pd.read_csv('../data/crashes-summer2018.csv')
    people_df = pd.read_csv('../data/people-summer2018.csv')
    vehicles_df = pd.read_csv('../data/vehicles-summer2018.csv')
    dfs = [crashes_df, people_df, vehicles_df]
    for df in dfs:
        df.columns = [c.replace(' ', '_') for c in df.columns]
        print(df.columns)
    '''
#    trainingTable = pd.read_csv("../data/trainingValid.csv")
    
    trainingTable = pd.read_csv("../data/trainingValid.csv")
    trainingLabels = pd.read_csv("../data/TrainingLabels.csv")
    trainingTable.columns = [c.replace(' ', '_') for c in trainingTable.columns]
#    print(trainingTable.columns)
    trainingValues = trainingTable
#    print(trainingLabels.values)
#    print(trainingTable)
    X_train, X_test, y_train, y_test = splitTraining(trainingTable, trainingLabels)
    trainingmatrix = sp.csr_matrix(X_train)
    kbest = SelectKBest(chi2, k=20)
#    print(trainingmatrix.toarray())
    reduced_train = kbest.fit_transform(trainingmatrix.toarray(), y_train)
#
    ros = RandomOverSampler(random_state=42)
    X_res, y_res = ros.fit_sample(reduced_train, y_train)   
    
    
if __name__ == "__main__":
    main()


'''
def drawproportiongraph():
    weather_group = crashes_df['34_CONDITION'].value_counts()
    print(weather_group)
    plt.ylabel('Proportion of Crashes')
    labels = ['CLEAR', 'RAIN', 'UNKNOWN', 'CLOUDY', 'OTHER', 'FOG', 'SNOW', 'SLEET', 'SEVERE CROSS WIND GATE']
    weather_group.index = labels

    (weather_group / weather_group.sum()).plot(kind='barh')     


def drawpopulationmapandaccidents():
    crashes_df = pd.read_csv('../data/crashes-summer2018.csv')    
    pop_path = "ChicagoPopulation.csv"
    DF       = pd.read_csv("ChicagoPopulation.csv")
    colormap = plt.cm.Oranges 
    
    us_shape_file_dir = "cb_2017_us_zcta510_500k"
    os.chdir(us_shape_file_dir)
    
    # Chicago coordinates.
    lowerlon = -88.2 
    upperlon = -87.2
    lowerlat = 41.62
    upperlat = 42.05
    
    
    m = Basemap(
        llcrnrlon=lowerlon,
        llcrnrlat=lowerlat,
        urcrnrlon=upperlon,
        urcrnrlat=upperlat,
        projection="lcc",
        resolution="c",
        lat_0=lowerlat,
        lat_1=upperlat,
        lon_0=lowerlon,
        lon_1=upperlon
        )
    
    
    shp_info = m.readshapefile(
        os.path.basename(us_shape_file_dir),'states',drawbounds=True
        )
    
    # Convert integer ZIP5 field to character dtype.
    DF['ZIP5'] = DF['ZIP5'].astype(str)
    
    # Read population density info into popdens dict. Take square root of 
    # actual density for better color mapping.
    popdens = {
        str(i):np.sqrt(j) for (i, j) in zip(DF.ZIP5.values,DF.POPULATION.values)
        }
    
    # Choose a color for each state based on population density. Range
    # vmin-vmax has arbitrarily been set to 0-6. Fee lfree to experiment 
    # with other ranges.
    ziplist = []
    colors  = {}
    vmin    = 0.
    vmax    = 6.
    
    
    # Filter m.states_info to only Chicago zipcodes.
    zip_info   = m.states_info
    popdiv     = (max(popdens.values())/(vmax-vmin))
    popdensscl = {i:(j/popdiv) for (i,j) in popdens.items()}
    
    
    for d in zip_info:
        iterzip = d["ZCTA5CE10"]
        if iterzip in popdensscl.keys():
            iterpop = popdensscl.get(iterzip,0)
            colors[iterzip] = colormap(iterpop/vmax)[:3]
        ziplist.append(iterzip)
    
    
    for nshape,seg in enumerate(m.states):
        i, j = zip(*seg)
        if ziplist[nshape] in popdensscl.keys():
            color = rgb2hex(colors[ziplist[nshape]])
            edgecolor = "#000000"
            plt.fill(i,j,color,edgecolor=edgecolor);
    
    
    # (Optional) include colorbar.
    sm = plt.cm.ScalarMappable(
        cmap=colormap,norm=mpl.colors.Normalize(vmin=vmin, vmax=vmax)
        )
    lats = []
    longs = []
    for i, e in enumerate(crashes_df.LONGITUDE):
#        print(i, crashes_df.LONGITUDE[i])
#        break
        lats.append(crashes_df.LATITUDE[i])
        longs.append(crashes_df.LONGITUDE[i])
    m.scatter(longs, lats, s=1,alpha=0.08,marker = 'o', color = 'b', zorder=2, latlon=True)          
    mm = plt.cm.ScalarMappable(cmap=colormap)
    mm.set_array([vmin, vmax])
    plt.colorbar(mm,ticks=np.arange(vmin, vmax+1, 1),orientation="vertical")
    plt.gca().axis("off")
    plt.show()      


def drawmapandaccidents(): # tutorial on basemaps from http://www.jtrive.com/visualizing-population-density-by-zip-code-with-basemap.html
    us_shape_file_dir = "cb_2017_us_zcta510_500k"
    os.chdir(us_shape_file_dir)
    crashes_df = pd.read_csv('../data/crashes-summer2018.csv')
    # Chicago coordinates.
    lowerlon = -88.2 
    upperlon = -87.2
    lowerlat = 41.62
    upperlat = 42.05
    
    
    m = Basemap(
        llcrnrlon=lowerlon,
        llcrnrlat=lowerlat,
        urcrnrlon=upperlon,
        urcrnrlat=upperlat,
        resolution='c',
        projection='lcc',
        lat_0=lowerlat,
        lat_1=upperlat,
        lon_0=lowerlon,
        lon_1=upperlon
        )
    h = 0
    crashes_df.LONGITUDE.dropna()
    crashes_df.LATITUDE.dropna()
    crashes_df['lat_lon'] = list(zip(crashes_df.LONGITUDE, crashes_df.LATITUDE))
    print(crashes_df['lat_lon'])

    print("Finished mapping plots")    
    shp_info = m.readshapefile(os.path.basename(us_shape_file_dir), 'state')
#    m.plot(32,42, marker = 'o', c='r', markersize=6, alpha=0.8, latlon=False)
#    m.scatter(crashes_df.LONGITUDE,crashes_df.LATITUDE)
    lats = []
    longs = []
    for i, e in enumerate(crashes_df.LONGITUDE):
#        print(i, crashes_df.LONGITUDE[i])
#        break
        lats.append(crashes_df.LATITUDE[i])
        longs.append(crashes_df.LONGITUDE[i])
    print(len(lats))
    print(len(longs))
    x,y=m(lats, longs)
    m.scatter(longs, lats, s=7,marker = '.', color = 'b', zorder=1, latlon=True)  
    plt.gca().axis("off")
    plt.savefig('Car_Accidents_Chicago_Visualization.png')
    plt.show() 
    plt.draw()    
'''