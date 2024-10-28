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
        
        
def ElmtKeN(N,L):
    if N == 1:
        return L[0]
    else:
        return ElmtKeN(N-1,tail(L))
    
def isEmpety(L):
    return L == []


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
        konso(firstElmt(L),copy(tail(L)))
        
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