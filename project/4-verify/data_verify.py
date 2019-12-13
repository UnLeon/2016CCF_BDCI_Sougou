# coding=utf-8

import numpy
import pandas as pd
import os

# real_id = pd.read_csv('verify.csv').ID
# real_age = pd.read_csv('verify.csv').age
# real_gender = pd.read_csv('verify.csv').gender
# real_edu = pd.read_csv('verify.csv').edu

real_file = pd.read_csv('Verify.csv')
test_file = pd.read_csv('Submit.csv')

# 准确率计算
age_correct = test_file[test_file.ID==real_file.ID and test_file.age==real_file.age]
P_age = sum(age_correct.age)/sum(test_file.age)
R_age = sum(age_correct.age)/sum(real_file.age)

# line = []
# real_file = open('verify.csv')
# test_file = open('submit.csv')

# for i in real_file.readline():
#     i=i[0:-1]
#     if len(i) != 0 and len(i) != 1:
#         line.append(i.split('\t'))
# df_real = pd.DataFrame(line,columns=['ID','age','gender','edu'])
#
# for i in test_file.readline():
#     i=i[0:-1]
#     if len(i) != 0 and len(i) != 1:
#         line.append(i.split('\t'))
# df_test = pd.DataFrame(line,columns=['ID','age','gender','edu'])

# #   age准确率计算
# correct = df_test[df_real.ID==df_test.ID and df_real.age==df_test.age]
# for i in (0,1,2,3,4,5,6):
#     R = sum(correct.age==i)/sum(df_real.age==i)
#     P = sum(correct.age==i)/sum(df_test.age==i)
#     F = R*P*2/(R+P)
#     print i, ':\n', 'R=', R, ' P=', P, ' F=', F
