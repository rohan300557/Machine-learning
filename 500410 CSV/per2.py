import datetime as dt
import pandas as pd
df = pd.read_csv("500410 (1).csv")
df['Date']=pd.to_datetime(df['Date'])
dic = {'Date_i':[],'Productivity':[]}
for q in df['Date'].dt.year.unique():
    for q1 in range(1,13):
        a1 = df[(df['Date'].dt.year == q) & (df['Date'].dt.month == q1)]
        for a2 in a1['Date']:
            current = a2.date()
            a = 1
            while True:
                current1 = current - dt.timedelta(days = a)
                if ((df['Date']==current1).any()):
                    break
                elif (current == min(df['Date'])):
                    break
                else:
                    a = a+1
            # print(current1)
            try:
                a3 = df[df['Date']==current]['Close Price'].values[0]
                a4 = df[df['Date']==current1]['Close Price'].values[0]
                per = (((a4-a3)/a4)*100)
                dic['Date_i'].append(current)
                dic['Productivity'].append(per)
                # print(per)
            except:
                pass
q = pd.DataFrame(dic)
q.to_csv("per2.csv")
