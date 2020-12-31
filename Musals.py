data='*'
spc=''
n=int(input('Enter Length: '))
print()
for i in range(n):
    spc+=' '
for s in range(n):
#     print(len(spc))
    print(data)
    spc+='\b'
    data+='*'
