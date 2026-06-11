'''def validar_cpf(cpf):
 
    cpf = ''.join(filter(str.isdigit, cpf))

  
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False


    def calcular_digito(cpf_parcial, peso_inicial):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(peso_inicial, 1, -1)))
        digito = 11 - (soma % 11)
        return str(digito if digito < 10 else 0)


    primeiro_digito = calcular_digito(cpf[:9], 10)
    if primeiro_digito != cpf[9]:
        return False

 
    segundo_digito = calcular_digito(cpf[:10], 11)
    if segundo_digito != cpf[10]:
        return False

    return True'''
    
    # Exemplo de uso de idade
'''idade = int(input("Digite sua idade: "))
if (idade>0 and idade<120):
        print("Idade válida.")
else:
        print("Idade inválida.")'''
#data e hora
from datetime import datetime
agora = datetime.now()
print(f"Data e hora atual: {agora}")
data = agora.date()
print(f"Data atual: {data}")
hora = agora.time()
print(f"Hora atual: {hora}")
data_formatada = agora.strftime("%d/%m/%Y")
print(f"Data formatada: {data_formatada}")