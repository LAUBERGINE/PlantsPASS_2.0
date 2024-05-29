from stockage import genVar, load
import os

stock = []

load(stock)

stock.append(genVar())

for i in stock:
    i.view_stockage()
    i.save()
