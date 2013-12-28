#coding:utf-8
import sys

def uruu(year):
	if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
		print u"閏年です"
	else:
		print u"閏年ではありません"

year = int(sys.argv[1])
uruu(year)
