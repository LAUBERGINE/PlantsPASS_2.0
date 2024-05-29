from stockage import genVar, load, save
from hachage import sha512

stock = []
temp_stock = []
load(stock)
master = sha512(input("Password : "))

temp_stock.append(genVar(master))

for i in stock:
    save(i, stock, temp_stock)
    i.view_stockage(master)
