from stockage import genVar, load
from hachage import sha512

stock = []

load(stock)

master = sha512(input("Password : "))

stock.append(genVar(master))

for i in stock:
    i.save()
    i.view_stockage(master)
