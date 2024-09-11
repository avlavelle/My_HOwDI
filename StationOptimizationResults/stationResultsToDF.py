import scipy.io
import pandas as pd
import numpy as np

def load_mat_and_set_df(file_path):
    # loading in the matlab file
    mat_file = scipy.io.loadmat(file_path)

    # finding the name of the matlab structure, in our trial it is StationListReduced3
    # we are assuming that the structure name is the fourth key in the mat_file dictionary based on the pattern of our trial data
    struct_name = list(mat_file.keys())[3]  

    # accessing the matlab structure
    mat_structure = mat_file[struct_name][0,0]

    # all fields from the matlab structure: ('ID', 'Lat', 'Long', 'Mins', 'TruckCount', 'Fuel') 
    all_fields = mat_structure.dtype.names

    # fields for our dataframe; mins and truckcount are excluded
    df_fields = ['Station ID', 'Latitude', 'Longitude', 'Total Daily Fuel']

    # initializing an empty dataframe
    stationResults = pd.DataFrame()

    # setting the data for the ID, Lat, and Long columns
    stationResults['Station ID'] = mat_structure["ID"][:, 0]
    stationResults['Latitude'] = mat_structure["Lat"][:, 0]
    stationResults['Longitude'] = mat_structure["Long"][:, 0]

    # calculating the fuel for each station across 1440 minutes
    daily_fuel = np.sum(mat_structure["Fuel"], axis=0, keepdims=True)

    # tranposing the (1,22) daily_fuel array so it is (22,1)
    daily_fuel = np.transpose(daily_fuel)

    # setting the data for the Total Daily Fuel column
    stationResults['Total Daily Fuel'] = daily_fuel[:, 0]

    return stationResults


if __name__ == "__main__":

    # call above function
    results = load_mat_and_set_df('H2LA_Station_Optimization_Results_2024_08_09.mat')

    # write the results stationResults DF to a csv
    results.to_csv('H2LA_Station_Optimization_Results.csv', index=False)

