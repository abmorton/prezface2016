from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
# import matplotlib.pyplot as plt

inpath = 'static/bw_pngs/'
outpath = 'static/wordcloud_pngs/'

# This is to generate wordclouds super-imposed on the cadidates' faces.

for c in range(1,19):
	text = open('static/txt/'+str(c)+'.txt', 'r').read()
	img = Image.open(inpath+str(c)+'.png')
	img = img.resize((490,540), Image.ANTIALIAS)
	hcmask = np.array(img)
	wordcloud = WordCloud(background_color="white", max_font_size=23, max_words=310, mask=hcmask, prefer_horizontal=0.94, stopwords=STOPWORDS)
	wordcloud.generate(text)
	wordcloud.to_file(outpath+str(c)+'_wordcloud.png')

# Making block word clouds (not masked).
	# text = open('static/txt/'+c.id+'.txt', 'r').read()
	wordcloud = WordCloud(background_color="white", max_font_size=43, max_words=250, width=700, height=450, prefer_horizontal=1.0, stopwords=STOPWORDS)
	wordcloud.generate(text)
	wordcloud.to_file(outpath+str(c)+'_block_wordcloud.png')


# Make Liberty Bell / Constitution word cloud.
# text = open('static/txt/constitution.txt', 'r').read()
# img = Image.open('libertybell.png')
# img = img.resize((400,440), Image.ANTIALIAS)
# hcmask = np.array(img)
# wordcloud = WordCloud(background_color="white", margin=1, max_font_size=50, max_words=200, mask=hcmask, stopwords=STOPWORDS)
# wordcloud.generate(text)
# wordcloud.to_file('libertybell_constitution_wordcloud.png')