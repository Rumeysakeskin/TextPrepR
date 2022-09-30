import re
import os
import sys
import pandas as pd
import numpy as np
import spacy
from spacy.lang.en.stop_words import STOP_WORDS as stopwords
from bs4 import BeautifulSoup
import unicodedata
from textblob import TextBlob
import contractions

def _get_word_counts(text):
	return len(str(text).split())

def _get_char_counts(text):
	return len("".join(text.split()))

def _get_nums(text):
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	nums = []
	words = text.split()
	for word in words:
		for char in word:
			if char in numbers:
				if word not in nums:
					nums.append(word)
	return nums

def _get_uppercase_counts(text):
	return len([t for t in "".join(text.split()) if t.isupper()])

def _get_uppercase(text):
	return [t for t in "".join(text.split()) if t.isupper()]

# remove special char and punctuations
def _get_special_chars(text):
	return re.sub(r'[\w]+', '', text)

def _get_set_special_chars(text):
	return set(_get_special_chars(text))

def _remove_special_chars(text):
	return " ".join(re.sub(r"[^\w ]+","",text).split())

def _remove_html_tags(text):
	return BeautifulSoup(text,"lxml").get_text().strip()

def _remove_accented_chars(text):
	return unicodedata.normalize("NFKD",text).encode("ascii","ignore").decode("utf-8","ignore")

def _get_emails(text):
	emails = re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', text)
	counts = len(emails)

	return counts, emails

def _remove_emails(text):
	return re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)',"",text)

def _get_urls(text):
	urls = re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',text)
	counts = len(urls)
	return counts, urls

def _remove_urls(text):
	return re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?',"",text)

def _get_value_counts(df, col):
	text = " ".join(df[col])
	text = text.split()
	freq = pd.Series(text).value_counts()
	return freq

def _remove_common_words(text, freq, n=20):
	fn = freq[:n]
	return " ".join([t for t in text if t not in fn])

def _remove_rare_words(text, freq, n=20):
	fn = freq.tail(n)
	return " ".join([t for t in text if t not in fn])

def _remove_multiple_spaces(text):
	return ' '.join(text.split())


def _get_stopwords_counts(lang, text):
    if lang== 'en':
        length = len([t for t in text.split() if t in stopwords])
        return length
    else:
        raise NameError("{} is not supported yet!".format(lang))

def _remove_stopwords(lang, text):
	if lang == 'en':
		return " ".join([ t for t in text.split() if t not in stopwords])
	else:
		raise NameError("{} is not supported yet!".format(lang))

def _convert_contractions(lang, text):
	if lang == 'en':
		return contractions.fix(text)
	else:
		raise NameError("{} is not supported yet!".format(lang))

def _spelling_correction(lang, text):
	if lang == 'en':
		return TextBlob(text).correct()
	else:
		raise NameError("{} is not supported yet!".format(lang))

def _make_base(lang, text):
	if lang == 'en':
		nlp = spacy.load("en_core_web_sm")
		text_list = []
		doc = nlp(str(text))

		for token in doc:
			lemma = token.lemma_
			if lemma == "-PRON-" or lemma == "be":
				lemma = token.text
			text_list.append(lemma)

		return " ".join(text_list)

	else:
		raise NameError("{} is not supported yet!".format(lang))
