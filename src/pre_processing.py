import os
import numpy as np
import pandas as pd 
import math 
import random 


# Xóa dữ liệu dư thừa và những hàng có nhiều giá trị NaN
def drop_missing_big_data(df):

    del df['Unnamed: 0']
    del df['ID']
    del df['Delivery_person_ID']

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

    return df


# Điền các giá trị khuyết 
def filling_missing_data(df):

    df["Delivery_person_Age"] = df["Delivery_person_Age"].replace(to_replace = np.NaN, value= random.choice(np.array(df["Delivery_person_Age"])))
    df["Multiple_deliveries"] = df["Multiple_deliveries"].replace(to_replace = np.NaN, value= random.choice(np.array(df["Multiple_deliveries"])))
    df["Road_traffic_density"] = df["Road_traffic_density"].replace(to_replace = np.NaN, value= random.choice(np.array(df["Road_traffic_density"])))
    df["Weather_conditions"] = df["Weather_conditions"].replace(to_replace = np.NaN, value= random.choice(np.array(df["Weather_conditions"])))
    df["Delivery_person_ratings"] = df["Delivery_person_ratings"].replace(to_replace = np.NaN, value= random.choice(np.array(df["Delivery_person_ratings"])))
    df["Festival"] = df["Festival"].replace(to_replace = np.NaN, value= random.choice(np.array(df["Festival"])))

    return df


# Chỉnh sửa sắp xếp lại dataframe 
def edit_dataframe(df):

    # Để feautures Time_taken_(min) (Labels) ra cuối cùng 
    columns = df.columns.tolist()
    colums_new = columns[:-2] + columns[-1:] + columns[-2:-1]
    df = df[colums_new]

    # Sắp xếp theo thứ tự 


    return df


def clear_data(df):
    df = drop_missing_big_data(df)      # Xóa dữ liệu dư thừa và những hàng có nhiều giá trị NaN
    df = filling_missing_data(df)       # Điền các giá trị khuyết 
    df = create_feature_distance(df)    # Khởi tạo feature distance dựa trên 4 feature có sẵn gồm kinh độ/ vĩ độ của 2 địa điểm
    df = edit_dataframe(df)             # Chỉnh sửa sắp xếp lại dataframe 

    return df



# Save file csv
def save_data_csv(df, path):
    df.to_csv(path)


# main
def main(df,path_save_new):
    df = clear_data(df)
    print(df[:5])
    #save_data_csv(df, path_save_new)

