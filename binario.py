converter = int (input ('Digite um numero decimal para converter em binário: '))
#pede o numero
binario = ''
#cria uma string vazia para receber o resultado final do binario

while converter != 0 :
    # da uma condiçao de parada,ou seja,enquanto o resultado for diferente de 0
    if converter % 2 == 1:
        #se o resto da divisao for 1,o codigo recebe o digito 1
        
        binario = binario +"1"
    else:
        #caso contraio,recebe 0
        
        binario = binario + "0"
        
    converter = converter // 2
    #dividira o numero por dois(divisao inteira)enquanto a funçao for executada
    
print (binario[::-1])
#printa a string ao contrario
