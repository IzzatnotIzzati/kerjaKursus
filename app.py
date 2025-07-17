import time
from decimal import Decimal, InvalidOperation
import sys

time.sleep(1) # titlescreen ahh

def clearScreen():
    """clear console screen"""
    print("\x1b[2J\033[H", end='') # just because its fancy ig, idk

def pretendLoading(duration):
    """simulate loading by sleeping for a given time just to make it look like the program is thinking lol"""
    
    spinner = ['|', '/', '-', '\\']
    start_time = time.time()
    
    # loop until time runs out
    i = 0
    while time.time() - start_time < duration:
        sys.stdout.write('\b' + spinner[i])  # \b moves cursor back one position
        sys.stdout.flush()
        time.sleep(0.25) # adjust how fast the spinny thing spins so that the spinning looks nice ig
        i = (i + 1) % len(spinner)
    sys.stdout.write('\b ')  # clear the spinner
    print()


print("Calculator to calulate how much time you need to achieve your savings goal")

pretendLoading(2)

clearScreen()

# enter goal amnt

while True:
    goalamt = input("How much would you like to save? \n RM ")
    pretendLoading(1)
    try:
        # validate and convert to decimal
        goalamtDecimal = Decimal(goalamt)
        if goalamtDecimal <= Decimal("0"):
            print("Enter a number greater than 0.")
            continue
        # break the loop if the response is what we expected
        break
    except InvalidOperation:
        print("Enter a valid number! Not text!")
        continue

# enter how much is saved per month

attemptAskingIncome = int(0)

while True:
  income = input("How much do you save per month? \n RM ")
  attemptAskingIncome = int(attemptAskingIncome) + 1
  pretendLoading(1)
  if attemptAskingIncome > 2:
    pretendLoading(2)
    print("You can never reach your goal if you don't save money! Come back later when you pulled your life together! Exiting program...")
    pretendLoading(0.5)
    exit(0)  # ragequit asking
  try:
      # validate and convert to decimal
      incomeDecimal = Decimal(income)
      if incomeDecimal <= Decimal("0"):
          print("Enter a number greater than 0. \nTip: You can't save if you don't put money aside or if you're bleeding money (unless you already earn enough in dividends to live off of)!")
          continue
      # break the loop if the response is what we expected
      break
  except InvalidOperation:
      print("Enter a valid number! Not text!")
      continue # continue the loop if user gives iffy input
  

# see if user earns interest/dividends on their savings

while True:
    hasDividends = input("Do you invest or put your savings in a bank account that earns interest? (y/n) \n")
    pretendLoading(1)
    if hasDividends != "y" and hasDividends != "n":
        print("Please enter 'y' or 'n'.")
        continue
    elif hasDividends == "y":
        hasDividends = True
        break
    else:
        hasDividends = False
        break
