from ReporEstoque import ReporEstoque

estoque = ReporEstoque()

class escolhaReposicao:
        
        def opcoesMenu():

            while True:

                escolhaServer = int(input("\nO que deseja fazer?\n1.Adicionar um novo item ao estoque\n2.Atualizar quantidade de um item\n3.Excluir item do estoque\n4.Sair\n"))

                if(escolhaServer == 1):

                    itemAdicionado = int( input("Você irá adicionar um novo:\n1.Cachorro\n2.Gato\n3.Pássaro\n4.Produto\n\n"))

                    if(itemAdicionado > 5 or itemAdicionado < 1):
                        print("\nOpção inválida!\n")
                        estoque.listaEstoque.clear()
                        estoque.escolhaReposicao() 
                        return 

                    estoque.adicionarItemEstoque(itemAdicionado)
                    break

                elif(escolhaServer == 2):

                    while True:
                        escolhaReposicao = int(input("Reponha o estoque de um dos seguintes recursos:\n1.Animais\n2.Produtos\n"))

                        if(escolhaReposicao == 1):

                            while True:
                                reposicaoAnimais = int(input("Reponha o estoque de um dos seguintes animais:\n1.Cães\n2.Gatos\n3.Pássaros\n4.Sair\n"))

                                if(reposicaoAnimais == 1):
                                    estoque.reposicaoAnimal("estoqueCaes.csv", 'a')
                                    break
                                elif(reposicaoAnimais == 2):
                                    estoque.reposicaoAnimal("estoqueGatos.csv", 'a')
                                    break
                                elif(reposicaoAnimais == 3):
                                    estoque.reposicaoAnimal("estoquePassaros.csv", 'a')
                                    break
                            break

                        elif(escolhaReposicao == 2):
                            estoque.reposicaoAnimal("estoqueProdutos.csv", 'p')
                            break
                        break

                elif(escolhaServer == 3):

                    while True:
                        
                        excluirItem = int(input("\nEscolha a categoria do item que será excluído:\n1.Cães\n2.Gatos\n3.Pássaros\n4.Produtos\n"))

                        if(excluirItem == 1):
                                estoque.exclusaoItemEstoque("estoqueCaes.csv")
                                break
                        elif(excluirItem == 2):
                            estoque.exclusaoItemEstoque("estoqueGatos.csv")
                            break
                        elif(excluirItem == 3):
                            estoque.exclusaoItemEstoque("estoquePassaros.csv")
                            break
                        elif(excluirItem == 4):
                            estoque.exclusaoItemEstoque("estoqueProdutos.csv")
                            break  
                            
                elif(escolhaServer == 4):
                    break               
