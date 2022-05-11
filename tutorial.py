# %%
import numpy as np 
import pandas as pd 

# %%
In [2]: lista=[1,2,4,6]
nplista=np.array(lista)
pdlista=pd.Series(lista)

print(lista*10)

# %%
df = pd.read_csv("insurance.csv")
df 
# %%
df.head(10)
# %%
df.tail(1)
# %%
df.sample(10)
# %%
df.describe()
# %%
df.info()

# %%
df[['age']]

# %%
df[['age','bmi']]

# %%
df[-2:]
# %%
df[-3:]
# %%
df[:2][['age','bmi']]

# %%
df[10:11]
# %%
df.iloc[[10]]
# %%
df.mean()

# %%
df.mode()
# %%
df['age'].quantile([0.25,0.5,0.75])
# %%
iqr=(df['age'].quantile(0.75))-(df['age'].quantile(0.25))
bigote_iz=27-1.5*24
bigote_de=51+1.5*24
print(bigote_iz)
print(iqr)
print(bigote_de)

# %%

# %%
