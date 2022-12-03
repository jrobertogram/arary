#import spacy

# Luckas
def palavras4Texto(texto, palavras):
  texto = texto.split()
  for plv1 in palavras:
    if plv1 not in texto:
      return False
  return True
	
#print(palavras4Texto("como surgiu a filosofia na Grécia", ['surgiu', 'filosofia']))

# Emerson
def contarRepetiçõesPalavras(texto):
  lista = texto.split()
  repeticao = []
  for n in lista:
      repeticao.append(lista.count(n))
  return list(zip(lista, repeticao))

#print(contarRepetiçõesPalavras('Meu nome é Benedito, qual é o seu Nome cara?'))

# Rodrigo
string = "como surgiu a filosofia na Grécia antiga" 
lista = [['nasceu',"oie", 'nascimento'], ['Grécia', 'Roma'], ["filosofia", 'matematica']]
quantidade = 1

def listaPalavras4Texto(lista, quan):
  l = []
  for c in range(len(lista)):
    cont = 0
    for i in lista[c]:
      if i in string:
        cont += 1
    if cont != quan:
      l.append('false')
    else:
      l.append('true')
  if 'false' in l:
    return False 
  return True

#listaPalavras4Texto(lista,quantidade)

#Roberto
texto = "como surgiu a matematica na Holanda" 
palavras = ['nasceu',"surgiu", 'filosofia', "matematica"]
quantidade = 2

def palavrasQuantidade4Texto(texto, palavras, quantidade):
  texto = texto.split()
  cont = 0
  for plv1 in palavras:
    if plv1 in texto:
      cont += 1
    if cont == quantidade:
     return True
  return False

#print(palavrasQuantidade4Texto(texto, palavras, quantidade))