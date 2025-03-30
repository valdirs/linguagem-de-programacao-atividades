''' 3. Peça ao usuário o valor total das mercadorias compradas. Se for menor que R$500,
não há imposto. Caso contrário, aplique uma taxa de 50% sobre o valor que ultrapassar
os R$500. '''

compras = float(input('Digite o valor total que você comprou no mercadinho do Berg:R$'))
if compras < 500:
    print('Obrigado pela preferência!')
# Se o valor for maior ou igual a 500, aplica o imposto de 50% sobre o valor excedente
else:
    excesso = compras - 500  # Calcula o quanto excede 500
    imposto = excesso * 0.50  # Aplica 50% sobre o excesso
    total_com_imposto = compras + imposto  # Soma o imposto ao valor original

    print(f"Como o valor da compra excedeu ou foi igual a R$500,adicionamos 50% de taxa por cada real que exceder os R$500. Por esse motivo,o valor total da compra com imposto é de R${total_com_imposto:.2f}")