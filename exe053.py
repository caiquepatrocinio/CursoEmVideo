frase = str (input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print('Você digito a frase: {}'.format(junto))
