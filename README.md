# Text Preprocessing Python Package

### This text cleaning and preprocessing package contains:

- get word, character, uppercase letters, and numbers in text.
- get and remove/clean special characters and punctuations.
- remove html tags.
- remove accented characters.
- get and remove @emails.
- get and remove urls (http, https, ftp, ssh).
- remove common and rare words.
- remove multiple spaces.

- get and remove stopwords for _English language_ 
- convert contractions for _English language_ 
- spelling correction for _English language_ 
- convert into base or root form of word for _English language_


#### Requirements:
```
pip install bs4
pip install spacy
pip install textblob
pip install contractions
pip install python -m spacy download en_core_web_sm
```

Install package by following command:
```
pip install TextPrepR
```

```
import TextPrepR as tp

text = 'howw arr yu todasyy?'
tp.spelling_correction('en', text).raw_sentences[0]
>> 'how are you today?'

text = 'how,, are you % today?'
tp.get_special_chars(text)
>> ',,   % ?'

tp.remove_special_chars(text)
>> 'how are you today'
```






