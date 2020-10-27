from FireflyAlgorithm import *
import pandas as pd 
import numpy as np
df=np.random.randint(30,100,(10,3))
df=pd.DataFrame(df,columns=['no_of_vehicle','avg_speed','avg_distance_btw_them'])
df.to_csv('data.csv')
df=df.values
prob_dim=(len(df))
pop_size=10
data_set=[[0 for x in range(prob_dim)] for x in range(pop_size)]

def generate(df):
    no_of_lane=prob_dim
    for i in range(pop_size):
        for j in range(no_of_lane):
            data_set[i][j]=((df[j][0]*df[j][1])//df[j][2])*np.random.rand()
            # print(data_set[i][j])
    return data_set
    

data_set=generate(df)  
# print(data_set)


def function(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val




Algorithm = FireflyAlgorithm(10, 10, 100, 0.5, 0.2,0.9,120, 180, function,data_set)
Best = Algorithm.Run()

print ('best solution is',Best[0], 'and time gained',round(Best[1]),'mins')
