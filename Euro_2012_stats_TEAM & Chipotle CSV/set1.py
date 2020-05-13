import pandas as pd

############################### todo:-  chipotle.tsv

df = pd.read_csv("chipotle.tsv",sep='\t')
# print(df)

prices = [float(value[1 : -1]) for value in df.item_price]
df.item_price = prices
#####todo:------- OR ------
# lis=[]
# for a in df['item_price']:
#     lis.append(float(a[1:]))
# df['item_price'] = pd.DataFrame(lis)


# # Q 1.
# print(len(df[df["item_price"] > 10.00]))

# # Q 2.
# print(df[df['quantity']==1].groupby('item_name')['item_name','item_price'].head())


# # Q 3.
# max_price = max(df['item_price'])
# print(df[df['item_price'] == max_price])

# # Q 4.
# name = (df[df['item_name']=='Veggie Salad Bowl' ])
# print(len(name))

# # Q 5.
# print(len(df[(df['item_name']=='Canned Soda')&(df['quantity']>1)]))

#######################################################################################################
################33333### todo:-  Euro_2012_stats_TEAM.csv

df1=pd.read_csv('Euro_2012_stats_TEAM.csv')

# print(df1)
# print(df1.isnull().sum())

# # Q 6.
# discipline = df1[['Team','Yellow Cards', 'Red Cards']]
# print(discipline)

# # Q 7.
# discipline = df1[['Team','Yellow Cards', 'Red Cards']]
# discipline = discipline.sort_values(['Yellow Cards'],ascending=False)
# discipline = discipline.sort_values(['Red Cards'],ascending=False)
# print(discipline)

# # Q 8.
# print(round(df1['Yellow Cards'].mean()))    ##todo:- Round Will give the nearest value with decimal 0.

# # Q 9.
# df1 = df1[(df1['Goals']>6)]
# print(df1[['Team','Goals']])

# # Q 10.
print(df1[df1.Team.str.startswith('G')]['Team'])
######## todo:-  --------------- OR ------
# lis1=[]
# for a in df1['Team']:
#     if 'G' in a:
#         lis1.append(a)
# for a in lis1:
#     print(df1['Team'][df1['Team'] == a])