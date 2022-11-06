import os
import numpy as np
import pandas as pd 
import math 

# Xóa dữ liệu dư thừa và những hàng có nhiều giá trị NaN
def drop_data_missing_big(df):
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


# Tính khoảng cách giữa cửa hàng và nơi giao hàng 
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295;   
    c = math.cos
    a = 0.5 - c((lat2 - lat1) * p)/2 + c(lat1 * p) * c(lat2 * p) * (1 - c((lon2 - lon1) * p))/2

    return 12742 * math.asin(math.sqrt(a))


# Khởi tạo feature distance dựa trên 4 feature có sẵn gồm kinh độ/ vĩ độ của 2 địa điểm
def create_feature_distance(df):
    # Khởi tạo cột Distance có tất cả giá trị đều bằng 0
    df["Distance"] = 0

    for i in range(len(df)):
        df["Distance"][i:i+1] = distance(df["Restaurant_latitude"][i:i+1], df["Restaurant_longitude"][i:i+1],
                                        df["Delivery_location_latitude"][i:i+1],df["Delivery_location_longitude"][i:i+1])

    # Để feautures Time_taken_(min) (Labels) ra cuối cùng 
    columns = df.columns.tolist()
    colums_new = columns[-1:] + columns[:-1]
    df = df[colums_new]

    return df

def main():
    df= pd.read_csv(os.path.abspath("../delivery-time-prediction/dataset/dataset.csv"))
    df = drop_data_missing_big(df)
    df = create_feature_distance(df)
    print(df[:5])

if __name__ == '__main__':
    main()
