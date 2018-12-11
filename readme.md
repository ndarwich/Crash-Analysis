# An Investigation Into What Causes Crash Injuries, Fatalities

### This project analyzes crash data from the City of Chicago.

## The original datasets can be found at the following links:
### Crashes - https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if
### Vehicles - https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3
### People - https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d

### The original datasets have been modified (by joining the tables, binning the data, feature reduction, etc) and can be found in the "data" folder.

### Source code (used for data transformation, map visualizations, dictionaries, etc) can be found in the src folder.

### The directory "Weka Files" contains files needed to do classification in Weka. oversampledtrain_strings.arff is used for training the classifier and final-test-NEW.arff is used as testing data on the classifier. Both training and test use INJURY_CLASSIFICATION as the label to predict.

### The corresponding association rules mined using Weka can be found in the "Association Rules" folder.

### More information regarding this report (data files, slides, etc) can be found at our github repo: https://github.com/ndarwich/Crash-Analysis
