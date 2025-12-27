"""Functions to help edit essay homework using string manipulation."""

def capitalize_title(title):# 每個單字的第一個字母大寫
    # title (the original string)(原始字串)
    
    return title.title()
    
def check_sentence_ending(sentence): # checking the end is ',' (檢查結尾為',')
     # sentence (the original string) (原始字串)

    return sentence.endswith('.')

def clean_up_spacing(sentence):
    # sentence (the original string) (原始字串)

    return sentence.strip()   

def replace_word_choice(sentence, old_word, new_word):
    # change {old_word} to {new_word} in {sentnce}
    # sentence (the original string) (原始字串)
    # old_word (目標文字) nwe_word (交換文字)

    return sentence.replace(old_word, new_word)