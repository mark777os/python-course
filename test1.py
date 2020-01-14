""" Программа преобразует трехзначное число в сумму цифр
     этого числа.
"""
x = int(input('Enter a three digit number  '))
z = x//100
y= (x-z*100)//10
c = x-y*10-z*100
print('your digit sum=  ', c+y+z)
'''and now this programm work under git control'''
print('play under git control')