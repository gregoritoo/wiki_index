import numpy as np 
import pandas as pd
import os 
import pickle
import matplotlib.pyplot as plt 
import sys
np.set_printoptions(threshold=sys.maxsize)
from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop
from spacy.lang.en.stop_words import STOP_WORDS as en_stop
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

final_stopwords_list = list(fr_stop) + list(en_stop)
vec_of_tokens=[]
vec_of_docs={}
count_doc={}
doctok=[]
dirs = os.listdir("./clean_docs")
i=0
for file in dirs:
	if i < 2 :
		i=i+1
		count=0
		count_doc={}
		if file[0]!="." :
			with open(r"./clean_docs/"+str(file),"r") as f :
				text=f.read()
				text=text.split(" ")
				for tok in text : 
					#print("token",tok)
					if not tok in vec_of_tokens :
						vec_of_tokens = vec_of_tokens +[tok]
						count_doc.update({tok:1})
					else :
						try :
							count_doc[tok]=count_doc[tok]+1
						except Exception as e :
							count_doc.update({tok:1})
				for element in count_doc:
					count_doc[element]=count_doc[element]/len(vec_of_tokens)
				doctok=doctok+[count_doc]
				print("end creation matrix")

with open("vec_of_tokens.txt", "wb") as fp:   #Pickling
	pickle.dump(vec_of_tokens, fp)

with open("doctok_matrix.txt", "wb") as fp:   #Pickling
	pickle.dump(doctok, fp)

with open("doctok_matrix.txt", "rb") as fp:   
	doctok_matrix = pickle.load(fp)

with open("vec_of_tokens.txt", "rb") as fp:   
	 vec_of_tokens= pickle.load(fp)

print(len(vec_of_tokens))
nb_files=len(os.listdir("./clean_docs"))
nb_tokens=len(vec_of_tokens)

maxtokdoc=np.zeros((nb_files,nb_tokens))
for i in range(len(doctok_matrix)) :
	for j in range(len(vec_of_tokens)) :
		if vec_of_tokens[j] in doctok_matrix[i].keys():
			maxtokdoc[i,j]=1

		else :
			continue

with open("maxtokdoc.txt", "wb") as fp:   #Pickling
	pickle.dump(maxtokdoc, fp)

info=np.zeros((1,nb_tokens))

for j in range(nb_tokens):
	#print(np.sum(maxtokdoc[:,j])/nb_files)
	info[0,j]=np.sum(maxtokdoc[:,j])/nb_files

with open("info.txt", "wb") as fp:   #Pickling
	pickle.dump(info, fp)

with open("info.txt", "rb") as fp:   
	 info= pickle.load(fp)


maxtokdoc=np.zeros((nb_files,nb_tokens))
for i in range(len(doctok_matrix)) :
	for j in range(len(vec_of_tokens)) :
		if vec_of_tokens[j] in doctok_matrix[i]:
			maxtokdoc[i,j]=doctok_matrix[i][vec_of_tokens[j]]*info[0,j]

print(maxtokdoc)

with open("D.txt", "wb") as fp:   #Pickling
	pickle.dump(maxtokdoc, fp)

with open("D.txt", "rb") as fp:   
	 tf= pickle.load(fp)


MTM=np.dot(np.transpose(tf),tf)
v, P = np.linalg.eig(MTM)

with open("v.txt", "wb") as fp:   #Pickling
	pickle.dump(v, fp)

with open("P.txt", "wb") as fp:   #Pickling
	pickle.dump(P, fp)

#print(v)

Diag=np.dot(np.dot(np.linalg.inv(P),MTM),P)
#print(Diag)

with open("Diag.txt", "wb") as fp:   #Pickling
	pickle.dump(Diag, fp)


