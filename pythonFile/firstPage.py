
aa = ['123','213','222']
bb = ['稍等','实现']

aa.extend(bb)
print(aa)
aa.insert(1,bb[0])
print(aa)
aa.append(bb[1])
print(aa)
aa[2] = '888'
print(aa)
for i in aa :
    print(i)
    if len(aa) == 3:
        break
    else:
        aa.pop()
print(aa)
aa.remove('稍等')
print(aa)
del aa[0]
print(aa)