#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#print(abs(-5))
#help(abs)
#help(print)
#print('*' *80)
'''
def calc(num1,num2):
    res=num1+num2
    return  res
print(calc(3,5))
'''
'''
def my_abs(x):
    if x >= 0 :
        return x
    else:
        return -x
print(my_abs(-8))
'''


def errabs(x):
    #doc string ,manual
    """
    This is RFM

    """
    if not isinstance(x,(int,float)):
        raise TypeError('wrong argument')
    if  x >= 0:

        return x
    else:
        return -x
print(errabs(-12.5))
print(errabs('hello'))

print(help(errabs))

