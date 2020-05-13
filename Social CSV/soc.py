import pandas as pd
df = pd.read_csv("social.csv")  ######### sep = '|'
# print(df)
# print(df.head())    ###### give first five value if no passed other if 10 then 1o data will be show
# print(df.tail())   ####### show the the bottom data
# print(df.describe())
# print(df["User ID"])
# print(df["User ID"].describe())
# print(df[["User ID","Age"]])
# print(df.columns)
# df1 = df.drop("Gender",axis=1)   ###### Remove the particular column
# print(df1)

# df.drop(["Gender","Age"],axis=1,inplace=True)   ###### Remove two column
# print(df)

# print(df.drop(0))   ###### Remove the particular row
# print(df.drop([1,2,3]))###### Remove the particular row

# print(df[(df['Gender']=='Male')&(df['Purchased']==1)])    ###########3 To show particular column

# print(df[(df['Gender']=='Male')&(df['Purchased']==1)][['Age','User ID']])    ###########3 To show particular column
# print(df.Gender.value_counts())   #########To count the no. of Male aNd Female
# print(df.Purchased.value_counts())
# print(df.loc[:,['Age','Gender']])
# print(df.loc[1,['Age','Gender']])         ############ show the age and gender of 1 row
# print(df.loc[15:20])       ############### print 15 to 20th data
# print(df.iloc[1,1])    ###############print 1 row 1 column data
# print(df.iloc[2:25,1:3])   ############## row,column

