def konso(e,L):
    return [e] + L

def konsi(L,e):
    return L + [e]

def firtElmt(L):
    return L[0]

def lastElmt(L):
    return L[-1]

def tail(L):
    return L[1:]

def head(L):
    return L[:-1]


print(konso(2,[3,4,5]))
print(konsi([3,4,5],6))

list =[1,2,3,4,5,6]

print(firtElmt(list))
print(lastElmt(list))
print(tail(list))
print(head(list))

def isEmpety(L):
    return L == []
   
def IsOneElmt(L):
    if isEmpety(L):
        return False
    else:
        return tail(L) == [] and head(L) == []
    
def MAX2(x,y):
    if x > y:
        return x
    else:
        return y
    
def maxElmt(L):
    if IsOneElmt(L):
        return firtElmt(L)
    else:
        return MAX2(lastElmt(L),maxElmt(head(L)))
        
print(maxElmt([6,5,8,3,9]))