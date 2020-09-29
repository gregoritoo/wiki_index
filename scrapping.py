import numpy as np 
import pandas as pd 
import requests 
import bs4
import re
import random
import html2text
#soup = bs4.BeautifulSoup(rep.text, 'html.parser')
#em_box = soup.find_all("em", {"class":"agency-website"})


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
	for w in range(nb_pages) :
		for match in matches :
			if info :
				print("------",match.group(0))
				print(dict)
			#print("len dict",len(dict))
			if not match.group(0) in dict.keys() :
				dict.update({match.group(0):0})
				random_num=random.randint(1,len(dict)-1)
				tab=[element for element in dict.keys()]
				with open(directory+"doc_"+str(i)+".txt","w") as file :
					print("saving file")
					file.write(html2text.html2text(html.text))
			else :
				dict[match]=1	
			j=0
			while dict[tab[random_num]] == 1 :
				random_num=random.randint(0,len(tab)-1)
				j=j+1
				if j > len(dict)- 1 :
					break
			#not necessary with a better regex
			page="https://fr.wikipedia.org"+tab[random_num]
			if info :
				print(page)
			html = requests.get(page)
			matches=pattern.finditer(html.text)
			i=i+1
			with open('pages.csv', 'w') as f:
			        f.write(page+"\n")

if __name__ == '__main__':
	page_init="https://fr.wikipedia.org/wiki/Mathématiques"
	scrapping(page_init,102,regex='(\/wiki\/[\w:]*)')