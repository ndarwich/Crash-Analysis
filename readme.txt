This project analyzes crash data from the city of Chicago.

TO RUN THE SOURCE CODE:
Go to https://github.com/ndarwich/Crash-Analysis and download ALL the files in the data folder and put them into the data folder in the project directory otherwise the code will not run.

If interested in running map code:
Go to https://github.com/ndarwich/Crash-Analysis then go to the src folderr and download ChicagoPopulation.csv (put it in src) and the contents in  cb_2017_us_zcta510_500k (put them in cb_2017_us_zcta510_500k in the same folder name found in src). These files must be put into the same locations they are found on the github otherwise the map code WILL NOT work.
Basemap is required. If installed, simply uncomment two lines of code at the bottom of main() (this is described in the code comments as well)

TO RUN WEKA ON FILES:
Go to https://github.com/ndarwich/Crash-Analysis and download the two .csv files found in Weka Files and put them in the same directory (train_file and final-test-NEW). They will be needed to be converted into .arff files using WEKA (we put the arff files up on github initially but downloading them converts them into .txt thus making them unreadable by WEKA). To convert the csv files into .arff: start WEKA and click Tools then ArffViewer. A new window will open then click File and Open then navigate to the directory where the files are. Once in that directory, click Files of Type and the file type to CSV data files. The file will be loaded and now click File and Save As and then click Save. This must be done for both files.

The original datasets can be found at the following links:

Crashes - https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if
Vehicles - https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3
People - https://data.cityofchicago.org/Transportation/Traffic-Crashes-People/u6pd-qa9d

The original datasets have been modified by us (by joining the tables, normalizing the data, data cleaning, etc) and can be found in the data folder.

Source code (used to do data transformations, mapping visualizations, etc) can be found in the src folder.

Weka Files contains all the appropriate files needed to do classification in Weka. oversampledtrain_strings.arff is used for training the classifier and final-test-NEW.arff is used as testing data on the classifier. Both training and test use INJURY_CLASSIFICATION as the label to predict.

The corresponding association rules mined using Weka can be found in the Association Rules folder.

Nore information regarding this report (data files, slides, etc) can be found at our github repo: https://github.com/ndarwich/Crash-Analysis

