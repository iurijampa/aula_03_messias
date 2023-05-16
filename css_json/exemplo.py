import csv

list = ['acabate', 'uva', 'uva', 'kiwi']

with open('exemplo1.csv', 'w' , newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo, delimiter=';')
    writer.writerow(list)
