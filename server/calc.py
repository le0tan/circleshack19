import pandas as pd
import numpy as np

df = pd.read_csv("pred_table.csv")

code_lst = df['postal_code']
length = len(code_lst)

def from_postal_code_to_income_distribution(code: int, ranging = 10):
    target = np.argmin(np.abs(code_lst - code))
    lower_bound = max(0, target-ranging)
    upper_bound = min(length, lower_bound+2*ranging)
    bar = df["income_pred"].iloc[lower_bound:upper_bound].value_counts()
    pred = df["income_pred"].iloc[target]
    return {'Prediction': pred, "Distribution": dict(bar)}

# sample output
# result = postal_code_to_incomes(234567,15)
"""
{'Prediction': '$3,000 - $3,999', 'Distribution': $3,000 - $3,999    6
 $2,000 - $2,499    4
 $4,000 - $4,999    4
 Below $1,000       2
 $1,500 - $1,999    1
 $2,500 - $2,999    1
 $8,000 & Over      1
 $1,000 - $1,499    1
"""
