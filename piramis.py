input()

moves = list(input())

for x in range(len(moves)//2):
    moves.remove(" ")

pos=[0,1]

for x in moves:
    if x=="0":
        pos[0]+=1
        pos[1]=pos[1]*2-1
    elif x=="1":
        pos[0]+=1
        pos[1]=pos[1]*2
    elif x=="2":
        pos[0]-=1
        pos[1]=(pos[1]+1)//2
    elif x=="3":
        pos[1]-=1
    else:
        pos[1]+=1

# print(pos)

rovid=[]
xmin=1
xmax=2**pos[0]

for x in range(pos[0]):
    if pos[1] > (xmin+xmax)/2:
        rovid.append(1)
        xmin=((xmin+xmax)/2)+0.5
    else:
        rovid.append(0)
        xmax=((xmin+xmax)/2)-0.5

for x in rovid:
    print (x," ", end = "") 
        
