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

    >>> from PyAudit.basics import dtypes_class
    >>> df = pd.read_csv('Heart.csv', dtype={'Sex': bool})
    >>> (num_fields, cat_fields, bool_fields, data_types, type_class) = dtypes_class(df)
    >>> num_fields
    ['Age', 'RestBP', 'Chol', 'Fbs', 'RestECG', 'MaxHR', 'ExAng', 'Oldpeak', 'Slope', 'Ca']
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
    all_types['class'] = ['numeric' if x in num_types else
                          'bool' if x in bool_types else
                          'category' if x in cat_types else
                          'unknown' for x in all_types['dtypes'].tolist()]

    quant_fields = all_types[all_types['class'] == 'numeric']['feature'].tolist()
    quanl_fields = all_types[all_types['class'] == 'category']['feature'].tolist()
    bool_fields = all_types[all_types['class'] == 'bool']['feature'].tolist()
    return quant_fields, quanl_fields, bool_fields, data_types, all_types


def missing_rate(df_in):
    """
    calculate missing rate for each feature in the DataFrame

    :param df_in: input pandas DataFrame
    :return: missing rate

    :author: Wenqiang Feng and Ming Chen
    :email:  von198@gmail.com

    >>> import pandas as pd
    >>> d = {'A': [1, 0, None, 3],
             'B': [1, 0, 0, 0],
             'C': ['a', None, 'c', 'd']}
    >>> # create DataFrame
    >>> df = pd.DataFrame(d)
    >>> from PyAudit.basics import missing_rate
    >>> missing_rate(df)
             feature  missing_rate
           0       A          0.25
           1       B          0.00
           2       C          0.25
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

    >>> import pandas as pd
    >>> d = {'A': [1, 0, None, 3],
             'B': [1, 0, 0, 0],
             'C': ['a', None, 'c', 'd']}
    >>> # create DataFrame
    >>> df = pd.DataFrame(d)
    >>> from PyAudit.basics import zero_rate
    >>> zero_rate(df)
             feature  zero_rate
           0       A   0.333333
           1       B   0.750000
           2       C   0.000000
    """

    rate = ((df_in == 0).sum(axis=0)) / df_in.notnull().sum()
    # rename the column
    percentage_zero = pd.DataFrame(rate).reset_index()\
                        .rename(columns={'index': 'feature', 0: 'zero_rate'})
    return percentage_zero


def feature_variance(df_in):
    """
    calculate the variance for each feature

    :param df_in: input pandas DataFrame
    :return: feature variance

    :author: Wenqiang Feng and Ming Chen
    :email:  von198@gmail.com

    >>> import pandas as pd
    >>> d = {'A': [1, 0, None, 3],
             'B': [1, 0, 0, 0],
             'C': ['a', None, 'c', 'd']}
    >>> # create DataFrame
    >>> df = pd.DataFrame(d)
    >>> from PyAudit.basics import zero_rate
    >>> zero_rate(df)
             feature  feature_variance
           0       A               1.0
           1       B               0.5
           2       C               1.0
    """

    rate = df_in.nunique() / df_in.notnull().sum()
    rate = pd.DataFrame(rate)\
             .reset_index()\
             .rename(columns={'index': 'feature', 0: 'feature_variance'})
    return rate






