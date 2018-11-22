#!/anaconda3/bin/python
# coding=UTF-8

#================================================================
#   Copyright (C) 2018 HALO Ltd. All rights reserved.
#   
#   文件名称：practice_day2.py
#   创 建 者：Zhangdunfeng
#   创建日期：2018-11-20 23:43:17
#   描    述：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
#
#================================================================

i = int(input('净利润：'))

incomes = [1000000, 600000, 400000, 200000, 100000, 0]
rates = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
total=0;

for index in range(len(incomes)):
    if i > incomes[index]:
        total+=(i - incomes[index])*rates[index]
        print ((i - incomes[index])*rates[index])
        i = incomes[index]

print (total)



