import pre_processing
import pandas as pd
import os


def main():
    # Read .csv file
    df = pd.read_csv(os.path.abspath("../delivery-time-prediction/dataset/dataset.csv"))
    # Clean data
    path_save_new = os.path.abspath("../delivery-time-prediction/dataset/dataset_clean.csv")
    #pre_processing.main(df, path_save_new)
    df = pd.read_csv(path_save_new)
    print(df[-10:])


    # EDA + deploy
    # Nhóm sẽ tiến hành trên file dataset_clean.csv

    # Model


if __name__ == '__main__':
    main()
