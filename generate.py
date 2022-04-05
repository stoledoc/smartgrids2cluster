import pandas as pd

df1 = pd.read_parquet("data/all.parquet")
df2 = pd.read_parquet("results/all.parquet")

#%%
df1["cluster"] = df2["all"]

#%%
data = df1.filter(["cluster", *(map(str, range(24)))]).pipe(pd.melt, id_vars="cluster")

#%%
groups = data.groupby("cluster")

mean = groups.agg({"value": "mean"}).rename(columns={"value": "mean"})
std = groups.agg({"value": "std"})
min = groups.agg({"value": "min"})["value"].apply(lambda x: x if x > 0 else 0)
max = groups.agg({"value": "max"})
acum = groups.agg({"value": "sum"})

#%%
mean["std"] = std["value"]
mean["min"] = min
mean["max"] = max["value"]
mean["acum"] = acum

#%%
mean.to_excel("all_kvh.xlsx")
