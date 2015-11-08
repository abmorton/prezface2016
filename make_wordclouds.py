from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
# import matplotlib.pyplot as plt
# from os import path

text = open('constitution.txt', 'r').read()
inpath = 'static/bw_pngs/'
outpath = 'static/wordcloud_pngs/'

for c in range(1,19):
	img = Image.open(inpath+str(c)+'.png')
	img = img.resize((490,540), Image.ANTIALIAS)
	hcmask = np.array(img)
	wordcloud = WordCloud(background_color="white", max_font_size=23, max_words=320, mask=hcmask, stopwords=STOPWORDS)
	wordcloud.generate(text)
	wordcloud.to_file(outpath+str(c)+'_wordcloud.png')