# Nome do Aluno: Lucas Siqueira dos Santos
# Curso: Analise e desenvolvimento de sistemas
# Atividade Somativa 1 de Raciocinio computacional

class Estudantes:
    list_estudantes = []  # Lista para armazenar os nomes dos estudantes

    @staticmethod
    def listar_estudantes():
        """
        Método estático para listar os estudantes cadastrados.
        """
        if not Estudantes.list_estudantes:
            print("Não há estudantes cadastrados")
        else:
            print("")
            print("Alunos cadastrados: ")
            count = 0
            for aluno in Estudantes.list_estudantes:  # for para listar os alunos cadastrados
                count += +1
                print("")
                print(f"{count} - {aluno}")
            print("")


class MainMenu:
    options_management = (" (1) : Adicionar  \n"
                          " (2) : Editar \n"
                          " (3) : Listar \n"
                          " (4) : Deletar \n"
                          " (5) : Voltar \n")

    # @staticmethod
    # def validar_input(texto):
    #     """
    #     Método estático para validar a entrada de texto.
    #     """
    #     texto = ' '.join(texto.split())
    #     return texto

    @staticmethod
    def set_menu(option):
        """
        Método estático para retornar uma mensagem com base na opção selecionada.
        """
        option = int(option)
        match option:
            case 1:
                return "Você está na tela de gerenciamento de Estudantes"
            case 2:
                return "Em desenvolvimento"
            case 3:
                return "Em desenvolvimento"
            case 4:
                return "Em desenvolvimento"
            case 5:
                return "Em desenvolvimento"
            case 6:
                return "Sair"

    @staticmethod
    def get_main_menu():
        """
        Método estático para exibir o menu principal e processar as opções selecionadas.
        """
        main_menu_layout = ("--------------------- MENU PRINCIPAL ---------------------\n"
                            " (1) : Gerenciar Estudantes  \n"
                            " (2) : Gerenciar Professores \n"
                            " (3) : Gerenciar Disciplinas \n"
                            " (4) : Gerenciar Turmas \n"
                            " (5) : Gerenciar Matrículas \n"
                            " (6) : Sair")

        # Loop para manter o menu principal em execução até que o usuário opte por sair
        while True:
            print(main_menu_layout)
            selected_menu = input("Digite a opção de menu desejada: ")
            # Verifica se a entrada é um número e se está dentro do intervalo de opções
            if selected_menu.isdigit() and int(selected_menu) < 7:
                # Verifica se a opção selecionada é para sair
                if int(selected_menu) == 6:
                    break
                # Se a opção selecionada for para gerenciar estudantes (opção 1)
                elif int(selected_menu) == 1:
                    while True:
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        # Exibe mensagem relacionada à opção selecionada
                        print(MainMenu.set_menu(selected_menu))
                        # Exibe opções de gerenciamento de estudantes
                        print(MainMenu.options_management)
                        selected_menu_management = input("Digite a opção de menu desejada: ")
                        # Verifica se a entrada é um número e se está dentro do intervalo de opções
                        if not selected_menu_management.isdigit() or int(selected_menu_management) > 5:
                            continue
                        # Se a opção selecionada for adicionar um aluno (opção 1)
                        if int(selected_menu_management) == 1:
                            # Solicita o nome do aluno ao usuário
                            nome_aluno = input('Digite o nome do aluno: ').strip()
                            if nome_aluno:
                                # Adiciona o nome do aluno à lista de estudantes
                                Estudantes.list_estudantes.append(nome_aluno)
                        # Se a opção selecionada for listar os estudantes (opção 3)
                        elif int(selected_menu_management) == 3:
                            # Chama o método para listar os estudantes
                            Estudantes.listar_estudantes()
                        # Se a opção selecionada for para voltar ao menu principal (opção 5)
                        elif int(selected_menu_management) == 5:
                            # Para o 2 while e volta para o menu principal
                            break
                        else:
                            # Mensagem temporária para opções ainda não implementadas
                            print("Em desenvolvimento")
                else:
                    # Mensagem temporária para opções ainda não implementadas
                    print("Em desenvolvimento")
                    # Exibe o menu principal novamente
            else:
                # Mensagem de erro para entrada inválida
                print("Caractere inválido")


# Inicializa o menu principal
MainMenu.get_main_menu()
