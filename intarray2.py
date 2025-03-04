
number_of_elements = int(input('Enter number of elements:'))
if number_of_elements<2:
    print('Atleast 2 numbers are requried to form a pair')
    quit()
    
elements =[]
for i in  range( number_of_elements):
    num=int(input(f'Enter element number  {i+1}: '))
    elements.append(num)

print(elements,'\n')
elements.sort()
maxx ,min = max(elements),min(elements)
print(f'The pair with maximum difference is {maxx, min} and the difference is {maxx-min}')

min_diff= elements[1]-elements[0]
min_pair=elements[0], elements[1]

for i in range(number_of_elements-1):
   
    diff = elements[i+1]-elements[i]
    if diff<min_diff:
        min_diff=diff
        min_pair=elements[i],elements[i+1]
        
print(f'The pair with minimum difference is {min_pair}, and the difference is {min_diff}')
