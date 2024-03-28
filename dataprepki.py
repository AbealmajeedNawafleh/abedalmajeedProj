# DataPrepKit Project
# Abedalmajeed Nawafleh
import pandas as pd
import numpy as np


class DataPrepKit:

    def __init__(self):
        pass

    def read_csv(self, file_name):
        file_path = '{}.csv'.format(file_name)
        try:
            c = pd.read_csv(file_path)
            return c
        except FileNotFoundError:
            print("Error: File {} not found.".format(file_path))

    def read_excel(self, file_name):
        file_path = '{}.xlsx'.format(file_name)
        try:
            return pd.read_excel(file_path)
        except FileNotFoundError:
            print("Error: File {} not found.".format(file_path))

    def read_json(self, file_name):
        file_path = '{}.json'.format(file_name)
        try:
            return pd.read_json(file_path)
        except FileNotFoundError:
            print("Error: File {} not found.".format(file_path))

    def handle_missing_values(self, dataframe):
        if dataframe.isnull().sum().sum() > (0):
            dataframe = dataframe.fillna(0)
            return dataframe
        else:
            print('There are not Null Values')
            return dataframe

    def encode_categorical(self, dataframe, columns=None, method='one-hot'):
        if columns is None:
            columns = dataframe.select_dtypes(
                include=['object']).columns.tolist()

        if method == 'one-hot':
            return pd.get_dummies(dataframe, columns=columns)
        elif method == 'label':
            for col in columns:
                dataframe[col] = dataframe[col].astype('category').cat.codes
                return dataframe
        else:
            raise ValueError("Invalid method.")

    def data_summary(self, dataframe):
        summary = {}
        summary['mean'] = dataframe.mean()
        summary['median'] = dataframe.median()
        summary['mode'] = dataframe.mode().iloc[0]
        summary['std_dev'] = dataframe.std()
        return summary


if __name__ == "__main__":
    data_prep = DataPrepKit()
    file_name = input(
        "Enter the name of the dataframe file without the extension: ")
    dataframe = data_prep.read_csv(file_name)
    dataframe1 = data_prep.read_excel(file_name)
    dataframe2 = data_prep.read_json(file_name)
    if dataframe is not None:
        print("\nDataframe preview:")
        d = data_prep.handle_missing_values(dataframe)
        d1 = data_prep.encode_categorical(d)
        d2 = data_prep.data_summary(d1)
        print(dataframe, d, d1, d2)
    elif dataframe1 is not None:
        print("\nDataframe preview:")
        f = data_prep.handle_missing_values(dataframe1)
        f1 = data_prep.encode_categorical(f)
        f2 = data_prep.data_summary(f1)
        print(dataframe1, f, f1, f2)
    elif dataframe2 is not None:
        print("\nDataframe preview:")
        g = data_prep.handle_missing_values(dataframe2)
        g1 = data_prep.encode_categorical(g)
        g2 = data_prep.data_summary(g1)
        print(dataframe2, g, g1, g2)
    else:

        print("\nExiting program due to file error.")
