import cmath
import math

def complex_calculator():
    print("Calculadora Complexa")
    print("Operações disponíveis:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Exponenciação (^)")
    print("6. Logaritmo (log)")
    print("7. Seno (sin)")
    print("8. Cosseno (cos)")
    print("9. Tangente (tan)")
    print("10. Módulo (|z|)")
    
    while True:
        try:
            escolha = int(input("\nDigite o número da operação que deseja realizar (ou 0 para sair): "))
            
            if escolha == 0:
                print("Saindo da calculadora...")
                break
            
            elif escolha in [1, 2, 3, 4, 5]:  # Operações básicas e exponenciação
                num1 = complex(input("Digite o primeiro número (exemplo: 1+2j): "))
                num2 = complex(input("Digite o segundo número (exemplo: 3+4j): "))
                
                if escolha == 1:
                    resultado = num1 + num2
                elif escolha == 2:
                    resultado = num1 - num2
                elif escolha == 3:
                    resultado = num1 * num2
                elif escolha == 4:
                    resultado = num1 / num2
                elif escolha == 5:
                    resultado = num1 ** num2
                
                print(f"Resultado: {resultado}")
                
            elif escolha == 6:  # Logaritmo
                num = complex(input("Digite um número para calcular o logaritmo: "))
                base = input("Digite a base do logaritmo (pressione Enter para logaritmo natural): ")
                
                if base:
                    base = float(base)
                    resultado = cmath.log(num, base)
                else:
                    resultado = cmath.log(num)
                
                print(f"Resultado: {resultado}")
                
            elif escolha == 7:  # Seno
                num = complex(input("Digite um número para calcular o seno: "))
                resultado = cmath.sin(num)
                print(f"Resultado: {resultado}")
                
            elif escolha == 8:  # Cosseno
                num = complex(input("Digite um número para calcular o cosseno: "))
                resultado = cmath.cos(num)
                print(f"Resultado: {resultado}")
                
            elif escolha == 9:  # Tangente
                num = complex(input("Digite um número para calcular a tangente: "))
                resultado = cmath.tan(num)
                print(f"Resultado: {resultado}")
                
            elif escolha == 10:  # Módulo
                num = complex(input("Digite um número para calcular o módulo: "))
                resultado = abs(num)
                print(f"Resultado: {resultado}")
                
            else:
                print("Operação inválida. Tente novamente.")
                
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

complex_calculator()

