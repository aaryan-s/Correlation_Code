import pandas as pd
import plotly.express as px
import numpy as np

dataframe = pd.read_csv("correlationdata.csv")

print(dataframe)

CDS = list(dataframe["Cold drink sales"])
print(CDS)
ICS = list(dataframe["Ice-cream Sales"])
print(ICS)
Temp = list(dataframe["Temperature"])
print(Temp)
fig = px.scatter(dataframe,x="Temperature",y="Cold drink sales")
all = list(zip(Temp,CDS,ICS))
print(all)

corr = np.corrcoef(Temp,CDS)
print(corr[0,1])


# fig.show()



