
import nltk
import os
#nltk.download('punkt')
import sys
from nltk.stem.snowball import FrenchStemmer
import string
from nltk import word_tokenize
from nltk.stem import SnowballStemmer

def progressbar(it, prefix="", size=60, file=sys.stdout):
	'''
	Show docs cleaning progress
	:parameters:
	:inputs:
		it: str
		number of elements to treat
		prefix : str
		message to show 
	'''
	count = len(it)
	def show(j):
	    x = int(size * j / count)
	    file.write("%s[%s%s] %i/%i\r" % (prefix, "#" * x, "." * (size - x), j, count))
	    file.flush()

	show(0)
	for i, item in enumerate(it):
	    yield item
	    show(i + 1)
	file.write("\n")
	file.flush()


def clean_txt_files(directory:str,language="french",output_directory="clean_docs"):
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
	fr = SnowballStemmer(language)

	dirs = os.listdir(directory)
	for i in progressbar(range(len(dirs)), "Computing: ", 40):
		file=dirs[i]
		if file[0]!="." :
			with open(directory+"/"+str(file),"r") as f :
				text=f.read()
				text.translate(str.maketrans('', '', string.punctuation))
				stemmer = FrenchStemmer()
				#french_stem = [stemmer.stem(word) for word in nltk.word_tokenize(text,language=language) if word.isalpha()]
				stemmed_text = ' '.join([stemmer.stem(word) for word in nltk.word_tokenize(text,language=language) if word.isalpha() ])
				#print(stemmed_text)
				with open(output_directory+"/stemmed_"+str(file),"w") as f2 :
					f2.write(stemmed_text)
				f2.close()
			f.close()



if __name__ == '__main__':
	clean_txt_files(directory="./docs")