prmd='*'
spc=''
halfprmd,hlfinvprmd,hhip='','',''
rows=int(input('LENGTH: '))
cont=rows
#Half Paramid

# for i in range(rows):
#     halfprmd+=prmd
#     print(halfprmd)

#Half Inverted Paramid

for a in range(1,rows+1):
    cont-=1
    for b in range(1,cont+2):
        hlfinvprmd+=prmd+' '
    print(hlfinvprmd)
    hlfinvprmd=''

#Half Hollow Inverted Paramid
cont=rows
for a in range(1,rows+1):
    cont-=1
    for b in range(1,cont+2):
        if a==1:
            hhip+=prmd+' '
        elif b==1 and a!=1:
            hhip+=prmd
        elif b==cont+1:
            hhip+=' '+prmd
        else:
            hhip+='  '
    print(hhip)
    hhip=''