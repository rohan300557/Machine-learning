import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
df1  = pd.read_csv("cereal.csv")

# Q1.) Load the data from “cereal.csv” and plot histograms of sugar and vitamin content across different cereals.

# print(df1)
# plt.hist([df1["sugars"], df1["vitamins"]],color=['orange', 'green'])
# plt.xlabel("Sugars and Vitamins")
# plt.legend(["Sugars", " Vitamins"])   ##uses the text from the DisplayName properties of the data series.
# plt.show()

## Q2.)  ################################################################

## A.)
# dict={'N': 'Nabisco','Q':'Quaker Oats','K':'Kelloggs','R':'Raslston Purina','G':'General Mills','P':'Post','A':'American Home Foods Products' }
# df1["manufactures"] = [dict[mfr] for mfr in df1["mfr"]]
# print(df1)


## B.)
# sb.set(style='dark')
# dict={'N': 'Nabisco','Q':'Quaker Oats','K':'Kelloggs','R':'Raslston Purina','G':'General Mills','P':'Post','A':'American Home Foods Products' }
# df1["manufactures"] = [dict[mfr] for mfr in df1["mfr"]]
# t1 = sb.countplot(x = 'manufactures',data=df1,facecolor=(0, 0, 0, 0),linewidth=3,edgecolor=sb.color_palette("dark", 3))
# plt.show()


# Q3.
# t1 = df1.corr()
# t2 = sb.heatmap(t1,annot=True)
# plt.show()
x_train = train_test_split(df1)
print(x_train)