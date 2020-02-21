import bank
print('****************************************')
print('Welcome to your online Financial Liason!')
print('****************************************')
b = bank.Bank()
def main():
 chat_func()

def chat_func():
  user_input = input('Would you like to 1. Do a basic trascation? or 2. Learn more financial literacy? ')
  if user_input == '1':
    atm()
  elif user_input == '2':
    user_input_2 = input('Would you like to 1. learn about budgeting? or 2. learn about credit score?  ')
    if user_input_2 == '1':
      budget_func()
    elif user_input_2 == '2':
      credit_score()
    else:
      print('Try again please.')
      user_input_2 = input('Would you like to 1.learn about budgeting? or 2. learn about credit score? ')
  else:
    print('Try again please.')
    user_input = input('Would you like to 1. Do a basic trascation or 2. Learn more financial literacy')
  chat_func()
def atm ():
  user_balance = int(input('What is your balance: $'))
  b = bank.Bank()
  b.set_balance(user_balance)
  user_deposit = input('Would you like to deposit? ')
  if user_deposit == 'Yes' or user_deposit == 'yes':
    deposit_amount = int(input('How much would you like to deposit: $'))
    print(b.deposit(deposit_amount))
  else:
    print('Okay')
  user_withdrawl = input('Would you like to withdraw? ')
  if user_withdrawl == 'Yes' or user_withdrawl == 'yes':
    withdrawl_amount = int(input('How much would you like to withdraw: $'))
    print(b.withdraw(withdrawl_amount))
  else:
    print('okay') 
  transfer_ans = input('Would you like to do a tansfer? ')
  if transfer_ans == 'Yes' or transfer_ans == 'yes':
    trans_amount = int(input('How much would you like to transfer: $'))
    print(b.set_savings(savings))
  else:
    print('Okay, Have a great day!')

def credit_score():
  print('A credit score is a three digit number that tells companies how likely you are to pay your debt. Students in college usually get their first credit score due applying for their first credit card and student loans.')
  print('Credit scores are used for situations like getting a car, getting an apartment, and taking out a bank loan.')
  print('They update every 30 days but you can use resources like creditkarma.com for an estimate to stay on track. *NOTE: creditkarma.com is an ESTIMATE of your credit score.')
  credit_score = int(input('What is your credit score: '))
  def loan_approval(credit_score):
    if credit_score >= 400 and credit_score < 500:
      print('Very low likelyhood of approval, think about increasing income instead of any loans.')
    elif credit_score >= 500 and credit_score < 600:
      print('Unlikely for loan approval, make more payments on time.')
    elif credit_score >= 600 and credit_score < 700:
      print('You are likely to be approved for a small loan \n save more money first.')
    elif credit_score >= 700 and credit_score < 800:
      print('You are very likely to be approved')
    elif credit_score >= 800:
      print('Your score is great! Keep it up.')
  print(loan_approval(credit_score))

def budget_func():
  print('A budget is a plan to not go over certain amount to spend and/or not going under a certain amount in your bank account.')
  minimum = int(input('Enter a balance you do not want to go under: $'))
  bud_ans = input('Would you like to 1. withdraw money? 2.transfer money? 3. neither')
  if bud_ans == '1':
    withdrawl_amount = int(input('How much would you like to withdraw: $'))
    print(b.withdraw(withdrawl_amount))
  elif bud_ans == '2':
    trans_amount = int(input('How much would you like to transfer: $'))
    print(b.set_savings(savings))
  if minimum >= withdrawl_amount:
    print('WARNING! YOU ARE AT YOUR MINIMUM BALANCE')
  else:
    print('Good job budgeting!')
def Certificate_of_Deposit(cd_amount, years, apr_amount, cd_choice, y=1):
  if cd_choice == 'no':
    return "bye"
  if years == y:
    return cd_amount * apr_amount * y
  interest_earned = (cd_amount * apr_amount * y) + Certificate_of_Deposit(cd_amount, years-1, apr_amount, cd_choice, y)

  return interest_earned

cd_amount = int(input('Enter CD amount: '))
years = int(input('Enter the amount of years: '))
apr_amount = .03
cd_choice = input('would you like to purchase a CD of' + str(cd_amount) + 'for' + str(years) + 'years at '+ str(apr_amount) + 'percent?')
print(Certificate_of_Deposit(cd_amount, years, apr_amount, cd_choice, 1))
main()