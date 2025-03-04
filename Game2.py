import numpy as np

def higher_or_lower():
    num1 = np.random.randint(1,20)
    num2 = np.random.randint(1,20)
    print(f" First number is {num1}")
    HL= input( 'Enter H for Higher or L for Lower: ')
    HL1= HL.upper()
    
    if HL1 not in('H', 'L'):
        print('Invalid Input!\n')
        return None
    else:
        print(f'Second number is {num2}')
    if (HL1 == 'H' and num2 > num1) or (HL1 == 'L' and num2 < num1):
        print('You Won!\n')
    else:
        print('You lost!\n')


def paper_scissors_rock():
    rand_num = np.random.randint(1,3)
    psr= input('Enter P for Paper, S for Scissors and R for Rock:  ')
    psr1= psr.upper()
    
    if psr1 not in ['P','S','R']:
        print('Invalid input. Enter P, S or R only\n')
        return None
    dict1 = {1: 'Paper', 2:'Scissors', 3: 'Rock'}
    user = {'P':1, 'S': 2, "R": 3}.get(psr1)
    
    print(f"Computer chose: {dict1[rand_num]}")
    print(f"You chose: {dict1[user]}")
    
    if user == rand_num:
        print("It's a tie!")
    elif (user == 1 and rand_num == 3) or (user == 2 and rand_num == 1) or (user == 3 and rand_num == 2):
        print(f'You won! {dict1[user]} beats {dict1[rand_num]}\n')
    else:
        print(f"You lost! {dict1[rand_num]} beats {dict1[user]}\n")


def guess_the_numbers():
    rand_num3 = [np.random.randint(0,9) for i in range(3)]
    user= []
    j=1
    while  j <=3:
        
        num = int(input('Enter a number between 0 and 9\n'))
        if num >= 0 and num<10:
            user.append(num)
            j+=1
        else:
            print('Invalid Input')
    
    print(f"Random numbers were: {rand_num3}\n")
    match=0
    for a in rand_num3:
        if a in user:
            match+=1

    if user ==rand_num3:
        print("Three matching in exact order!")
    elif match == 3:
        print('Three matching, but not in order!')
    elif match == 2:
        print("Two numbers matched!")
    elif match == 1:
        print("One number matched!")
    else:
        print('No Number matchedd !')
    
         
while True:
    print("Welcome to Guessing Games!")
    print("1. Play Higher or Lower")
    print("2. Play Paper - Scissors - Rock")
    print("3. Guess the Numbers")
    print("4. Quit")
        
    choice = input("Enter your choice (1 - 4): ")
        
    if choice == '1':
        higher_or_lower()
    elif choice == '2':
        paper_scissors_rock()
    elif choice == '3':
        guess_the_numbers()
    elif choice == '4':
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
