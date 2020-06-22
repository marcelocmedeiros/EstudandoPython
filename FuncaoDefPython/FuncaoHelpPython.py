def ajuda(comando):
    help(comando)


comando = ''
while True:
    comando = input('Função ou Biblioteca >')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)