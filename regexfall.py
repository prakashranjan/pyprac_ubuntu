import re
s = 'abaabaabaabaae'
rule = r'[aeoiuAEIOU]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'
x = re.finditer(rule,s)
lst = (list(map(lambda x: x.group(),x)))
if len(lst) == 0:
	print(-1)
elif x:
	for i in lst:
		ln = len(i)-1
		print(i[0:ln])
#-----------------------------------------------------------------------------------------------------------------------------

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))

#my answer-----------------------------------------------------------------------------------------------------------------------
import re

if __name__ == "__main__":
    s = input()
    #print (s)
    z =re.findall("[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][aeiouAEIOU]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]",s)
    #print(z)
    if len(z) == 0:
        print(-1)
    else:
        for i in z:
            zln = len(i)-1
            print(i[1:zln])