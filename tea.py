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