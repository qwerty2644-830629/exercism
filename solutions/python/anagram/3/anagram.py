def find_anagrams(word, candidates):
    answer = []
    
    for i, index in enumerate(candidates):
                if sorted(index.upper()) == sorted(word.upper()) and word.upper() != candidates[i].upper(): answer.append(i)

    return sorted([candidates[i] for i in answer])
