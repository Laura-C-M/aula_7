#perguntar velocidade se for +80km(por cada km acima é 2€ se tiver abaixo estás abaixo do limite boa viagem
velocidade = int(input("A que velocidade estavas a passar?"))
if velocidade <= 80 :
    print("Estás dentro do limite de velocidade. Faz boa viagem!")
elif velocidade > 80 :
    multa = (velocidade-80)*2
    print(f'Estás acima do limite de velocidade. A tua multa é de { multa } euros.')