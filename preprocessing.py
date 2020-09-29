
import nltk
import os
#nltk.download('punkt')
from nltk.stem.snowball import FrenchStemmer
import string
from nltk import word_tokenize
from nltk.stem import SnowballStemmer

fr = SnowballStemmer('french')

dirs = os.listdir("./docs")
for file in dirs:
	if file[0]!="." :
		with open(r"./docs/"+str(file),"r") as f :
			text=f.read()
			text.translate(str.maketrans('', '', string.punctuation))
			stemmer = FrenchStemmer()
			french_stem = [stemmer.stem(word) for word in nltk.word_tokenize(text) if word.isalpha()]
			stemmed_text = ' '.join([stemmer.stem(word) for word in nltk.word_tokenize(text) if word.isalpha() ])
			print(stemmed_text)
			with open(r"stemmed_"+str(file),"w") as f2 :
				f2.write(stemmed_text)
			f2.close()
		f.close()


