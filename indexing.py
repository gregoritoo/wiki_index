import numpy as np 
import pandas as pd 
from scrapping import scrapping
from preprocessing import clean_txt_files


if __name__ == '__main__':
	page_init="https://fr.wikipedia.org/wiki/Mathématiques"
	scrapping(page_init,102,regex='(\/wiki\/[\w:]*)')
	clean_txt_files(directory="./docs")