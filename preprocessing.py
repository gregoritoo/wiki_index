
import nltk
import os
#nltk.download('punkt')
from nltk.stem.snowball import FrenchStemmer
import string
from nltk import word_tokenize
from nltk.stem import SnowballStemmer



def clean_txt_files(directory:str,language="french":str):
	'''
	This function tokenize the files contained in the /docs directory , stemmed them and then change the html format to markdown
	:parameters:
	:input:
		directory : str
		directory conataining the webpages scwralled with the html balises (txt format)
		language : str
		language for nltk tokenizer
	:output:
		none
	'''
	fr = SnowballStemmer('language')

	dirs = os.listdir(directory)
	for file in dirs:
		if file[0]!="." :
			with open(directory+"/"+str(file),"r") as f :
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



if __name__ == '__main__':
	clean_txt_files(directory="./docs")