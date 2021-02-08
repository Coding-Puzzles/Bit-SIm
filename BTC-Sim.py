# Ethan Hopkins

import random
from datetime import datetime
import pytz

class Wallet:
  def __init__(self, ticker, coinCount):
    self.ticker = ticker
    self.coinCount = coinCount

  def checkAmount(self):
    print(self.ticker + str(self.coinCount))

class Ledger:
  def __init__(self, history):
    self.history = history
  
  def printHistory(self):
    print("Account history:", self.history)

class MyDate:
  def date():
    return datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%B %d, %Y at %I:%M %p")

class GetLive: 
  def fluctuations():
    return random.randint(10000,12000)

bal = 20000
bitcoinCount = Wallet("BTC", 0)
bitcoinVal = GetLive.fluctuations()
record = Ledger([])
def BitcoinSimulator():
  choice = int(input("Choose an option — \n\n1) Check Current Bitcoin Value\n2) Purchase Bitcoin\n3) Sell Bitcoin\n4) View User Portfolio\n5) View Transaction History\n\nEnter choice: "))

  def check(): 
    global bitcoinVal
    print("\nCurrent value of " + bitcoinCount.ticker + ": $" + str(bitcoinVal) + "\n")
    BitcoinSimulator()

  def buy(): 
    global bitcoinVal
    global bal
    global record
    bitcoinVal = GetLive.fluctuations()
    purchased = float(input("How many Bitcoins would you like to purchase? "))
    if (bal >= (bitcoinVal * purchased)): 
      bitcoinCount.coinCount += purchased
      bal -= (bitcoinVal * purchased)
      print("\n" + MyDate.date() + ": Purchased " + str(purchased) + " " + bitcoinCount.ticker + " for $" + str(bitcoinVal * purchased) + ".\n")
      record.history.append(MyDate.date() + ": Purchased " + str(purchased) + " " + bitcoinCount.ticker + " for $" + str(bitcoinVal * purchased) + ".")

    else: 
      print("\nError: Not enough funds to purchase " + str(purchased) + " " + bitcoinCount.ticker + ".\n")
    BitcoinSimulator()
  def sell(): 
    global bitcoinVal
    global bal
    global record
    bitcoinVal = GetLive.fluctuations()
    sold = float(input("How many Bitcoins would you like to sell? "))
    if (bitcoinCount.coinCount >= sold):
      bal += (sold * bitcoinVal)
      bitcoinCount.coinCount -= sold
      print("\n" + MyDate.date() + ": Sold " + str(sold) + " " + bitcoinCount.ticker + " for $" + str(bitcoinVal * sold) + ".\n")
      record.history.append(MyDate.date() + ": Sold " + str(sold) + " " + bitcoinCount.ticker + " for $" + str(bitcoinVal * sold) + ".")
    else:
      print("\nError: Your account has a total of " + str(bitcoinCount.coinCount) + " " + bitcoinCount.ticker + ", which is not enough to sell " + str(sold) + " " + bitcoinCount.ticker + ".\n")
    BitcoinSimulator()

  def bal():
    global bal
    print("\nYour portfolio: \n\n" + str(bal) + " USD\n" + str(bitcoinCount.coinCount) + " " + bitcoinCount.ticker + "\n")
    BitcoinSimulator()

  def history(): 
    print("\nYour transaction history:\n")
    if (len(record.history) > 0):
      for recorded in record.history: 
        print(recorded)
    else:
      print("You do not have any transaction history.")
    BitcoinSimulator()


  if (choice == 1): 
    check()
  
  elif (choice == 2):
    buy()
  
  elif (choice == 3):
    sell()

  elif (choice == 4):
    bal()

  elif (choice == 5):
    history()
    

BitcoinSimulator()