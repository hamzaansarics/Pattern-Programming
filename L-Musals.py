#Solid Rectangle

data='*'
sm=''
spc=''
row=int(input('ROWS: ' ))
col=int(input('COLS: '))
for i in range(row):
    for i in range(col):
        sm+=data+'  '
    print(sm)
    sm=''

#Hollow Rectangle
print('\n')
data='*'
sm=''
spc=''
for i in range(1,row+1):
    for s in range(1,col+1):
        if i==1 or i==row:
            sm+=data+'  '
        else:
            if s==1:
               sm+=data
            elif s==col:
                sm+='  '+data
            else:
                sm+='   '
    print(sm)
    sm=''
                