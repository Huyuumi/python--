#-*- coding:utf-8 -*-
import sys

def sosuu(i):
	if i==1 or i==0:
		return 0
	x = 2
	while x<i:
		if i%x == 0:
			return 0
		x+=1
	return 1

i = int(sys.argv[1])

if sosuu(i)==1 :
	print i,u"は素数です"
else:
	print i,u"は素数ではありません"
