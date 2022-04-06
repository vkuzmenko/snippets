import pandas as pd

pd_csv = pd.read_csv('./1.csv')
pd_json = pd.read_json('./1.json')

res = pd.merge(pd_json, pd_csv, on=['col1','col2'], how='left')

res.to_csv('./out.csv', index=False)
