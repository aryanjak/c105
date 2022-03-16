import pandas as pd
import plotly.express as ps
import math
import csv

with open('C105/data.csv') as f:
    reader = csv.reader(f)
    filedata = list(reader)

marks = filedata[0]

#df = pd.read_csv("C105/data.csv")
#marks = df['Marks'].tolist()

sum = 0
print(marks)
for m in marks:
    sum = sum+int(m)

mean = sum/len(marks)

sigma = 0
for x in marks:
    xi = int(x)-mean
    sq = xi*xi
    sigma = sigma+sq

n = len(marks)

sd = sigma/(n-1)
std = math.sqrt(sd)
print(std)