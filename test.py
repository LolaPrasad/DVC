import pandas as pd 

data = [
    {"name":"Prasad","age" : 23,"city":"Solapur" },
    {"name":"Alice","age" : 25,"city":"pune" },
    {"name":"Tom","age" : 32,"city":"delhi" },
    {"name":"Ben","age" : 36,"city":"chennai" }
]

df=pd.DataFrame(data)

df.to_csv("data/data.csv",index=False)

