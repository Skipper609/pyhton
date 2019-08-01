import csv

class Stock:

    def __init__(self,Name,Symbol,Exchange,Price):
        self.Name = Name
        self.Symbol = Symbol
        self.Exchange = Exchange
        self.Price = Price
    
    def __str__(self):
        return f"{self.Name} - {self.Symbol} - {self.Exchange} - {self.Price}"
    
def get_info():
    try:
        with open("stock_Price.csv") as f:
            data = csv.DictReader(f, delimiter = ',')
            stock_list = []
            for d in data:
                stock_list.append(Stock(**d))
        for s in stock_list:
            print(s)
    except Exception as e:
        print(e)