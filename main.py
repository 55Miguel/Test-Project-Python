meme_dict = {
    "F": "respeito",
    "FF": "desistir",
    "GG": "bom jogo",
    "RUSHAR":"ir pra cima",
    "BROKEN":"algo que esta desbalanceado"
}

word = input("digite uma palavra que esta dentro do nosso dicionário e direi oseu significado:")

if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print("esta palavra não conta no nosso dicionário")
