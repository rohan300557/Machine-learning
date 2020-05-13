# pag 15----Statistical learning
import numpy as np
import matplotlib.pyplot as mlt
y = [1, 2, 3, 4]
x = [13, 25, 36, 41]
col = ["red","yellow","green","blue"]
# mlt.plot(x,y)
# mlt.plot(x,y,'azure')
# mlt. bar(x,y,width=1)   #######  width to change the width of the bar
# mlt.bar(x, y, width=1, align='edge') #######################  To align the bars on the edge or center(by default)
# mlt. bar(x,y,color = col)
# mlt. bar(x,y,edgecolor = 'red')

mlt.xlabel('x axis ---------->')
mlt.ylabel('some numbers')

# mlt. hist(x)

# mlt.scatter(x,y,marker='*')

# mlt.pie(x)
# mlt.pie(x,labels=['a','b','c','d'])
# mlt.pie(x,labels=['a','b','c','d'],explode=[0,0,1,0])
# s= [0, 10, 0.1]
r  = np.arange(0, 18, 0.1)
q = np.sin(r)
# mlt.plot(x,y,marker='o')
# mlt.plot(x,y,linestyle='dashed')
print(mlt.show())







