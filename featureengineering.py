from sklearn import preprocessing
le = preprocessing.LabelEncoder()
import pandas as pd
from datapreprocessing import data_preprocessing
from scipy import stats
import numpy as np

def remove_outliers(data,par):
        print(par)
        print(data.info())
        z = np.abs(stats.zscore(data[par]))
        a=np.where(z > 3)
        for i in a[0]:
            if i in data.index:
                data.drop(index=i,inplace=True)


def feature_engineering():
    dataset = data_preprocessing()
    categorical_columns = []
    numerical_columns = []        
    for col in dataset.columns:
        if dataset[col].dtypes == object:
            categorical_columns.append(col)
        else:
            numerical_columns.append(col)
        # if col in ['Item_Visibility']:
            remove_outliers(dataset,col)
    
    print(categorical_columns) 
    print(numerical_columns)
    # Changing the categorical columns to numerical by using the label encoding method.
    for c in categorical_columns:
        dataset[c] = le.fit_transform(dataset[c])
        remove_outliers(dataset,c)
    # for col in dataset.columns:
    #     remove_outliers(dataset,col)
    # Performing the one hot encoding for some categorical values which contains less than 3 unique values
    # dataset = pd.get_dummies(dataset, columns=['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Outlet_Type'])
    dataset.drop('Outlet_Establishment_Year', axis=1, inplace=True)
    dataset.drop('Outlet_Identifier', axis=1, inplace=True)
    dataset.to_csv("cleaned_data.csv", index = False)
    return dataset
feature_engineering()
