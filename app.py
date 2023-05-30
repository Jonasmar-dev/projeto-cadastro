
resposta = input('[1] Fazer Login\n[2] Cadastrar Usuário\nopção: ')
# armazenar usuarios
usuarios = []
senhas = []
arquivo_usuarios = 'usuarios.txt'
arquivo_senhas = 'senhas.txt'


while True:
    if resposta == '1':
        usuario_digitado = input('Digite seu usuário: ')
        senha_digitada = input('Digite sua senha: ')

        # faz a leitura dos usuarios e senhas existentes
        try:
            with open(arquivo_usuarios, 'r') as usuarios_txt:
                usuarios = usuarios_txt.read().splitlines()

            with open(arquivo_senhas, 'r') as senhas_txt:
                senhas = senhas_txt.read().splitlines()
        except FileNotFoundError:
            pass

        if usuario_digitado in usuarios:
            index_usuario = usuarios.index(usuario_digitado)
            if senha_digitada == senhas[index_usuario]:
                print('Login realizado com sucesso!')
                break
            else:
                print('Senha incorreta.')
        else:
            print('Usuário não encontrado.')

    elif resposta == '2':
        usuario_digitado = input('Digite seu usuário: ')

        # Carregar usuários existentes, se o arquivo existir
        try:
            with open(arquivo_usuarios, 'r') as usuarios_txt:
                usuarios = usuarios_txt.read().splitlines()
        except FileNotFoundError:
            pass

        if usuario_digitado in usuarios:
            print('Este usuário já existe!')
        else:
            senha_digitada = input('Digite sua senha: ')
            print('Cadastro aprovado!')
            usuarios.append(usuario_digitado)
            senhas.append(senha_digitada)

            # Salva o usuario e senha nos arquivos
            with open(arquivo_usuarios, 'a') as usuarios_txt:
                usuarios_txt.write(usuario_digitado + '\n')

            with open(arquivo_senhas, 'a') as senhas_txt:
                senhas_txt.write(senha_digitada + '\n')

            break

    else:
        resposta = input('Opção inválida. Digite novamente: ')
