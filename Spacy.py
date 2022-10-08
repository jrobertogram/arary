"""
intalação: pip install spacy
pacote de modelo em pt: python -m spacy donwload pt
"""
import spacy

nlp = spacy.blank("pt")
doc = nlp('Todos os gatos são amarelos')

for token in doc:
    print(token.text, token.pos_)