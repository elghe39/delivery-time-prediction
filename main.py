import create_data
import pre_processing
import os
import pandas as pd 

def main():

    # Tổng hợp tất cả dữ liệu (file .txt) vào 1 file .csv  
    # Dữ liệu lưu tại file dataset.csv

    # path = "D:/Github/Predict_the_time_of_arrival_for_the_delivery_persons/dataset/data"
    # path_save = "D:/Github/delivery-time-prediction/dataset/data_new/dataset.csv"
    # os.chdir(path)
    # create_data.main(path, path_save)

    # ----------------------------------------------------------------------------------
    # Pre-processing - Sử dụng file csv mới được tạo để xử lý lại dữ liệu 

    # Đọc file dữ liệu csv mới được tạo 
    df = pd.read_csv("D:/Github/delivery-time-prediction/dataset/data_new/dataset.csv")
    # Xử lý
    path_save_new = "D:/Github/delivery-time-prediction/dataset/data_new/dataset_new.csv"
    pre_processing.main(df, path_save_new)

    # Dữ liệu sau khi xử lý được lưu tại D:/Github/delivery-time-prediction/dataset/data_new/dataset_new.csv



    # EDA + deploy 
    # Nhóm sẽ tiến hành trên file dataset_new.csv 



    # Model 

if __name__ == '__main__':
    main()