def calcular_valor_entrada(idade):
    if idade < 18:
        preco = 15
        tipo_entrada = "meia"
    elif 18 <= idade < 60:
        preco = 30
        tipo_entrada = "inteira"
    else:
        preco = 0
        tipo_entrada = "entrada livre"
    
    return preco, tipo_entrada

def main():
    try:
        idade = int(input("Digite a idade da pessoa: "))
        preco, tipo_entrada = calcular_valor_entrada(idade)
        
        if preco > 0:
            print(f"A entrada é {tipo_entrada}, e o valor a ser pago é R$ {preco:.2f}.")
        else:
            print("A entrada é gratuita para idosos a partir de 60 anos.")
    
    except ValueError:
        print("Por favor, insira uma idade válida (número inteiro).")

if __name__ == "__main__":
    main()
