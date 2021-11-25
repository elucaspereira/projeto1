from time import sleep
from random import randint
print('*'*68)
print('                           LP EVENTOS')
print('*'*68)
print('Bem vindo ao portal da LP Eventos')
print('Neste ambiente você ira adquirir o ingresso do Buteco do Gustavo Lima')
data = ('12/12/2021')
nome = str(input('Digite seu nome completo: ')).strip().title()
cpf = input('Digite seu CPF: ').strip()
cpffor = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]) #esta variavel dara formato para o cpf(000.000.000-00)
print('para escolher o tipo de ingresso digite o seu codigo, sendo: ')
print('Camarote: 1')
print('Vip: 2')
print('Pista: 3')
ingresso = int(input('Qual tipo de ingresso: '))
camarote = 250
vip = 200
pista = 100
if ingresso == 1:
    preço = camarote
    print('o ingreço custa: R${:.2f}'.format(preço))
else:
    if ingresso == 2:
        preço = vip
        print('o ingreço custa: R${:.2f}'.format(preço))
    else:
        if ingresso == 3:
            preço = pista
            print('o ingreço custa: R${:.2f}'.format(preço))
        else:
            ingresso > 3
            print('Nem um ingresso cadastrado neste codigo. Tente novamente.')
print('Realizar pagamento:[0] Sim e [1] Não')
print('O pagamento será realizado com o saldo da conta cadastrada na LP Eventos')
pagamento = int(input('Digite a opção desejada: '))
if pagamento == 0:
    print('AGUARDE ESTAMOS GERENDO O SEU INGRESSO...')
    sleep(3)
    print('-='*32)
    print('Buteco do Gustavo Lima')
    print('ingresso individual')
    print('Nome:{}'.format(nome))
    print('CPF:{}'.format(cpffor))#cpffor retornara o cpf no formato separado por ponto e traço
    print('Valor:{:.2f}'.format(preço))
    print(data)
    print('Apresentar na Portaria')
    cod = randint(1, 1000)
    print('código do bilhete:{}'.format(cod))
    print('-='*32)
else:
    pagamento == 1
    print('Que pena, fica para proxima oportunidade')
print('Obrigado Por utilizar nossa plataforma, tenha um bom dia')


