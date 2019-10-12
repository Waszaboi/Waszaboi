dbmuveletek=int(input("db szamok: "))-1
szamok=[]
for valami in range(dbmuveletek+1):
    szamok.append(int(input("szam: ")))
eredmeny=int(input("eredmeny: "))
muveletek=[]
vmuveletek=[]
vszamok=[]
bestmuveletek=[]


def valtoztat(j):
    global vszamok
    global vmuveletek
    # print("len vmuveletek ",len(vmuveletek))
    for y in range(len(vmuveletek)-j):
        if y < len(vmuveletek)-j-1:
            # print("sima")
            # print("y,j: ", y ," + ",j," = ",y+j)
            
            
            vmuveletek[y+j]=vmuveletek[y+j+1]
            vszamok[y+j]=vszamok[y+j+1]
        else:
            # print("else")
            # print("y,j: ", y," + ",j," = ",y+j)
            vszamok[y+j]=vszamok[y+j+1]
            
            
    vszamok.pop()
    vmuveletek.pop()
    # print("vszamok ",vszamok)
    # print("vmuvetek ",vmuveletek)
    # print("valtoztatas vege")
        
        
        

def szamol():
    global vmuveletek
    global vszamok
    global veredmeny
    vmuveletek=muveletek.copy()
    vszamok=szamok.copy()
    # print("vszamok ",vszamok)
    k=0
    
    while k <= len(vmuveletek)-1:
        x = vmuveletek[k]
        if x == 2:
            vszamok[k+1]=vszamok[k]*vszamok[k+1]
            valtoztat(k)
            k=k-1
        elif x == 3:
            vszamok[k+1]=vszamok[k]//vszamok[k+1]
            valtoztat(k)
            k=k-1
        k=k+1
    k=0
    # print("m: ",muveletek)
    while k <= len(vmuveletek)-1:
        x = vmuveletek[k]
        if x==0:
            vszamok[k+1]=vszamok[k]+vszamok[k+1]
            valtoztat(k)
            k=k-1
            # print("m: ",muveletek)
        elif x==1:
             vszamok[k+1]=vszamok[k]-vszamok[k+1]
             valtoztat(k)
             k=k-1
        k=k+1
    return vszamok[0]
    # print("m: ",muveletek)
    # print("szamolas vege")
        

def fordit(szam):
    if szam == 0:
        return ("+")
    elif szam == 1:
        return ("-")
    elif szam == 2:
        return ("*")
    else:
        return ("//")
    
                

def maxl(i):
    lista=[]
    for c in range(i):
        lista.append(3)
    return lista

def check(i):
    global muveletek
    # print("muveletek ",muveletek)
    if muveletek[i] < 3:
       muveletek[i]=muveletek[i]+1
    else:
        muveletek[i]=0
        check(i+1)
    # print("check vege")
        
            
for z in range(dbmuveletek):
    muveletek.append(0)


besteredmeny=szamol()
bestmuveletek=muveletek.copy()

while muveletek != maxl(dbmuveletek):
    check(0)
    # print("check utani m: ",muveletek)
    veredmeny=szamol()
    if abs(eredmeny-besteredmeny) > abs(eredmeny-veredmeny):
        besteredmeny=veredmeny
        bestmuveletek=muveletek.copy()

hely=0
for s in bestmuveletek:
    print(szamok[hely], end="")
    print(fordit(s),end="")
    hely=hely+1
print(szamok[hely],"=",besteredmeny,"≈",eredmeny)
