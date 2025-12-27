"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word): # add un to {word}

    return 'un' + word



def make_word_groups(vocab_words):
    # vocab_words [<prefix>, <word_1>, <word_2> .... <word_n>]
    prefix = ' :: ' + vocab_words[0]
    return prefix.join(vocab_words)    


def remove_suffix_ness(word):
    if word.endswith('ness'):
        word = word[:-4]

        if word[-1] == 'i':
            word = word[:-1] + 'y'

    return word

def adjective_to_verb(sentence, index):
    # sentence (句子)
    # index (第幾個單詞)

    sentence_list = sentence.split() # divid sentence
    word = sentence_list[index].strip(".") # choose the verb and remove '.'

    return word + "en"
        
