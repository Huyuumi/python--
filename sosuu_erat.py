#coding:utf-8
#エラトステネスの篩
import sys
Num = int(sys.argv[1])
li = range(2,Num+1)

j = 0
z = 2
while j < len(li):
	i=0
	while i < len(li):
		if ((li[i] % z == 0 ) and (li[i] != z)):
			del li[i]
		i += 1
	z += 1
	j += 1

print li
print u"素数の数は",len(li),u"個です"
