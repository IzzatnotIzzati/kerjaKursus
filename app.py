import time, sys
from decimal import Decimal, InvalidOperation

# Set console mode to allow ANSI escape sequences on Windows because bruh why doesn't it work by default :(
try: 
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
except:
    pass # run without crashing if it's not windows, prob should work out of the box on *nix

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

# get user's interest rate/dividend (annual)
if hasDividends:
    while True:
        appreciationRate = input("What is your annual interest rate/dividend percentage? (in %) \n")
        print('\033[F' + '\r' + appreciationRate + "% p.a.\n")  # Move up one line with \033[F then overwrite, didn't know it was this hard ngl, like ANSI codes are so weird
        pretendLoading(1)
        try:
            # validate and convert to decimal
            appreciationRateDecimal = Decimal(appreciationRate) / Decimal("100")  # convert percentage to decimal
            if appreciationRateDecimal < Decimal("0") or appreciationRateDecimal == Decimal("0"):
                print("Enter a number greater than 0.")
                continue
            break
        except InvalidOperation:
            print("Enter a valid number! Not text!")
            continue

# see how many times it compounds annually
if hasDividends:
    while True:
        compoundingFrequency = input("How many times does it compound annually? (e.g. 12 for monthly, 4 for quarterly, 1 for annually\n")
        pretendLoading(1)
        try:
            # validate and convert to integer
            compoundingFrequencyInt = int(compoundingFrequency)
            if compoundingFrequencyInt < 0:
                print("Enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Enter a valid number! Not text!")
            continue

# Output how muh time needed to reach goal
monthsToGoal = None
yearsToGoal = None
monthsToGoalWithoutYear = None

def printTimeToGoal():
    """Procedure to print how long it'll take to reach the goal. Error alarms are blaring because of a variable issue and this is a very jank non-modular way of doing it but it works ig"""
    if monthsToGoal >= Decimal(12):
        if monthsToGoalWithoutYear > Decimal(0):
            if yearsToGoal == Decimal(1): # see if it's 1 year or more
                print(f"It will take you about {int(yearsToGoal)} year and {int(monthsToGoalWithoutYear)} months to reach your goal of RM {goalamtDecimal:.2f} by saving RM {incomeDecimal:.2f} per month.")
            else:
                print(f"It will take you about {int(yearsToGoal)} years and {int(monthsToGoalWithoutYear)} months to reach your goal of RM {goalamtDecimal:.2f} by saving RM {incomeDecimal:.2f} per month.")
        else:
            if yearsToGoal == Decimal(1):
                print(f"It will take you about {int(yearsToGoal)} year to reach your goal of RM {goalamtDecimal:.2f} by saving RM {incomeDecimal:.2f} per month.")
            else:
                print(f"It will take you about {int(yearsToGoal)} years to reach your goal of RM {goalamtDecimal:.2f} by saving RM {incomeDecimal:.2f} per month.")
    else:
        if monthsToGoal == Decimal(1):
            print(f"It will take you about {int(monthsToGoal)} month to reach your goal of RM {goalamtDecimal:.2f} by saving RM {incomeDecimal:.2f} per month.")
        else:
            print(f"It will take you about {int(monthsToGoal)} months to reach your goal of RM {goalamtDecimal:.2f} by saving RM {incomeDecimal:.2f} per month.")

# calculate how long it will take to reach the goal

#### doesnt have dividends

## formula is t = goalamt / income (result will be in months)

if not hasDividends:
    monthsToGoal = Decimal(goalamtDecimal) / Decimal(incomeDecimal)
    yearsToGoal = Decimal(monthsToGoal) / Decimal("12")
    monthsToGoalWithoutYear = monthsToGoal % Decimal(12)
    pretendLoading(1)
    printTimeToGoal() # c'est tres jank et amusant, mdrrrrr :D
    
### has dividends, with compounding



# debug values
#print("Goal amount:", goalamtDecimal)
#print("Monthly savings:", incomeDecimal)
#print("Has dividends:", hasDividends)
#print("Interest/dividend rate:", appreciationRateDecimal if hasDividends else "N/A")
#print(yearsToGoal)
#print(f"monthsToGoal: {monthsToGoal}")
#print(f"monthsToGoal: {monthsToGoal}")
#print(f"yearsToGoal: {yearsToGoal}")
#print(f"monthsToGoalWithoutYear: {monthsToGoalWithoutYear}")

