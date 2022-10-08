"""
intalação: pip install spacy
modelo em pt: python -m spacy download pt
Pacote de frases: python -m spacy donwload pt_core_news_sm
              ou: python -m spacy donwload pt_core_news_md
"""
import spacy
nlp = spacy.load('pt_core_news_sm')

doc = nlp('A galinha atravessou a rua para ganhar um milhão.')
word_With_Classe = {}
for token in doc:
    word_With_Classe[token.text] = spacy.explain(token.tag_)

print(word_With_Classe)
