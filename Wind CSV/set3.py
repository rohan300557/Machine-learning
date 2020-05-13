import pandas as pd
import datetime

df = pd.read_csv("wind.data.txt",delimiter= '\s+')
# print(df)



# # Q 1.
df.insert(0,'Yr_Mo_Dy',pd.to_datetime(df.Yr*10000+df.Mo*100+df.Dy,format='%y%m%d'))
df.drop(['Yr','Mo','Dy'],inplace=True,axis=1)
# print(df)



# # Q 2.
def fix(dt):
    if dt.year > 1989:
        year = dt.year - 100
    else:
        year = dt.year
    return datetime.date(year,dt.month,dt.day)
df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix)
# print(df)
#### todo: ----- OR --------
# for a in range(61,69):
#     df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].mask(df['Yr_Mo_Dy'].dt.year == int('20'+str(a)),df['Yr_Mo_Dy'] + pd.offsets.DateOffset(year=int('19'+str(a))))



# # Q 3.
df = df.set_index('Yr_Mo_Dy')
print(df.isnull().sum())
#


# # Q 4.
# print(df.notna().sum())



# # Q 5.
# loc_stats = df.describe(percentiles=[])
# print(loc_stats)
######todo: ------ OR ------
# loc_stats = df.describe()



# # Q 6.
# day_stats = pd.DataFrame()
# day_stats['min'] = df.min(axis=1)
# day_stats['max'] = df.max(axis=1)
# day_stats['mean'] = df.mean(axis=1)
# day_stats['std'] = df.std(axis=1)
# print(day_stats)



# # Q 7.
# print(df[(df.index.month==1)].mean())