import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as mlt

df = pd.read_csv('train.csv')
# print(df)

# # Q 1...................................
df = df.set_index('PassengerId')
# print(df)

# # Q 2...................................
# gen= df['Sex'].value_counts().values.tolist()
# mlt.pie(gen,colors = ['blue', 'red'],explode=(0,0.1),labels=['Males','Females']
#         ,autopct='%.1f%%',startangle=90)
# mlt.show()


# # Q 3....................................
# def add_age(cols):
#     Age = cols[0]
#     Pclass = cols[1]
#     if pd.isnull(Age):
#         return int(df[df["Pclass"] == Pclass]["Age"].mean())
#     else:
#         return Age
# df["Age"] = df[["Age", "Pclass"]].apply(add_age,axis=1)
# sb.scatterplot(x = df['Age'], y=df['Fare'], hue=df['Sex'])
# mlt.show()

# # Q 4.....................................
# print(df[df['Survived']==1]['Survived'].count())

# # Q 5.....................................
# df['Fare'].plot.hist(alpha=0.5,color='blue' ,bins=50)
# mlt.show()