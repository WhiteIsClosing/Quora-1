import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag

lemmatizer = WordNetLemmatizer()

def do_tokenlize(text):
    words = nltk.tokenize._treebank_word_tokenize(text.lower())
    preprocessedText_pos = pos_tag(words)
    tokens = [do_lemmatization(term) for term in preprocessedText_pos]
    return tokens

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

def do_lemmatization(term):
    if get_wordnet_pos(term[1]) is '':
        return lemmatizer.lemmatize(term[0])
    else:
        return lemmatizer.lemmatize(term[0], get_wordnet_pos(term[1]))

def get_words_and_states(sentence1, sentence2):
    tokens1 = do_tokenlize(sentence1)
    tokens2 = do_tokenlize(sentence2)
    st1 = [0]*len(tokens1)
    st2 = [0]*len(tokens2)
    set1 = set(tokens1)
    set2 = set(tokens2)
    for i in range(1,len(tokens1)):
        if tokens1[i] not in set2:
            st1[i] = 1
    for i in range(1, len(tokens2)):
        if tokens2[i] not in set1:
            st2[i] = 1
    return tokens1, st1, tokens2, st2