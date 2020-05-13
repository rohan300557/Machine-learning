import seaborn as sb
import matplotlib.pyplot as plt
tip_data = sb.load_dataset('tips')

# # Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='object')
# print(tip_data.head())     ######## Show the data from of the table
# print(tip_data.columns)     ######### show the columns of the table
# t1 = sb.scatterplot(x="total_bill", y="tip",data = tip_data)

# t1 = sb.scatterplot(x="total_bill", y="tip",hue='time',data = tip_data)
# t1 = sb.scatterplot(x="total_bill", y="tip",hue='time',style='time',data = tip_data)
# cmap = sb.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
# t1 = sb.scatterplot(x="total_bill", y="tip",palette="Set2",size="size",style='time',data = tip_data, hue="day")

# t1 = sb.lineplot(x="total_bill", y="tip",hue='day',lw=0.5,markers=True,data = tip_data)
# t1 = sb.lineplot(x="total_bill", y="tip",hue='day',data = tip_data)

# t1 = tip_data.corr()        #############CORR :- Use for making matrix of DataFrame
# t2 = sb.heatmap(t1)

# flights = sb.load_dataset("flights")
# flights = flights.pivot("month", "year", "passengers")
# x = sb.heatmap(flights)
#

# t1 = tip_data.corr()
# t2 = sb.clustermap(t1)


# sb.set(color_codes=True)
# iris = sb.load_dataset("iris")
# g = sb.clustermap(iris,figsize=(7, 5),row_cluster=False,dendrogram_ratio=(.1, .2),cbar_pos=(0, .2, .03, .4))

# t1 = sb.catplot(x="total_bill", y="tip",data = tip_data,kind="violin")

# t1 = sb.barplot(x="day", y="total_bill",data = tip_data)
# t1 = sb.barplot(x="day", y="total_bill",data = tip_data,linewidth=2.5, facecolor=(1, 1, 1, 0),errcolor=".2", edgecolor=".2")

# sb.set(style='dark')
# t1 = sb.countplot(x="day",data = tip_data)

t1 = sb.countplot(x="day",data = tip_data,facecolor=(0, 0, 0, 0),linewidth=5,edgecolor=sb.color_palette("dark", 3))
print(plt.show())