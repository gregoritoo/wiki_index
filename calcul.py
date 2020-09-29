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
#print(rr)
j=0
nb_files=len(os.listdir("./clean_docs"))
nb_tokens=len(idf)
matrix=np.zeros((nb_files,nb_tokens))
for key,prob in rr.items() :

	i=0
	for file in dirs :
		if i < nb_files :
			with open(r"./clean_docs/"+str(file),"r") as f :
					doc=f.read()

			if key in doc :
				matrix[i,j]=prob
			else :
				matrix[i,j]=0
		i=i+1
	j=j+1


with open("matrixtf_idf.txt", "wb") as fp:   #Pickling
	pickle.dump(matrix, fp)
