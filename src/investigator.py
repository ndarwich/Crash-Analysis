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


 


def main():
    traffic_df = pd.read_csv('../data/summer2018.csv')
#    test = pd.read_table("../data/Traffic_Violations.csv", header=None, skip_blank_lines=False, delim_whitespace=True)
#    traffic_df.rename(index=str, columns={"Date Of Stop": "Date_Of_Stop"})
    traffic_df.columns = [c.replace(' ', '_') for c in traffic_df.columns]
    print(traffic_df.Date_Of_Stop)
    print(traffic_df.columns)    
    plt.scatter(traffic_df.Longitude,traffic_df.Latitude)

#    fig = plt.figure(num=None, figsize=(42, 16) ) 
#    m = Basemap(width=6000000,height=4500000,resolution='c',projection='aea',lat_1=35.,lat_2=45,lon_0=-75,lat_0=40)
#    m.drawcoastlines(linewidth=0.5)
#    m.fillcontinents(color='tan',lake_color='lightblue')
#    # draw parallels and meridians.
#    m.drawparallels(np.arange(-90.,91.,15.),labels=[True,True,False,False],dashes=[2,2])
#    m.drawmeridians(np.arange(-180.,181.,15.),labels=[False,False,False,True],dashes=[2,2])
#    m.drawmapboundary(fill_color='lightblue')
#    m.drawcountries(linewidth=2, linestyle='solid', color='k' ) 
#    m.drawstates(linewidth=0.5, linestyle='solid', color='k')
#    m.drawrivers(linewidth=0.5, linestyle='solid', color='blue')
#    plt.show()
    plt.savefig('Car_Accidents_Visualization.png')
    plt.show()
    plt.draw()
if __name__ == "__main__":
    main()       