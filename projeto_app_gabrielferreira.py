if random # Importamos para gerar a distância aleatória


usuarios = {"aluno": "123"} # Usuário padrão para teste rápido
pedidos_realizados = []

# Cardápio Realista de Açaiteria (2026)
cardapio = [
    {"id": 1, "item": "Copo de Açaí 300ml (3 acompanhamentos)", "preco": 18.00},
    {"id": 2, "item": "Copo de Açaí 500ml (5 acompanhamentos)", "preco": 26.00},
    {"id": 3, "item": "Barca de Açaí 1L (Completa)", "preco": 45.00},
    {"id": 4, "item": "Adicional de Nutella", "preco": 5.50},
    {"id": 5, "item": "Suco de Laranja 500ml", "preco": 10.00}
]

print("========================================")
print("     🍧 BEM-VINDO À AÇAITERIA VIP 🍧     ")
print("========================================")

while True:
    print("\n--- MENU DE ENTRADA ---")
    print("1. Criar Conta (Cadastro)")
    print("2. Entrar (Login)")
    print("3. Fechar Sistema")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- CADASTRO DE NOVO CLIENTE ---")
        novo_usuario = input("Digite o nome de usuário: ")
        nova_senha = input("Digite a senha: ")
        usuarios[novo_usuario] = nova_senha
        print("✅ Conta criada com sucesso! Agora faça o login.")

    elif opcao == "2":
        print("\n--- LOGIN ---")
        user_login = input("Usuário: ")
        senha_login = input("Senha: ")

        # Verificação (Se o usuário existe e a senha bate)
        if user_login in usuarios and usuarios[user_login] == senha_login:
            print(f"\nLogin realizado! Olá, {user_login}.")
            
            while True:
                print("\n--- ÁREA DO CLIENTE ---")
                print("1. Ver Cardápio e Fazer Pedido")
                print("2. Rastrear meu Pedido")
                print("3. Sair da Conta")
                
                escolha_cliente = input("O que deseja fazer? ")

                if escolha_cliente == "1":
                    carrinho = []
                    total_conta = 0
                    
                    print("\n--- CARDÁPIO DE HOJE ---")
                    for p in cardapio:
                        print(f"ID: {p['id']} | {p['item']} | R$ {p['preco']:.2f}")
                    
                    while True:
                        item_id = input("\nDigite o ID do item para comprar (ou 0 para finalizar): ")
                        
                        if item_id == "0":
                            break
                        
                        # Procurando o item no cardápio
                        encontrado = False
                        for p in cardapio:
                            if item_id == str(p['id']):
                                carrinho.append(p['item'])
                                total_conta += p['preco']
                                print(f"✓ {p['item']} adicionado!")
                                encontrado = True
                        
                        if encontrado == False:
                            print("❌ Código não encontrado!")

                    # Finalização do Pedido
                    if total_conta > 0:
                        print(f"\nRESUMO: {carrinho}")
                        print(f"TOTAL A PAGAR: R$ {total_conta:.2f}")
                        confirmar = input("Confirmar pedido? (s/n): ")
                        
                        if confirmar.lower() == "s":
                            # Lógica de distância e tempo (Simulação)
                            distancia = round(random.uniform(1.2, 7.5), 1)
                            tempo_estimado = int(distancia * 8) # Média de 8 min por km
                            
                            novo_pedido = {
                                "cliente": user_login,
                                "itens": carrinho,
                                "valor": total_conta,
                                "distancia": distancia,
                                "tempo": tempo_estimado,
                                "status": "Preparando seu Açaí..."
                            }
                            pedidos_realizados.append(novo_pedido)
                            print("\n🚀 Pedido enviado para a cozinha!")
                    else:
                        print("\nCarrinho vazio. Pedido cancelado.")

                elif escolha_cliente == "2":
                    print("\n--- 🛵 RASTREAMENTO EM TEMPO REAL ---")
                    tem_pedido = False
                    for p in pedidos_realizados:
                        if p['cliente'] == user_login:
                            tem_pedido = True
                            print(f"Status: {p['status']}")
                            print(f"O entregador está a {p['distancia']} km de você.")
                            print(f"Tempo de espera: {p['tempo']} minutos.")
                            print(f"Itens do pedido: {p['itens']}")
                    
                    if not tem_pedido:
                        print("Você não tem pedidos em andamento.")
                    input("\nAperte Enter para voltar...")

                elif escolha_cliente == "3":
                    print("Saindo da conta...")
                    break
        else:
            print("❌ Usuário ou senha incorretos!")

    elif opcao == "3":
        print("Finalizando o programa da Açaiteria. Até mais!")
        break
    else:
        print("Opção inválida, tente novamente.")

  
