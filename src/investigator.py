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
from sklearn.naive_bayes import BernoulliNB
from imblearn.combine import SMOTETomek
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_selection import SelectKBest, SelectPercentile, chi2, SelectFdr, f_regression, mutual_info_classif, RFE
from imblearn import over_sampling
import Basemap
from sklearn.metrics import f1_score
LIGHTING_CONDITION = {
0: "DARKNESS",
1: "DAYLIGHT",
2: "DAWN",
3: "DARKNESS LIGHTED ROAD",
4: "DUSK",
12: "OTHER",
200: "UNKNOWN"
}

WEATHER_CONDITION = {
0: "CLEAR",
1: "CLOUDY OR OVERCAST",
2: "RAIN",
3: "SEVERE CROSS WIND GATE",
4: "SLEET OR HAIL",
5: "SNOW",
6: "FOG OR SMOKE OR HAZE",
12: "OTHER",
200: "UNKNOWN"
}

TRAFFIC_CONTROL_DEVICE = {
0: "NO_CONTROLS",
1: "TRAFFIC SIGNAL",
2: "STOP SIGN OR FLASHER",
3: "LANE USE MARKING",
4: "YIELD",
5: "SCHOOL ZONE",
6: "RAILROAD CROSSING GATE",
7: "POLICE OR FLAGMAN",
8: "DELINEATORS",
9: "OTHER WARNING SIGN",
10: "OTHER REG SIGN",
11: "OTHER RAILROAD CROSSING",
12: "OTHER",
200: "UNKNOWN"
}

DEVICE_CONDITION = {
0:  "NOT KNOWN",
1: "FUNCTIONING IMPROPERLY",
2: "FUNCTIONING PROPERLY",
3: "NOT FUNCTIONING",
4: "MISSING",
5: "WORN REFLECTIVE MATERIAL",
12: "OTHER",
200: "UNKNOWN"
}

ROADWAY_SURFACE_COND = {
0: "DRY",
1: "WET",
2: "SAND MUD DIRT",
3: "SNOW OR SLUSH",
12: "OTHER",
200: "UNKNOWN"
}

FIRST_CRASH_TYPE = {
0: "ANGLE",
1: "ANIMAL",
2: "FIXED OBJECT",
3: "HEAD ON",
4: "OTHER NONCOLLISION",
5: "OTHER OBJECT",
6: "OVERTURNED",
7: "PARKED MOTOR VEHICLE",
8: "PEDALCYCLIST",
9: "PEDESTRIAN",
10: "REAR END",
11: "SIDESWIPE OPPOSITE DIRECTION",
12: "SIDESWIPE SAME DIRECTION",
13: "TRAIN",
14: "TURNING",
200: "UNKNOWN"
}

TRAFFICWAY_TYPE = {
0: "ALLEY",
1: "CENTER TURN LANE",
2: "DIVIDED WITH MEDIAN  NOT RAISED",
3: "DIVIDED WITH MEDIAN BARRIER",
4: "DRIVEWAY",
5: "NOT DIVIDED",
6: "ONEWAY",
7: "PARKING LOT",
8: "RAMP",
12: "OTHER",
200: "UNKNOWN"
}

ALIGNMENT = {
0: "STRAIGHT AND LEVEL",
1: "STRAIGHT ON HILLCREST",
2: "STRAIGHT ON GRADE",
3: "CURVE LEVEL",
4: "CURVE ON HILLCREST",
5: "CURVE ON GRADE",
200: "UNKNOWN"
}

ROAD_DEFECT = {
0: "NO DEFECTS",
1: "RUT HOLES",
2: "SHOULDER DEFECT",
3: "WORN SURFACE",
4: "DEBRIS ON ROADWAY",
12: "OTHER",
200: "UNKNOWN"
}

CRASH_TYPE = {
0: "NO INJURY  OR  DRIVE AWAY",
1: "INJURY AND  OR  OR TOW DUE TO CRASH",
12: "OTHER",
200: "UNKNOWN"
}

