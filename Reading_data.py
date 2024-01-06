import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

#Load csv file into a dataframe
House_Information = pd.read_csv("City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv")

print(House_Information.head())

print(House_Information.describe())
print(House_Information.RegionName.unique)
print(House_Information.RegionName.nunique)


Philadelphia_Values = House_Information.loc[House_Information.RegionName == 'Philadelphia'] 
Philadelphia_Value = Philadelphia_Values.loc[House_Information.State == "PA"]
print(Philadelphia_Value)


