class Bank:
  def __init__(self):
    self.__b = 0
    self.__s = 0
  def set_balance(self, b):
    self.__b = b
  def withdraw(self, w):
    self.__b -= w
    print('Your new balance is: $')
    return self.__b
  def deposit(self, d):
    self.__b += d
    print('Your new balance is: $')
    return self.__b
  def get_balance(self):
    return self.__b
  def set_savings(self, s):
    self.__b -= s
    print('Your savings balance is: $')
    return self.__s
  def get_savings(self):
    return self.__s
