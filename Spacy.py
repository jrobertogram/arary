"""
intalação: pip install spacy
modelo em pt: python -m spacy download pt
Pacote de frases: python -m spacy donwload pt_core_news_sm
              ou: python -m spacy donwload pt_core_news_md
"""
import spacy
nlp = spacy.load('pt_core_news_sm')
class_pt = {'ADJ': 'adjetivo', 'ADP' : 'aposição', 'ADV': 'adverbio', 'AUX': 'auxiliar', 'CCONJ': ['conjunção', 'coordenativa'], 'DET': 'determinante', 'INTJ' : 'interjeição', 'NOUN' : 'substantivo', 'NUM' : 'numeral', 'PART': 'partícula', 'PRON' : 'pronome', 'PROPN' : 'nome próprio', 'PUNCT' : 'pontuação', 'SCONJ' : 'conjunção subordinativa', 'SYM' : 'símbolo', 'VERB' : 'verbo', 'X' : 'outro'}

doc = nlp('A galinha atravessou a rua para ganhar um milhão.') #Coloque o texto aqui

word_With_Class = {}
for token in doc:
    Class = token.tag_
    word_With_Class[token.text] = class_pt[Class]

print(word_With_Class)
