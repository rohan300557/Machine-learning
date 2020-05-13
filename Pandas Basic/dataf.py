import pandas as pd
d1 = {'a':5,'b':10,'c':12,'d':13}    #### the datatype is int
d2 = {'a':5,'c':10,'f':13,'g':14}    #### the datatype is int
x = pd.Series(d1)
y = pd.Series(d2)
q = pd.DataFrame({'a':x,"b":y,'c':x+y})
# print(q)
# print(q[q.isnull()])       ########## which is NAN
# print(q[q['a'].isnull()])    ########## Show the column NAN
print(q.isnull().sum())


########### using day time to check the month performance
########To check Performance   formula = [[7 jan closing price - 8 jan today price]/[7 jan previous closing price ]]*100
######  which is the best month in the year

# to get the performace of jan 2018 we g=have to find the performance of dec 2017


