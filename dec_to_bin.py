dec= int(input('Input a decimal number: '))

# What if we were to do it without using built in function , what shall we do?
binar=0
pl=1
while dec>0:
    rem = dec%2
    binar =(rem*pl)+ binar
    dec=dec//2
    pl*=10
print(binar)

