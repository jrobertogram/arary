'''import nltk

texto = """A França, na Europa Ocidental, abrange cidades medievais, aldeias alpinas e praias mediterrâneas. Paris, sua capital, é famosa por suas casas de moda, museus de arte clássica, incluindo o Louvre, e monumentos como a Torre Eiffel. O país também é conhecido por seus vinhos e gastronomia sofisticada. Os antigos desenhos rupestres de Lascaux, o teatro romano de Lyon e o vasto Palácio de Versalhes atestam sua rica história."""
words = nltk.word_tokenize(texto)
tagged_words = nltk.pos_tag(words)

word_tags = []

for tw in tagged_words:
    word_tags.append(tw[0] + "_" + tw[1])
                     
tagged_paragraph = ' '.join(word_tags)
print (tagged_words)'''
import pickle
import nltk
text = 'ola mundo'
tagger = pickle.load(open("tagger.pkl"))
portuguese_sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")
sentences = portuguese_sent_tokenizer.tokenize(text)
tags = [tagger.tag(nltk.word_tokenize(sentence)) for sentence in sentences]
'''import nltk

teste = 'Gato de botas. Para todo andar mundo killed have tenho'
frase = nltk.tokenize.sent_tokenize(teste)
token = nltk.word_tokenize(teste)

classes = nltk.pos_tag(token)
print(classes)'''