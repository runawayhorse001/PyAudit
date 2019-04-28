import numpy as np
import pandas as pd
from scipy.stats import norm


def dtypes_class(df_in):
    """
    numerical, categorical and bool name list in the DataFrame

    :param df_in: input pandas DataFrame
    :return: numerical, categorical and bool name list

    :author: Wenqiang Feng and Ming Chen
    :email:  von198@gmail.com
    """

    # quantitative data types in pandas dtypes
    num_types = ['int64', 'float64']
    # qualitative data types in pandas dtypes
    cat_types = ['object', 'datetime64', 'category']
    # bool data types in pandas dtypes
    bool_types = ['bool']

    all_types = pd.DataFrame(df_in.dtypes).reset_index() \
                  .rename(columns={'index': 'feature', 0: 'dtypes'})

    data_types = all_types.copy()
    type_indx = ['num' if x in num_types else
                 'bool' if x in bool_types else
                 'cat' if x in cat_types else
                 'unknown' for x in all_types['dtypes'].tolist()]

    all_types['class'] = type_indx

    quant_fields = all_types[all_types['class'] == 'num']['feature'].tolist()
    quanl_fields = all_types[all_types['class'] == 'cat']['feature'].tolist()
    bool_fields = all_types[all_types['class'] == 'bool']['feature'].tolist()

    return quant_fields, quanl_fields, bool_fields, data_types


def missing_rate(df_in):
    """
    calculate missing rate for each feature in the DataFrame

    :param df_in: input pandas DataFrame
    :return: missing rate

    :author: Wenqiang Feng and Ming Chen
    :email:  von198@gmail.com
    """

    rate = df_in.isnull().sum() / df_in.shape[0]
    # rename the column
    percentage_miss = pd.DataFrame(rate).reset_index()\
                        .rename(columns={'index': 'feature', 0: 'missing_rate'})

    return percentage_miss


def zero_rate(df_in):
    """
    calculate the percentage of 0 value for each feature in the DataFrame

    :param df_in: input pandas DataFrame
    :return: zero rate

    :author: Wenqiang Feng and Ming Chen
    :email:  von198@gmail.com
    """

    rate = ((df_in == 0).sum(axis=0)) / df_in.shape[0]
    # rename the column
    percentage_zero = pd.DataFrame(rate).reset_index()\
                        .rename(columns={'index': 'feature', 0: 'zero_rate'})

    return percentage_zero







