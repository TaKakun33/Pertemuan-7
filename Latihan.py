def konso(e,L):
    return [e] + L

def konsi(L,e):
    return L + [e]

def firstElmt(L):
    return L[0]

def lastElmt(L):
    return L[-1]

def tail(L):
    return L[1:]

def head(L):
    return L[:-1]\
        
        
def isEmpety(L):
    return L == []
        
def IsOneElmt(L):
    if isEmpety(L):
        return False
    else:
        return tail(L) == [] and head(L) == []
        
def NbElmt(L):
    if isEmpety(L):
        return 0
    else:
        return 1 + NbElmt(tail(L))
            
def ElmtKeN(n,L):
    if n == 1:
        return L[0]
    else:
        return ElmtKeN(n-1,tail(L))

def isMember(x,L):
    if isEmpety(L):
        return False
    else:
        if firstElmt(L) == x:
            return True
        else:
            return isMember(x,tail(L))
        
def copy(L):
    if isEmpety(L):
        return []
    else:
        return konso(firstElmt(L),copy(tail(L)))
        
def inverse(L):
    if isEmpety(L):
        return []
    else:
        return konsi(inverse(tail(L)), firstElmt(L))
    
def konkat(L1,L2):
    if isEmpety(L2):
        return L1
    else:
        return konsi(konkat(L1,tail(L2)),firstElmt(L2))
    
def SumElmt(L):
    if isEmpety(L):
        return 0
    else:
        return firstElmt(L) + SumElmt(tail(L))
    
def AvgElmt(L):
    if isEmpety(L):
        return 0
    else:
        return SumElmt(L) / NbElmt(L)
    
def addList(L1,L2):
    if isEmpety(L1) and isEmpety(L2):
        return []
    elif isEmpety(L1) and not isEmpety(L2):
        return L2
    elif not isEmpety(L1) and isEmpety(L2):
        return L1
    else:
        return konso(firstElmt(L1) + firstElmt(L2), addList(tail(L1),tail(L2)))
    
def MaxElmt(L):
    if IsOneElmt(L):
        return firstElmt(L)
    else:
        if firstElmt(L) <= firstElmt(tail(L)):
            return MaxElmt(tail(L))
        else:
            return MaxElmt(konso(firstElmt(L),tail(tail(L))))

def NbOcc(x,L):
    if IsOneElmt(L):
        if x == firstElmt(L):
            return 1
        else:
            return 0
    else:
        if x == firstElmt(L):
            return 1 + NbOcc(x,tail(L))
        else:
            return  NbOcc(x,tail(L))

def NbMax(L):
    return [MaxElmt(L),NbOcc(MaxElmt(L),L)]
    
# Aplikasi
print(isEmpety([]))
print(IsOneElmt([2]))
print(ElmtKeN(3,[4,5,6,7,8,9,0]))
print(isMember(2,[4,5,6,7,8,9,0]))
print(copy([4,5,6,7,8,9,0]))
print(inverse([4,5,6,7,8,9,0]))
print(konkat([1,2,3],[9,8,7]))
print(SumElmt([1,2,3,5,6]))
print(AvgElmt([1,2,3]))
print(addList([1,2,3,10],[4,7,6]))
print(MaxElmt([1,1,1,1]))
print(NbOcc(2,[2,2,2,8,3]))
print(NbMax([2,8,2,8,9]))