import numpy as np 
import pandas as pd
import os

# Tạo 1 dataframe 
def create_feature():
    arr = []
    df = pd.DataFrame(arr, columns=['ID', 'Delivery_person_ID', 'Delivery_person_Age','Delivery_person_Ratings','Restaurant_latitude','Restaurant_longitude'
    ,'Delivery_location_latitude','Delivery_location_longitude','Order_Date','Time_Orderd','Time_Order_picked','Weather_conditions','Road_traffic_density'
    ,'Vehicle_condition','Type_of_order','Type_of_vehicle','multiple_deliveries','Festival','City','Time_taken_(min)'])
    return df

# Đọc file .txt 
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()


# Lưu tất cả file txt vào list_information_all
def save_text_file(path):
    list_information_all = []

    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path}\{file}"
            list_information_all.append(read_text_file(file_path))
    return list_information_all 


# Hàm trả về mảng chứa thông tin của 1 tệp txt 
def information(text_information):
    list_information = []

    for i in range(20):
        text = text_information[i][27:]
        text = text.replace(' ', '')
        text = text.replace('\n', '')
        list_information.append(text)
    return list_information

# Trả về Dataframe chứa thông tin của tất cả dữ liệu của file txt 
def create_data_csv(list_information_all):
    df = create_feature()

    for i in range(len(list_information_all)):
        df.loc[i] = information(list_information_all[i])
    return df 

# Lưu dữ liệu, trả về đường link chứa file data mới tạo 
def save_data_csv(df, path_save):
    df.to_csv(path_save) 


def main(path, path_save):
    list_information_all = save_text_file(path)
    df =  create_data_csv(list_information_all) 
    save_data_csv(df,path_save)
    
