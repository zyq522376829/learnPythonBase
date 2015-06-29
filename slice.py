#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

def fact(n):
	return factIter(n, 1)

def factIter(num, product):
	if num == 1:
		return product
	return factIter(num - 1, num * product)

L = ['Michael', 'Sarach', 'Tracy', 'Bob', 'Jack']

>>> L = ['Michael', 'Sarach', 'Tracy', 'Bob', 'Jack']
>>>
>>> L
['Michael', 'Sarach', 'Tracy', 'Bob', 'Jack']
>>> L[0:3]
['Michael', 'Sarach', 'Tracy']
>>> L[:3]
['Michael', 'Sarach', 'Tracy']
>>> L[1:3]
['Sarach', 'Tracy']
>>> L[-2:]
['Bob', 'Jack']

>>> L = list(range(100))
>>> L
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 2
2, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 4
2, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 6
2, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 8
2, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> L[:10]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> L[-10:]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> L[10:20]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> L[:10:2]
[0, 2, 4, 6, 8]
>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> L[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 2
2, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 4
2, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 6
2, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 8
2, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> (0, 1, 2, 3, 4, 5)[:3]
(0, 1, 2)

>>> 'ABCDEFG'[:3]
'ABC'
>>> 'ABCDEFG'[::2]
'ACEG'

list = [1,2,3,4,5]
list[:3]            #输出[1,2,3]
list[0:3]           #输出[1,2,3]
list[-2:]           #输出[4.5]
list[-2:-1]         #输出[4]

可以通过定义来理解。假想一个不存在的下标-0,用正数表示时指0之前的元素，用负数表示时指-1后的一个元素，但他们实际是不存在的。

list[:3] == list[-0:3]：虽然切片list[-0:3]包含-0元素，但其实他不存在，所以与list[0:3]相等。
list[-2:] == list[-2:-0]：切片list[-2:-0]不包含-0元素，他实际也不存在，所以不包含在此处没起作用，list[-2:-1]中的-1是存在的，所以不包含起作用了,故此两者不相等。