# import python libraries
import os
import sys
import pandas as pd

# import PyAudit module
from PyAudit.basics import auditing

# Audit output path
output = os.path.abspath(os.path.join(sys.path[0])) + '/output'

# load DataFrame
df = pd.read_csv('Heart.csv', dtype={'Sex': bool})
print(df.head(5))

# generate the audit results (.csv files in output folder)
num_summary, cat_summary, corr = auditing(df, output)

# the following is optional, since the .csv files are in the output folder
print(num_summary)
print(cat_summary)
print(corr)