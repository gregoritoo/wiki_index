import numpy as np 
import pandas as pd
import os 
import pickle
import matplotlib.pyplot as plt 
import sys
import nltk
np.set_printoptions(threshold=sys.maxsize)
import seaborn as sns; sns.set()
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.snowball import FrenchStemmer
import string
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import matplotlib
import matplotlib.pyplot as plt
import numpy as np



def compute_cosine_similarity(query,tf_idf):
	return cosine_similarity(query, tf_idf)[0]


def classify(similarity_list,top_size=10,min=0.1):
	ranking=[]
	if np.max(similarity_list) < min :
		return 0
	while top_size > 0 :
		pos=np.argmax(similarity_list)
		ranking.append(pos)
		similarity_list[pos]= 0
		top_size = top_size - 1
	return ranking


def plot_words_informations(tf,idf,nb_words_to_show=10,method="max"):
	word_vec = np.array(tf.get_feature_names())
	sorting_vec = np.argsort(idf).flatten()[::-1]
	if method == "min" :
		sorting_vec = np.flip(sorting_vec)
	labels = [word_vec[sorting_vec[i]] for i in range(nb_words_to_show)]
	x = np.arange(len(labels)) 
	width = 0.35  
	fig, ax = plt.subplots()
	rects1 = ax.bar(x , idf[sorting_vec][:nb_words_to_show], width)
	ax.set_ylabel('Information')
	if method == "min" :
		ax.set_title('Less informative words')
	else : 
		ax.set_title('Most informative words')
	ax.set_xticks(x)
	ax.set_xticklabels(labels)
	ax.legend()
	plt.show()

def clean_query(query,txt_fitted,language="french"):
	stemmer = FrenchStemmer()
	stemmed_text = ' '.join([stemmer.stem(word) for word in nltk.word_tokenize(query,language=language) if word.isalpha() ])
	print(stemmed_text)
	query_tok = txt_fitted.transform([stemmed_text]).toarray()
	return query_tok


def vectorize():
	index={}
	dirs = os.listdir("./clean_docs")
	nb_files=100
	i=0
	txt1=[]
	for file in dirs :
		if i < nb_files :
			count=0
			count_doc={}
			if file[0]!="." :
				index.update({str(i):str(file)})
				i=i+1
				with open(r"./clean_docs/"+str(file),"r") as f :
					if txt1==[]:
						txt1=[f.read()]
					else :
						txt1 = txt1+[f.read()]

	tf = TfidfVectorizer(smooth_idf=False, sublinear_tf=False, norm=None, analyzer='word')
	txt_fitted = tf.fit(txt1)
	doc_tok_matrix = txt_fitted.transform(txt1).toarray()
	idf = tf.idf_
	return index,tf,idf,doc_tok_matrix,txt_fitted


index,tf,idf,doc_tok_matrix,txt_fitted = vectorize()

plot_words_informations(tf,idf,nb_words_to_show=10,method="min")


query="chat"
Qt=clean_query(query,txt_fitted,language="french")
cos_matrix=compute_cosine_similarity(Qt,doc_tok_matrix)
ranking=classify(cos_matrix,top_size=4)

if ranking == 0 :
	print("no results to your request")
else :
	for element in ranking :
		print(index[str(element)])
 






"""
rr = dict(zip(txt_fitted.get_feature_names(), idf))
 
j=0
nb_files=len(os.listdir("./clean_docs"))
nb_tokens=len(idf)
matrix=np.zeros((nb_files,nb_tokens))
for file in dirs :
	for key,prob in rr.items() :
		j=0
		if j < nb_tokens and file[0]!="." :
			with open(r"./clean_docs/"+str(file),"r") as f :
					doc=f.read()
			if key in doc :
				matrix[i,j]=prob
			else :
				matrix[i,j]=0
			with open('stemmed_pages_order.csv', 'a') as f:
						f.write(file+"\n")
		j=j+1
	i=i+1


with open("matrixtf.txt", "wb") as fp:   #Pickling
	pickle.dump(matrix, fp)

with open("matrixtf.txt", "rb") as fp:   #Pickling
	tf=pickle.load(fp)

plt.matshow(tf,cmap=plt.cm.Blues)
plt.savefig("matrix.png")
plt.title("tf-idf matrix")

MTM=np.dot(np.transpose(tf),tf)

v, P = np.linalg.eig(MTM)

with open("V.txt", "wb") as fp:   #Pickling
	pickle.dump(v,fp)

with open("P.txt", "wb") as fp:   #Pickling
	pickle.dump(P,fp)

with open("matrixtf_idf.txt", "rb") as fp:   #Pickling
	tf=pickle.load(fp)

plt.matshow(tf,cmap=plt.cm.Blues)
plt.savefig("matrix.png")
plt.title("tf-idf matrix")

with open("matrixtf_idf.txt", "rb") as fp:   #Pickling
	tf=pickle.load(fp)

with open("V.txt", "rb") as fp:   #Pickling
	v=pickle.load(fp)


with open("P.txt", "rb") as fp:   #Pickling
	P=pickle.load(fp)

v=v.reshape(1,-1)
print(abs(v[:10]))
plt.plot(v[0][: 100])
plt.show(block=True)



mat=np.dot(np.dot(np.linalg.inv(P),tf),P)

plt.matshow(mat,cmap=plt.cm.Blues)
plt.savefig("matrix2.png")
plt.title("matrix")"""
