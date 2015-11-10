from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import random
from app import db, Candidate
# import matplotlib.pyplot as plt

# Add any stopwords here.
STOPWORDS.add('https')
STOPWORDS.add('u200b')
STOPWORDS.add('u2019')
STOPWORDS.add('XL')
STOPWORDS.add('u2019s')
STOPWORDS.add('co')
STOPWORDS.add('Get')
STOPWORDS.add('u201cbody')
STOPWORDS.add('AP')
STOPWORDS.add('u2019re')
STOPWORDS.add('nhttps')
STOPWORDS.add('u27a1')
STOPWORDS.add('u2019t')
STOPWORDS.add('u2019m')
STOPWORDS.add('u2013')
STOPWORDS.add('u2019ve')
STOPWORDS.add('u201d')
STOPWORDS.add('u2192')
STOPWORDS.add('u2014')
STOPWORDS.add('u2019ll')
STOPWORDS.add('u2019m')
STOPWORDS.add('u2026')
STOPWORDS.add('Q')
STOPWORDS.add('t')
STOPWORDS.add('nGet')
STOPWORDS.add('ET')
STOPWORDS.add('amp')
STOPWORDS.add('H')
STOPWORDS.add('s')
STOPWORDS.add('gt')
STOPWORDS.add('n')
STOPWORDS.add('u200bGet')
STOPWORDS.add('8pm')
STOPWORDS.add('7pm')
STOPWORDS.add('EDT')

inpath = 'static/bw_pngs/'
outpath = 'static/wordcloud_pngs/'

# Querying candidates to get parties so we can use custom colors for different parties.
candidates = Candidate.query.all()

# Color customizations
def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(220, 70%%, %d%%)" % random.randint(38, 88)

def red_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 69%%, %d%%)" % random.randint(27, 80)


# This is to generate wordclouds super-imposed on the cadidates' faces.
for c in candidates:
	text = open('static/txt/'+str(c.id)+'.txt', 'r').read()
	# img = Image.open(inpath+str(c.id)+'.png')
	# img = img.resize((490,540), Image.ANTIALIAS)
	# hcmask = np.array(img)
	# wordcloud = WordCloud(background_color="white", max_font_size=23, max_words=310, mask=hcmask, prefer_horizontal=0.94, stopwords=STOPWORDS)
	# wordcloud.generate(text)
	# wordcloud.to_file(outpath+str(c.id)+'_wordcloud.png')

# Making block word clouds (not masked).
	wordcloud = WordCloud(background_color="white", margin=2, max_font_size=48, max_words=200, width=700, height=450, prefer_horizontal=1.0, stopwords=STOPWORDS)
	wordcloud.generate(text)
	if c.party == 'Republican Party':
		print c.party
		wordcloud.recolor(color_func=red_color_func, random_state=3)
	elif c.party == 'Democratic Party':
		print c.party
		wordcloud.recolor(color_func=blue_color_func, random_state=3)
	wordcloud.to_file(outpath+str(c.id)+'_block_wordcloud.png')


# Make Liberty Bell / Constitution word cloud.
# text = open('static/txt/constitution.txt', 'r').read()
# img = Image.open('libertybell.png')
# img = img.resize((400,440), Image.ANTIALIAS)
# hcmask = np.array(img)
# wordcloud = WordCloud(background_color="white", margin=1, max_font_size=50, max_words=200, mask=hcmask, stopwords=STOPWORDS)
# wordcloud.generate(text)
# wordcloud.to_file('libertybell_constitution_wordcloud.png')