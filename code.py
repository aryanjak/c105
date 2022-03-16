import pandas as pd
import plotly.express as ps
import math

df = pd.read_csv("C105/class1.csv")
marks = df['Marks'].tolist()

sum = 0

for m in marks:
    sum = sum+m

mean = sum/len(marks)

sigma = 0
for x in marks:
    xi = x-mean
    sq = xi*xi
    sigma = sigma+sq

n = len(marks)

sd = sigma/(n-1)
std = math.sqrt(sd)
print(std)