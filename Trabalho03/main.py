import sys

from ri import *

def init():
  if len(sys.argv) < 3:
    print("Por favor, a forma correta de executar este arquivo é:")
    print("python3 main.py base.txt consulta.txt")
    exit()

def iniciarValores(values, str):
  while True:
    try:
        ref = float(input("Informe a porcentagem para "+str+": "))
        if not 0 <= ref <= 1 and ref != -1:
            raise ValueError("Insira valores entre 0 e 1, ou -1 caso deseje utilizar os valores padrões")
        elif ref != -1:
          values[str] = ref
    except ValueError as e:
        print("Valor inválido:", e)
    else:
        break

if __name__ == '__main__':
  init()

  if len(sys.argv) == 3 or '-v' in sys.argv:
    vetorial(sys)
  elif '-vm' in sys.argv:
    values = {"referencia":0.015, "titulo":0.015, 'abstract':0.015, 'majorSub': 0.015, 'minorSub':0.015}
    print("Você escolheu a opção do vetorial modificado!")
    flag = input("Gostaria de alterar alguns valores para testar novas configurações do modelo!? (1->Sim; 0->Não): ")
    if flag == '1':
      print("Ok, Vamos alterar alguns valores.")
      print("Lembrando que os valores inseridos devem estar entre 0 e 1")
      print("Caso queira utilizar os valores padroes estipulados pelos alunos, digite -1")
      
      for i in values:
        iniciarValores(values, i)

    modificado(sys, values)