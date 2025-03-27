# encapsulation in OOPS for ATM code
# instance variable 
# encapsulation means the hide the code and the private the code for this runnig 
# it can be assigned the before the self.__pin and self.__balance is are the example  of this 


class Atm():
  def __init__(self):
      
    self.__pin = ''
    self.__balance = 0
    print(id(self))
    
    self.__menu()

  def get_pin(self):
      return self.__pin

  def set__pin(self,new_pin):
      if type(new_pin)==str:
          self__pin=new_pin
          print('pin changed')
      else:
          print('not changed')
  
    

  def __menu(self):
    user_input = input("""
                Hello, how would you like to proceed?
                1. Enter 1 to create pin
                2. Enter 2 to Deposit
                3. Enter 3 to withdraw
                4. Enter 4 to check balance
                5. Enter 5 to exit
                """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.deposit()
    elif user_input == '3':
      self.withdraw()
    elif user_input == '4':
      self.check_balance()
    else:
      print('bye')

  def create_pin(self):
    self.__pin = input('Enter your pin: ')
    print('Pin set successfully')

  def deposit(self):
    temp = input('Enter your pin: ')
    if temp == self.__pin:
      amount = int(input('Enter the amount: '))
      self.__balance = self.__balance + amount
      print('Deposit successful')
    else:
      print('Invalid pin')

  def withdraw(self):
    temp = input('Enter your pin: ')
    if temp == self.__pin:
      amount = int(input('Enter the amount: '))
      if amount < self.__balance:
        self.__balance = self.__balance - amount
        print('Operation successful')
      else:
        print('Insufficient funds')
    else:
      print('Invalid pin')

  def check_balance(self):
    temp = input('Enter your pin: ')
    if temp == self.__pin:  # Corrected 'slef' to 'self'
      print(self.__balance)
    else:
      print('Invalid pin')
