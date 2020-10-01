import numpy as np 
import pandas as pd
import os 
import pickle
import matplotlib.pyplot as plt 
import sys
np.set_printoptions(threshold=sys.maxsize)
import seaborn as sns; sns.set()
np.set_printoptions(threshold=sys.maxsize)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
dirs = os.listdir("./clean_docs")
nb_files=100
i=0
txt1=[]
for file in dirs:
	if i < nb_files :
		i=i+1
		count=0
		count_doc={}
		if file[0]!="." :
			with open(r"./clean_docs/"+str(file),"r") as f :
				if txt1==[]:
					txt1=[f.read()]
				else :
					txt1 = txt1+[f.read()]

tf = TfidfVectorizer(smooth_idf=False, sublinear_tf=False, norm=None, analyzer='word')
txt_fitted = tf.fit(txt1)
txt_transformed = txt_fitted.transform(txt1)


#print(tf.vocabulary_)


idf = tf.idf_

rr = dict(zip(txt_fitted.get_feature_names(), idf))
 
j=0
nb_files=len(os.listdir("./clean_docs"))
nb_tokens=len(idf)
matrix=np.zeros((nb_tokens,nb_files))
for key,prob in rr.items() :
	i=0
	for file in dirs :
		if i < nb_files and file[0]!="." :
			with open(r"./clean_docs/"+str(file),"r") as f :
					doc=f.read()
			if key in doc :
				matrix[j,i]=prob
			else :
				matrix[j,i]=0
			with open('stemmed_pages_order.csv', 'a') as f:
						f.write(file+"\n")
		i=i+1
	j=j+1


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



with open("matrixtf.txt", "rb") as fp:   #Pickling
	tf=pickle.load(fp)



with open("V.txt", "rb") as fp:   #Pickling
	v=pickle.load(fp)


with open("P.txt", "rb") as fp:   #Pickling
	v=pickle.load(fp)
v=np.sort(v)

plt.plot(v)
plt.show()