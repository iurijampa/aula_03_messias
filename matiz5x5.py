matriz5x5 = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]

#imprimindo apenas um numero especifico da lista
for i in matriz5x5:
    for item in i:
        if (item % 2) == 0:
            print(f'Esse numero é par:{item}')
        elif item == 5:
            print (f'Esse numero é o cinco: {item}')
        elif (item %2) != 0:
            print (f'Esse nummero não é cinco e é impar: {item}')
            
            
