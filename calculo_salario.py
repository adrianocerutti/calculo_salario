#Exibe uma mensagem na tela
print("Cálculo de salário em um mês")
#Recupera o valor por hora e armazena em uma variável
valor_hora = float(input("Digite o valor por hora: "))
#Recupera o numero de horas e armazena em uma variável
numero_horas = int(input("Digite o número de horas trabalhadas: "))
#Realiza o cálculo e armazena em uma variável
salario = valor_hora * numero_horas
#Exibe o resultado na tela
print("Seu salário este mês foi R$",salario)
