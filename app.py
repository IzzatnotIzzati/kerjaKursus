import time
from decimal import Decimal, InvalidOperation



print(
    "Calculator to calulate how much time you need to achieve your savings goal"
)

time.sleep(2)

print("\x1b[2J\033[H"
      )  # clear screen and reset cursor position just because i want it to :)

# enter goal amnt

while True:
    goalamt = input("How much would you like to save? \n RM ")
    time.sleep(1)
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

while True:
  income = input("How much do you save per month? \n RM ")
  time.sleep(1)
  try:
      # validate and convert to decimal
      incomeDecimal = Decimal(income)
      if incomeDecimal <= Decimal("0"):
          print("Enter a number greater than 0. \nTip: You can't save if you don't put money aside ")
          continue
      # break the loop if the response is what we expected
      break
  except InvalidOperation:
      print("Enter a valid number! Not text!")
      continue