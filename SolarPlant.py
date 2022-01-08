import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

class SolarPV:
    def __init__(self):
        self.P1_G=pd.read_csv(r"C:\Datasets-base\Datasets\Solar_power_generation_data\Plant_1_Generation_Data.csv")
        self.P2_G=pd.read_csv(r"C:\Datasets-base\Datasets\Solar_power_generation_data\Plant_2_Generation_Data.csv")
        self.P1_WSn=pd.read_csv(r"C:\Datasets-base\Datasets\Solar_power_generation_data\Plant_1_Weather_Sensor_Data.csv")
        self.P2_WSn=pd.read_csv(r"C:\Datasets-base\Datasets\Solar_power_generation_data\Plant_2_Weather_Sensor_Data.csv")
        self.Plant_df=[self.P1_G,self.P2_G,self.P1_WSn,self.P2_WSn]      #list with plant dataframes

    def CheckNullValues(self,Dataset):
        Null = Dataset.isnull().sum()
        Na = Dataset.isna().sum()
        if Null.sum()==0 and Na.sum()==0:
            return 1
        else:
            return 0 
    

    
    def main(self):
        for idx, df in enumerate(self.Plant_df):
            ctrl_NA=self.CheckNullValues(df) 
            if ctrl_NA==0:
                print('........Valores invalidos......')
            if idx==0:
                df['DATE_TIME']=pd.to_datetime(df['DATE_TIME'], format='%d-%m-%Y %H:%M')
            else:
                df['DATE_TIME']=pd.to_datetime(df['DATE_TIME'], format='%Y-%m-%d %H:%M:%S')
            df.sort_values(by=['DATE_TIME'])    #ordenar dados
        source_key_p1=self.Plant_df[0]['SOURCE_KEY'].unique()
        source_key_p2=self.Plant_df[1]['SOURCE_KEY'].unique()
        return source_key_p1, source_key_p2
    
 
    
