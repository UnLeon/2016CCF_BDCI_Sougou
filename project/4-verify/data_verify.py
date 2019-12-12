# conding = utf-8
import numpy
import pandas
import os

line = []
real_file = open()
test_file = open()

for i in real_file.readline():
    i=i[0:-1]
    if len(i) != 0 and len(i) != 1:
        line.append(i.split('\t'))
df_real = pandas.DataFrame(line,columns=['ID','age','gender','edu'])

for i in test_file.readline():
    i=i[0:-1]
    if len(i) != 0 and len(i) != 1:
        line.append(i.split('\t'))
df_test = pandas.DataFrame(line,columns=['ID','age','gender','edu'])

#   age准确率计算
correct = df_test[df_real.ID==df_test.ID and df_real.age==df_test.age]
for i in (0,1,2,3,4,5,6):
    R = sum(correct.age==i)/sum(df_real.age==i)
    P = sum(correct.age==i)/sum(df_test.age==i)
    F = R*P*2/(R+P)
    print i, ':\n', 'R=', R, ' P=', P, ' F=', F