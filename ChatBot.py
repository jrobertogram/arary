import random

cerebro = [
["oi cara", ["olá, tudo bem?", "oi", "oieeee", "eaeeh"],{"tipoEntrada": "Pesquisa", "tipoSaida": "Aleatorio"}],
["Tudo bem", "Que bom, Eu me chamo Arári, estou aqui para conversar sobre filosia.",{"tipoEntrada": "exato", "tipoSaida": "exato"}],
]

while True:
	frase = input("Escreva aqui: ").lower().strip()
	for neuronio in cerebro:
		entrada = neuronio[0].lower()
		saida   = neuronio[1]
		config  = neuronio[2]
		
		if config["tipoEntrada"] == "exato":
			if frase == entrada:
				if config["tipoSaida"] == "exato":
					print(saida)
		elif config["tipoEntrada"] == "Pesquisa":	
			if frase in entrada:
				if config["tipoSaida"] == "Aleatorio":
					print(saida[random.randint(0, len(saida) -1)])		
	if frase == "0":
		exit()
