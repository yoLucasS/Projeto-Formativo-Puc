# Nome do Aluno: Lucas Siqueira dos Santos
# Curso: Analise e desenvolvimento de sistemas
# Atividade Somativa 1 de Raciocínio computacional

class Estudantes:
    list_estudantes = {}  # Dicionário para armazenar os estudantes cadastrados

    @staticmethod
    def adicionar_estudantes():
        """
        Método estático para adicionar novos estudantes ao dicionário.
        """
        try:
            id_aluno = int(input('Digite o código do aluno: '))
            # Verifica se o código do aluno já existe no dicionário
            if id_aluno in Estudantes.list_estudantes:
                print('Código já existe')
                Estudantes.adicionar_estudantes()
                return
        except ValueError:
            print('Valor inválido. Por favor, insira um número inteiro para o código do aluno.')
            Estudantes.adicionar_estudantes()
            return  # Interrompe a execução após a chamada recursiva
        nome_aluno = input('Digite o nome do aluno: ').strip()
        cpf_aluno = input('Digite o CPF do aluno: ').strip()
        # Verifica se o nome e o CPF são válidos antes de adicionar ao dicionário
        if nome_aluno and cpf_aluno and not nome_aluno.isdigit():
            Estudantes.list_estudantes[id_aluno] = {'nome': nome_aluno, 'cpf': cpf_aluno}
        else:
            print('Dados inválidos, digite novamente.')
            Estudantes.adicionar_estudantes()
            return

    @staticmethod
    def editar_estudante():
        """
        Método estático para editar informações de um estudante existente.
        """
        try:
            id_aluno = int(input('Digite o código do aluno que deseja editar: '))
        except ValueError:
            print('Valor inválido. Por favor, insira um número inteiro para o código do aluno.')
            Estudantes.editar_estudante()
            return  # Interrompe a execução após a chamada recursiva
        if id_aluno in Estudantes.list_estudantes:
            nome_aluno = input('Digite o novo nome do aluno: ').strip()
            cpf_aluno = input('Digite o novo CPF do aluno: ').strip()
            Estudantes.list_estudantes[id_aluno] = {'nome': nome_aluno, 'cpf': cpf_aluno}
        else:
            print('Código não cadastrado')
            Estudantes.editar_estudante()
            return

    @staticmethod
    def excluir_estudante():
        """
        Método estático para excluir um estudante do dicionário.
        """
        try:
            id_aluno = int(input('Digite o código do aluno que deseja excluir: '))
        except ValueError:
            print('Valor inválido. Por favor, insira um número inteiro para o código do aluno.')
            Estudantes.excluir_estudante()
            return  # Interrompe a execução após a chamada recursiva
        if id_aluno in Estudantes.list_estudantes:
            Estudantes.list_estudantes.pop(id_aluno)
            print('Aluno excluído com sucesso!')
        else:
            print('Código não cadastrado')
            Estudantes.excluir_estudante()
            return

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
            for id_aluno, info_aluno in Estudantes.list_estudantes.items():
                nome = info_aluno['nome']
                cpf = info_aluno['cpf']
                print("")
                print(f"Código: {id_aluno} - Nome: {nome} - CPF: {cpf}")
            print("")


class MainMenu:
    options_management = (" (1) : Adicionar  \n"
                          " (2) : Editar \n"
                          " (3) : Listar \n"
                          " (4) : Deletar \n"
                          " (5) : Voltar \n")

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
                        print('')
                        # Exibe opções de gerenciamento de estudantes
                        print(MainMenu.options_management)
                        try:
                            selected_menu_management = int(input("Digite a opção de menu desejada: "))
                        except ValueError:
                            print('Valor inválido, digite novamente.')
                            continue
                            # Verifica se a entrada está dentro do intervalo de opções
                        if selected_menu_management > 5:
                            continue
                        # Se a opção selecionada for adicionar um aluno (opção 1)
                        if selected_menu_management == 1:
                            Estudantes.adicionar_estudantes()  # Chama função que adiciona aluno no dicionário
                        # Se a opção for 2 chama função para editar estudantes
                        elif selected_menu_management == 2:
                            Estudantes.editar_estudante()  # Chama função para editar estudantes
                        # Se a opção selecionada for listar os estudantes (opção 3)
                        elif selected_menu_management == 3:
                            # Chama o método para listar os estudantes
                            Estudantes.listar_estudantes()
                        # Se a opção for 4, chama função para apagar um estudante
                        elif selected_menu_management == 4:
                            Estudantes.excluir_estudante()
                        # Se a opção selecionada for para voltar ao menu principal (opção 5)
                        elif selected_menu_management == 5:
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
