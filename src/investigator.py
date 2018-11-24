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


 


def main():
    crashes_df = pd.read_csv('../data/crashes-summer2018.csv')
    people_df = pd.read_csv('../data/people-summer2018.csv')
    vehicles_df = pd.read_csv('../data/vehicles-summer2018.csv')
    dfs = [crashes_df, people_df, vehicles_df]
    for df in dfs:
        df.columns = [c.replace(' ', '_') for c in df.columns]
        print(df.columns)
    plt.scatter(crashes_df.LONGITUDE,crashes_df.LATITUDE)
    plt.savefig('Car_Accidents_Visualization.png')
    plt.show()
    plt.draw()
if __name__ == "__main__":
    main()       