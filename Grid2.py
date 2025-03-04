
colours = { 1: "green", 2: "red", 3: "blue", 4: "orange", 5: "gray", 6: "green",
           7: "green", 8: "gray", 9: "orange", 10: "blue", 11: "red", 12: "green",
           13: "red", 14: "blue", 15: "orange", 16: "gray", 17: "green", 18: "red",
           19: "red", 20: "green", 21: "gray", 22: "orange", 23: "blue", 24: "red",
            25: "blue", 26: "orange", 27: "gray", 28: "green", 29: "red", 30: "blue",
           31: "blue", 32: "red", 33: "green", 34: "gray", 35: "orange", 36: "blue"}
number=set()
win=0
i=1
Warning=0
while i<=5:
    num1=int(input(f'Enter a number between 1 and 36, Round {i} : '))
    num2=int(input(f'Enter a number between 1 and 36, Round {i} : '))
    if num1 not in colours or num2 not in colours:
        print('Invalid Input! Number greater than 36 or less than 1 are not allowed!')
        continue 
    elif win>=2:
        print('.....You won!.....')
        break
    elif Warning >=3:
        print('Game Terminated!')
        break
    
    if (num1, num2) in number or (num2,num1) in number:
        Warning+=1
        print(f"Warning: {Warning}, Numbers already Enteref ")
    elif colours[num1]== colours[num2]:
        print('Same Colour!')
        win=win+1
        i+=1
    else:
        print('Not the Same Colour!')
        i+=1

    number.add((num1,num2))
if i>=5:
    print('.....You Could not Win!.....')
    
    
        