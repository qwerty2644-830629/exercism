def find_anagrams(word, candidates):
    word_set = sorted(word.upper())
    candidates_list = [sorted(i.upper()) for i in candidates]
    answer = []
    
    for i, index in enumerate(candidates_list):
                if index == word_set and len(word) == len(candidates[i]) and word.upper() != candidates[i].upper(): answer.append(i)

    print(answer, sorted([candidates[i] for i in answer]))
    return sorted([candidates[i] for i in answer])