PRIM_CONTRIBUTORY_CAUSE = SEC_CONTRIBUTORY_CAUSE = {
0: "UNABLE TO DETERMINE",
1: "ANIMAL",
2: "CELL PHONE USE OTHER THAN TEXTING",
3: "DISREGARDING OTHER TRAFFIC SIGNS",
4: "DISREGARDING ROAD MARKINGS",
5: "DISREGARDING STOP SIGN",
6: "DISREGARDING TRAFFIC SIGNALS",
7: "DISTRACTION FROM INSIDE VEHICLE",
8: "DISTRACTION FROM OUTSIDE VEHICLE",
9: "DISTRACTION OTHER ELECTRONIC DEVICE  NAVIGATION DEVICE DVD PLAYER ETC",
10: "DRIVING ON WRONG SIDE OR WRONG WAY",
11: "DRIVING SKILLS OR KNOWLEDGE OR EXPERIENCE",
12: "EQUIPMENT VEHICLE CONDITION",
13: "EVASIVE ACTION DUE TO ANIMAL OBJECT NONMOTORIST",
14: "EXCEEDING AUTHORIZED SPEED LIMIT",
15: "EXCEEDING SAFE SPEED FOR CONDITIONS",
16: "FAILING TO REDUCE SPEED TO AVOID CRASH",
17: "FAILING TO YIELD RIGHTOFWAY",
18: "FOLLOWING TOO CLOSELY",
19: "HAD BEEN DRINKING  USE WHEN ARREST IS NOT MADE",
20: "IMPROPER BACKING",
21: "IMPROPER LANE USAGE",
22: "IMPROPER OVERTAKING OR PASSING",
23: "IMPROPER TURNING OR NO SIGNAL",
24: "MOTORCYCLE ADVANCING LEGALLY ON RED LIGHT",
25: "OPERATING VEHICLE IN ERRATIC RECKLESS CARELESS NEGLIGENT OR AGGRESSIVE MANNER",
26: "PASSING STOPPED SCHOOL BUS",
27: "PHYSICAL CONDITION OF DRIVER",
28: "ROAD CONSTRUCTION OR MAINTENANCE",
29: "ROAD ENGINEERING OR SURFACE OR MARKING DEFECTS",
30: "TEXTING",
31: "TURNING RIGHT ON RED",
32: "UNDER THE INFLUENCE OF ALCOHOL OR DRUGS  USE WHEN ARREST IS EFFECTED",
33: "VISION OBSCURED  SIGNS TREE LIMBS BUILDINGS ETC",
34: "WEATHER",
35: "BICYCLE ADVANCING LEGALLY ON RED LIGHT",
36: "DISREGARDING YIELD SIGN",
200: "UNKNOWN"
}

WORK_ZONE_TYPE = {
0: "UTILITY",
1: "MAINTENANCE",
2: "CONSTRUCTION",
200: "UNKNOWN"
}

"""
INJURY_CLASSIFICATION = {
0: "NO INDICATION OF INJURY",
1: "REPORTED NOT EVIDENT",
2: "NONINCAPACITATING INJURY",
3: "INCAPACITATING INJURY",
4: "FATAL",
200: "UNKNOWN"
}
"""

#NEW
INJURY_CLASSIFICATION = {
0: "NO INDICATION OF INJURY",
1: "NONINCAPACITATING INJURY",
2: "INCAPACITATING INJURY",
3: "FATAL",
200: "UNKNOWN"
}

PERSON_TYPE = {
0: "DRIVER",
1: "PASSENGER",
2: "NONCONTACT VEHICLE",
3: "NONMOTOR VEHICLE",
4: "BICYCLIST",
5: "PEDESTRIAN",
200: "UNKNOWN"
}

SEX = {
0: "M",
1: "F",
2: "X",
12: "OTHER",
200: "UNKNOWN"
}

PHYSICAL_CONDITION = {
0: "NORMAL",
1: "EMOTIONAL",
2: "FATIGUED OR ASLEEP",
3: "HAD BEEN DRINKING",
4: "ILLNESS OR FAINTED",
5: "IMPAIRED ALCOHOL",
6: "IMPAIRED DRUGS",
7: "REMOVED BY EMS",
8: "MEDICATED",
12: "OTHER",
200: "UNKNOWN"
}

SAFETY_EQUIPMENT = {
0: "SAFETY BELT USED",
1: "SAFETY BELT NOT USED",
2: "HELMET NOT USED",
3: "HELMET USED",
4: "CHILD RESTRAINT NOT USED",
5: "CHILD RESTRAINT USED",
6: "CHILD RESTRAINT USED IMPROPERLY",
7: "NONE PRESENT",
12: "OTHER",
200: "UNKNOWN"
}

DRIVER_ACTION = {
0: "NONE",
1: "FAILED TO YIELD",
2: "IMPROPER PASSING",
3: "FOLLOWED TOO CLOSELY",
4: "IMPROPER LANE CHANGE",
5: "DISREGARDED CONTROL DEVICES",
6: "IMPROPER BACKING",
7: "IMPROPER TURN",
8: "TOO FAST FOR CONDITIONS",
9: "WRONG WAY OR SIDE",
10: "IMPROPER PARKING",
11: "TEXTING",
12: "OTHER OR STOPPED SCHOOL BUS OR LICENSE RESTRICTIONS",
13: "EVADING POLICE VEHICLE",
14: "EMERGENCY VEHICLE ON CALL",
15: "CELL PHONE USE OTHER THAN TEXTING",
200: "UNKNOWN"
}

DRIVER_VISION = {
	0: "NOT OBSCURED",
	1: "MOVING VEHICLES",
	2: "BUILDINGS",
	3: "TREES PLANTS",
	4: "WINDSHIELD  WATER OR ICE",
	5: "PARKED VEHICLES",
	6: "BLINDED SUNLIGHT OR BLINDED HEADLIGHTS",
	12: "OTHER OR SIGNBOARD OR HILLCREST OR BLOWING MATERIALS",
	200: "UNKNOWN"
	}

ROADWAY_SURFACE_COND = {
	0: "DRY",
	1: "WET",
	2: "SAND MUD DIRT",
	3: "SNOW OR SLUSH",
	12: "OTHER",
	200: "UNKNOWN"
	}

