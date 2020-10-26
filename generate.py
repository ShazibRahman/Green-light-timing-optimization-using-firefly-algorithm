import pandas as pd 
import numpy as np
df=np.random.randint(100,999,(7,6))

df=pd.DataFrame(df)



df.to_csv('data.csv')
