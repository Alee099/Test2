names = ['ali','usman','ahmad','hassan','umer']
age= {23,35,27,56,21}
group= ('C','A','D','F','B')
#for name , agee, groop in zip(names, age, group):
#   print(f"{name} is {agee} years old and belongs to group {groop}")

#The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into
# a single iterator of tuples.
# Each tuple contains elements from the input iterables that are at the same position.
zipped = list(zip(names,age,group))
print(zipped)
'''
namess , agee, groop = zip(*zipped)
print(names)
print(agee)
print(groop)



ab= [('Usman', 22),('Myself',24),('Sarmad', 26),('Salman', 23), ('Noone', 24)]
name , age = zip(*ab)
print(name)
print(age)'''