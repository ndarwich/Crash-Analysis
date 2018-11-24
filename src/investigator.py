#Authors: Nabil Darwich, Hamza Mughal
import numpy
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm
import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import os
import os.path
import scipy.sparse as sp
 


def main():
    crashes_df = pd.read_csv('../data/crashes-summer2018.csv')
    people_df = pd.read_csv('../data/people-summer2018.csv')
    vehicles_df = pd.read_csv('../data/vehicles-summer2018.csv')
    dfs = [crashes_df, people_df, vehicles_df]
    for df in dfs:
        df.columns = [c.replace(' ', '_') for c in df.columns]
        print(df.columns)
#    plt.scatter(crashes_df.LONGITUDE,crashes_df.LATITUDE)
#    plt.savefig('Car_Accidents_Visualization.png')
#    plt.show()
#    plt.draw()    
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
#    for i in crashes_df['lat_lon']:
#        if h % 5000 == 0:
#            print(h)
##        print(i[0])
##        break
#        h+=1
##        x,y = i
#        m.plot(i[0], i[1], marker = 'o', c='r', markersize=1, alpha=0.8, latlon=False)
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
if __name__ == "__main__":
    main()


def drawmap():
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
#    for i in crashes_df['lat_lon']:
#        if h % 10 == 0:
#            print(h)
#        h+=1
#        x,y = i
#        m.plot(x, y, marker = 'o', c='r', markersize=1, alpha=0.8, latlon=False)
    m.plot(-87.73654930000001,41.91967954, marker = 'o', c='r', markersize=6, alpha=0.8, latlon=False)    
    shp_info = m.readshapefile(os.path.basename(us_shape_file_dir), 'state')
    plt.gca().axis("off")
    plt.show()       