# Q.Write a python programe to compute the difference betwwen two list
a=[11,12,13,14,15,16]
b=[16,15,14]

def DiffVal(a,b):
    return list(set(a) - set(b))

finalval=DiffVal(a,b)
print(finalval)
