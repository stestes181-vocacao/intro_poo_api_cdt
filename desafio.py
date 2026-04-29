###**DESAFIO 1:A CALCULADORA DE DIVISÃO (Erros Matemáticos)**

def aula_tratamento_erros():
    print("---Desafio 1:Divisão---")
try:
        numerador = int(input("Digita o numerador: "))
        denominador = int(input("Digita o denominador: "))
        resultado = numerador / denominador
except ValueError:
      print("Erro: Digita apenas números inteiros!")
except ZeroDivisionError:
      print("Erro: Não podes dividir por zero.")
except Exception as erro:
      print(f"Erro inesperado: {erro}")
else:
      print(f"Sucesso ! Resultado : {resultado}")
finally:
      print("---Fim da divisão---")
aula_tratamento_erros()

''' '''
#### **Desafio 2: Telemóvel e Duração (Tratamento o input)**
class Celular:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo
        self.bateria = 100
