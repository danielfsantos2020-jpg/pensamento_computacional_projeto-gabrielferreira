'''
CRUD

AÇÃI








'''


print('\n === Sistema de Açãitaria === \n')
print("1. Cadastro no Aplicativo")
print("2. Número de telefone")
print("3.Agendar Pedido")
print("4. Promoções e ofertas")
print("5. Cancelamento")
print("6. Constatar o Suporte")
print("7. Feedback e Avaliações")



while True:

  escolha_menu = input('\n Cadastro no Aplicativo')
if escolha_menu == '1':
 print('Agendamento do Cliente...')
 nome_do_cliente = ipunt("Digite o Nome do Cliente")
 telefone_cliente = input('Digite o Telefone do Cliente')
 #Código para agendar cliente
  
elif escolha_menu == '0':
   


   print('Saindo do Sistema. Até Logo!')


else:
   print('Opção Inválida. Por Favor, Tente Novamente')