num = int(input('Enter a number to be checked :'))
div=[]
i=1
while i <num:
    if num%i==0:
        div.append(i)
    i+=1


if sum(div)==num:
    print(num,'Number is  a perfect Number !')
else:
    print('Number is not a perfect number')
    