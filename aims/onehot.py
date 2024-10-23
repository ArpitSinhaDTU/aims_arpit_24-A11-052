import pandas as pd
data = {'RANG': ['Red', 'Green', 'Blue','Green']}
df = pd.DataFrame(data)
df_one_hot = pd.get_dummies(df, columns=['RANG'],prefix='is',prefix_sep=' ')

print(df_one_hot)

