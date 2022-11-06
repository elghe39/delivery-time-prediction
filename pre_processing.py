def data_information_basic(df):
    print(df.info())
    print("-------------------------------------------------------------------------------")

    print(df.isnull().sum())
    print("-------------------------------------------------------------------------------")

    print((df.isna().sum())*100/ ((df.isna().sum()) + (df.notna().sum())))









def save_data_csv(df, path_save):
    df.to_csv(path_save) 

def main(df, path):
    data_information_basic(df)
    # save_data_csv(df, path)