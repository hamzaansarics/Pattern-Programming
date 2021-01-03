prmd='*'
spc=''
halfprmd,hlfinvprmd,hhip,fp,ifp='','','','',''
rows=int(input('LENGTH: '))

###########Half Paramid##############

# for i in range(rows):
#     halfprmd+=prmd
#     print(halfprmd)

############Half Inverted Paramid##############
# cont=rows
# for a in range(1,rows+1):
#     cont-=1
#     for b in range(1,cont+2):
#         hlfinvprmd+=prmd+' '
#     print(hlfinvprmd)
#     hlfinvprmd=''

############Half Hollow Inverted Paramid#############

# cont=rows
# for a in range(1,rows+1):
#     cont-=1
#     for b in range(1,cont+2):
#         if a==1:
#             hhip+=prmd+' '
#         elif b==1 and a!=1:
#             hhip+=prmd
#         elif b==cont+1:
#             hhip+=' '+prmd
#         else:
#             hhip+='  '
#     print(hhip)
#     hhip=''

##############Full Paramid################

for p in range(rows):
    spc+=' '
for pr in range(rows+1):
    print(spc+fp)
    fp+=' *'
    spc+='\b'
print('-------------------------------')

##########Inverted Full Paramid###########
ifp=''
cont=rows+2
ass=[]
for m in range(1,rows+1):
    cont-=1
    for r in range(1,cont):
        if m==1:
            ifp+=prmd+' '
        else:
            ifp+=prmd+' '
        
    spc+=' '
    print(spc+ifp)
    ifp=''





