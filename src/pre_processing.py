import os
import numpy as np
import pandas as pd 
import math 

def drop_data_missing(df):
    # Xóa cột "Unnamed: 0" 
    del df['Unnamed: 0']

    # Xóa những hàng có trên 4 giá trị NaN
    for i in range(len(df)):
        if sum(np.array(df[i:i+1].isnull().sum())) > 3:
            df = df.drop(df[i:i+1].index)
    
    # Tạo lại cột index
    df["Index"] = 0
    for i in range(len(df)):
    df["Index"][i:i+1] = i 
    df.set_index("Index", inplace = True)
    return df



def main():
    df= pd.read_csv(os.path.abspath("../delivery-time-prediction/dataset/dataset.csv"))
    drop_data_missing(df)
    
if __name__ == '__main__':
    main()
