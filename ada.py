
c=str(input("ENTER YOUR NAME"))
F=open("users.txt","a+")
F.write(c)
print("INSTRUCTIONS")
ins=open("ins.txt",'r')
for line in ins.readlines():
    print(line)
ins.close()
f=open("pydext word game base.txt")
t=[f.readlines()]
s=[]
c=0
l=0
z=1
trials=0
for x in t:
    for m in x:
        if((m[1]!=m[2])&(m[1]!=m[3])&(m[0]!=m[3])&(m[0]!=m[1])&(m[2]!=m[3])&(m[0]!=m[2])):
            s.append(m)
            l+=1
import random
k=random.randint(0,403)
#instructoionmsd
print("ENTER YOUR four letter GUESS")
ut=s[k]
if c!=4:
    while(z==1):
        c=0
        d=0
        u=str(input())
        if((len(u))!=4):
            print("Type properly")
            continue
        else:
            for lk in range(0,4):
                if ((u[lk]in ut)&(u[lk]==ut[lk])):
                    c+=1
                elif((u[lk]in ut)&(u[lk]!=ut[lk])):
                    d+=1
            print(c,"CORRECT")
            print(d,"DISPLACED")
            trials+=1
            if(c==4):
                break
print("Number of trials=",trials)
dict={}
dict[trials]=c

print("U HAVE WON!!!******")
F.close()
m=open("users.txt","r")
print("LIST OF PEOPLE AND SCORE")
for x in m:
    print(x)
m.close()
ASD=input()

