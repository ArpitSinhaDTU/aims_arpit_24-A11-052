import pandas as pd
data = {'CATEGORY': ['GRANDE','VENTI','TRENTA','VENTI']}
df=pd.DataFrame(data)

new={'GRANDE': 1,'VENTI':2,'TRENTA':3}

df['category encoding']=df['CATEGORY'].map(new)

print(df)