AGE = {
   0: "TODDLER 0 TO 3",
   1: "SMALL CHILD 3 TO 6",
   2: "PRETEEN 6 TO 13",
   3: "TEEN 13 TO 18",
   4: "YOUNG ADULT 18 TO 21",
   5: "ADULT 21 TO 30",
   6: "MIDDLE AGED ADULT 30 TO 50",
   7: "OLD ADULT 50 TO 65",
   8: "SENIOR 65 TO 75",
   9: "OLD SENIOR 75 TO 100",
   10: "SUPERCENTENARIAN 100+",
   200: "UNKNOWN AGE"
   }

categories = {
"PERSON_TYPE": PERSON_TYPE,
#"POSTED_SPEED_LIMIT": POSTED_SPEED_LIMIT,
"TRAFFIC_CONTROL_DEVICE": TRAFFIC_CONTROL_DEVICE,
"DEVICE_CONDITION": DEVICE_CONDITION,
"WEATHER_CONDITION": WEATHER_CONDITION,
"LIGHTING_CONDITION": LIGHTING_CONDITION,
"FIRST_CRASH_TYPE": FIRST_CRASH_TYPE,
"TRAFFICWAY_TYPE": TRAFFICWAY_TYPE,
"ALIGNMENT": ALIGNMENT,
"ROADWAY_SURFACE_COND": ROADWAY_SURFACE_COND,
"ROAD_DEFECT": ROAD_DEFECT,
"PRIM_CONTRIBUTORY_CAUSE": PRIM_CONTRIBUTORY_CAUSE,
"SEC_CONTRIBUTORY_CAUSE": SEC_CONTRIBUTORY_CAUSE,
"SEX": SEX,
"AGE": AGE,
"SAFETY_EQUIPMENT": SAFETY_EQUIPMENT,
"DRIVER_ACTION": DRIVER_ACTION,
"DRIVER_VISION": DRIVER_VISION,
"PHYSICAL_CONDITION": PHYSICAL_CONDITION
}



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
    
    trainingTable = pd.read_csv("../data/training-final-values.csv")
    #trainingLabels = pd.read_csv("../data/training-final-labels.csv")
    trainingLabels = pd.read_csv("../data/training-final-labels-NEW.csv")
    trainingTable.columns = [c.replace(' ', '_') for c in trainingTable.columns]
    
#    print(trainingTable.columns)
    
#    print(trainingLabels.values)
#    print(trainingTable)
    X_train, X_test, y_train, y_test = splitTraining(trainingTable, trainingLabels) # make train test split
    trainingmatrix = sp.csr_matrix(X_train)
    kbest = SelectKBest(chi2, k=20) # select best 2o features

#    print(trainingmatrix.toarray())
    reduced_train = kbest.fit_transform(trainingmatrix.toarray(), y_train)
 
    
#
    ros = RandomOverSampler(random_state=42)
    X_res, y_res = ros.fit_sample(reduced_train, y_train) # over sample training data
    print(y_res) 
    feature_idx = kbest.get_support()
    feature_name = trainingTable.columns[feature_idx]
    print(feature_name)
    kbestfeaturenames = ','.join(feature_name)
    print(kbestfeaturenames)
    

    np.savetxt("oversampledtrain.csv", X_res, delimiter=",",header=kbestfeaturenames,comments='',fmt='%d')
    np.savetxt("oversampledlabels.csv", y_res, delimiter=",",header='INJURY_CLASSIFICATION',comments='',fmt='%d')
    
    y_res_2 = []
    for v in y_res:
        y_res_2.append(INJURY_CLASSIFICATION[v])
    
    np.savetxt("oversampledlabels_strings.csv", y_res_2, delimiter=",",header='INJURY_CLASSIFICATION',comments='',fmt='%s')    
   # mylist = [[ for g in range(len(x))] for x in X_res]
    X_res = X_res.astype(int)
    categoryList = categories.keys()
    mylist = []
    for x in X_res: # convert number to string in dictionaries
        sublist = []
        for g in range(len(x)):
            if feature_name[g] in categoryList:
                try:
                    feature = categories[feature_name[g]]
                    sublist.append(feature[x[g]])
                except Exception as e:
                    print("Error x[g] =", x[g], "Feature =", feature)
            else:
                sublist.append(str(int(x[g])) + " " + feature_name[g])
        mylist.append(sublist)
    np.savetxt("oversampledtrain_strings.csv", mylist, delimiter=",",header=kbestfeaturenames,comments='',fmt='%s')          
if __name__ == "__main__":
    main()



def drawproportiongraph():
    weather_group = crashes_df['34_CONDITION'].value_counts()
    print(weather_group)
    plt.ylabel('Proportion of Crashes')
    labels = ['CLEAR', 'RAIN', 'UNKNOWN', 'CLOUDY', 'OTHER', 'FOG', 'SNOW', 'SLEET', 'SEVERE CROSS WIND GATE']
    weather_group.index = labels

    (weather_group / weather_group.sum()).plot(kind='barh')     


def drawpopulationmapandaccidents(): # reference: http://www.jtrive.com/visualizing-population-density-by-zip-code-with-basemap.html
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
