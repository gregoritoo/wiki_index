#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd 
import requests 
import bs4
import re
import random
import html2text
import os
import time



def scrapping(init_page,nb_pages,regex,info=True,directory="./docs/") :
	'''
	This function crawl the web and save the html pages in a txt file and keep the list in a txt file from the init page jumping from link to link
	:parameters:
	:input:
		init_page : str
		starting web page for crawling
		regex= str
		regex for finding links in the html code
		nb_pages : int
		nb of web pages to save
	:output:
		none
	'''
	init_page=init_page
	html = requests.get(init_page)
	pattern=re.compile(regex)
	print(pattern)
	matches=pattern.finditer(html.text)
	dict={init_page:1}
	i=0
	print(matches)
	nb_files=len(os.listdir(directory))
	for w in range(nb_pages) :
		while nb_files+i < nb_pages+nb_files :
			for match in matches :
				if info :
					print(dict)
					print(match.group(0))
				#print("len dict",len(dict))
				if not match.group(0) in dict.keys() :
					dict.update({match.group(0):0})
					random_num=random.randint(1,len(dict)-1)
					tab=[element for element in dict.keys()]
					page="https://fr.wikipedia.org"+tab[random_num]
					if not os.path.isfile(directory+match.group(0).replace("/","_")+".txt") :
						with open(directory+match.group(0).replace("/","_")+".txt","w") as file :
							print("saving file")
							file.write(html2text.html2text(html.text))
						#not necessary with a better regex
						with open('pages.csv', 'a') as f:
							f.write(page+"\n")
				else :
					dict[match.group(0)]=1	
				j=0
				while dict[tab[random_num]] == 1 :
					random_num=random.randint(0,len(tab)-1)
					j=j+1
					if j > len(dict)- 1 :
						break
				
				if info :
					print(page)
				html = requests.get(page)
				matches=pattern.finditer(html.text)
				i=i+1



if __name__ == '__main__':
	page_init="https://fr.wikipedia.org/wiki/Mathématiques"
	scrapping(page_init,500,regex='(\/wiki\/[\w:]*)')