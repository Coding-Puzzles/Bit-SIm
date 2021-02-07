import random
from datetime import date


class Wallet:
    def __init__(self, ticker, current_holdings, value):
        self.ticker = ticker
        self.current_holdings = current_holdings
        self.value = value
        
    
    def data(self):
        return self.ticker + " - " + str(self.current_holdings)


class Getlive:
    def __init__ (self, currency):
        self.currency = currency
    
    def get_price(self):
        if(self.currency == "BTC"):
            return random.randint(30000,50000)
class MyDate:
    def date():
        return date.today()

class Leger:
    def __init__ (self, type, amount, date):
        self.type = type
        self.amount = amount
        self.date = date
    def __str__(self):
        return "type:% s amount:% s date:% s" % (self.type, self.amount, self.date)  
    

wallet = Wallet("BTC", 0, 0)
blockchain = []

def bit_sim(balance, previous_price):
    menu_data = input("Please enter your query " )
    menu_data = menu_data.split(' ')
    int; currency_price = Getlive("BTC").get_price()


    request = menu_data[0]

    if len(menu_data) > 1:
        global params
        params = menu_data[1]
        params = float(params)
    
    if(previous_price != ''):
        currency_price = previous_price

    if(request == "price"):
        print(str(currency_price) + "$")
        bit_sim(balance, currency_price) 
    elif(request == "buy"):
        cost = params * currency_price
        if(cost <= balance):
            print("You bought " + str(params) + " BTC at " + str(currency_price))
            balance = balance - cost
            wallet.current_holdings = wallet.current_holdings + params
            wallet.value = wallet.value + cost
            node = str(Leger("Buy",params, MyDate.date()))
            blockchain.append(node)
            bit_sim(balance, '')
        else:
            print("Incefficent funds try again")
            bit_sim(balance, currency_price) 
    elif(request == "sell"):
        if(wallet.current_holdings != 0 and wallet.current_holdings >= params):
            cash = params * currency_price
            print("You sold " + str(params) + " BTC for " + str(currency_price))
            balance = balance + cash
            wallet.current_holdings = wallet.current_holdings - params
            wallet.value = wallet.value - cash
            node = str(Leger("Sell",params, MyDate.date()))
            blockchain.append(node)
            bit_sim(balance, '')
        else:
            print("You either didn't have any crypto or tried to sell too many coins")
            
    elif(request == "balance"):
        print("your cash balance is " + str(balance))
        print("your crypto balance is " + str(wallet.data()))
        bit_sim(balance, currency_price)
    elif(request == "history"):
        print(blockchain)
        bit_sim(balance, currency_price)
    elif(request == "wait"):
        bit_sim(balance, '')
    elif(request == "exit"):
        print("Thanks for playing")
    
bit_sim(100000, '')


