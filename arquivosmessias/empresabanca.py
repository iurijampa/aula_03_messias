#Bem vindo ao código

while True:
    print ('Digite uma opção do Menu:')
    print ('1 - Empréstimos')
    print ('2 - Financiamentos')    
    print ('3 - COnsórcios')
    op_menu = int(input('Escolha sua opção:'))
    if op_menu == 1:
        print('Você selecionou empréstimo')
        break
    if op_menu ==2:
        print('Você selecionou financiamento ')
        break
    if op_menu == 3:
        print ('Voce selecionou consorcio')
        break
    elif op_menu >3:
        print('Opção Invalida')
    



