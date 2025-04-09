##### Creating a Class
# __init__() is a constructor 
# Code inside a constrtucotor is executed everytime we create an object of the class.
class Atm:
    __counter=0   # A static or class variable
    def __init__(self):   # A constructor , used to initilize an object when it is created.
        self.__pin= ''            # Instance variables
        self.__balance = 0         # Private instance variables
        self.sno=Atm.__counter
        Atm.__counter = Atm.__counter+1

        #self.menu()

    def get_pin(self):           # Getter Function
        return self.__pin

    def set_pin(self,new_pin):         # Setter function
        if type(new_pin) ==str:
            self.__pin =new_pin
            print('Pin changed')
        else:
            print('Invalid input')
            
    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new)==int:
            Atm.__counter= new
        else:
            print('Invalid Input')
        
    
        
    def menu(self):
        while True:
            user_input=input(""" 
                            Hello, How would you like to procees
                            1. Enter 1 to create pin
                            2. Enter 2 to deposit cash
                            3. Enter 3 to withdraw
                            4. Enter 4 to check Blanace
                            5. Enter 5 to Exit 
                            """)
                                               
            if user_input =='1':
                self.create_pin()
            elif user_input =='2':
                self.cash_deposit()
            elif user_input== '3':
                self.withdraw()
            elif user_input =='4':
                self.check_balance()
            else:
                print('Good Bye')
                break

    def create_pin(self):    # A method should get self as input
        self.__pin = input('Enter a 4 digit pin')
        print('pin Set successfully')


    def cash_deposit(self):
        temp = input('Enter your atm pin')
        if temp ==self.__pin:
            self.__balance += int(input('Enter amount to deposit: '))
            print('Cash Deposited successfully')
        else:
            print('Invalid Pin')

    def withdraw(self):
        temp = input('Enter your atm pin')
        if temp == self.__pin:
            amount= int(input('Enter amount to withdraw: '))
            if amount <= self.__balance:
                self.__balance-= amount
                print('Cash Withdrawal successfuly')
            else:
                print('Not enough amount in account') 
        else:
            print('Invalid pin')
    
            

    def check_balance(self):
        temp = input('Enter your atm pin')
        if temp ==self.__pin:
            print(f'Your Current Balance is: {self.__balance}')
        else:
            print('Invalid pin')
        
                    

        