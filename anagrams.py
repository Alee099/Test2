import sympy 

x =sympy.symbols('x')
f = 3*x**3 +5*x**2+  2*x+8
der= sympy.diff(f,x)


# Finding anagrams.....
anagrams =['ate','bat','eat', 'cat','tea','tan','nat','tab']
ang={}
for a in anagrams:
     soo= ''.join(sorted(a))
     if soo not in ang:
         ang[soo]=[]
     ang[soo].append(a)
#print(list(ang.values()))
    
    
#finding anagrams without sorting
liss={}
for word in anagrams:
    tot=0
    for char in word:
        tot=tot +ord(char)
    if tot not in liss:
        liss[tot]=[]
    liss[tot].append(word)
print(list(liss.values()))
    
        
 