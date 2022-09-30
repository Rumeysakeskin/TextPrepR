from TextPrepR import utils

__version__ = "0.0.1"

def get_word_counts(x):
	return utils._get_word_counts(x)

def get_char_counts(x):
	return utils._get_char_counts(x)

def get_nums(x):
	return utils._get_nums(x)

def get_uppercase_counts(x):
	return utils._get_uppercase_counts(x)

def get_uppercase(x):
	return utils._get_uppercase(x)

def get_special_chars(x):
	return utils._get_special_chars(x)

def get_set_special_chars(x):
	return utils._get_set_special_chars(x)

def remove_special_chars(x):
	return utils._remove_special_chars(x)

def remove_html_tags(x):
	return utils._remove_html_tags(x)

def remove_accented_chars(x):
	return utils._remove_accented_chars(x)

def get_emails(x):
	return utils._get_emails(x)

def remove_emails(x):
	return utils._remove_emails(x)

def get_urls(x):
	return utils._get_urls(x)

def remove_urls(x):
	return utils._remove_urls(x)

def remove_common_words(x):
	return utils._remove_common_words(x)

def remove_rare_words(x):
	return utils._remove_rare_words(x)

def remove_multiple_spaces(x):
	return utils._remove_multiple_spaces(x)

def get_stopwords_counts(lang, x):
	return utils._get_stopwords_counts(lang, x)

def remove_stopwords(lang, x):
	return utils._remove_stopwords(lang, x)

def convert_contractions(lang, x):
	return utils._convert_contractions(lang, x)

def spelling_correction(lang, x):
	return utils._spelling_correction(lang, x)

def make_base(lang, x):
	return utils._make_base(lang, x)






