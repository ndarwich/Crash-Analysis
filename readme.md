# An Investigation Into What Causes Crash Injuries, Fatalities

### This project analyzes crash data from the City of Chicago.

## The original datasets can be found at the following links:
### Crashes - https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if
### Vehicles - https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3
### People - https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d

### The original datasets have been modified (by joining the tables, binning the data, feature reduction, etc) and can be found in the "data" folder.

### Source code (used for data transformation, map visualizations, dictionaries, etc) can be found in the src folder.

### The directory "Weka Files" contains files needed to do classification in Weka. They will be needed to be converted into .arff files using WEKA (we put the arff files up on github initially but downloading them converts them into .txt thus making them unreadable by WEKA). To convert the csv files into .arff: start WEKA and click Tools then ArffViewer. A new window will open then click File and Open then navigate to the directory where the files are. Once in that directory, click Files of Type and the file type to CSV data files. The file will be loaded and now click File and Save As and then click Save. This must be done for both files.

### The corresponding association rules mined using Weka can be found in the "Association Rules" folder.

### More information regarding this report (data files, slides, etc) can be found at our github repo: https://github.com/ndarwich/Crash-Analysis
