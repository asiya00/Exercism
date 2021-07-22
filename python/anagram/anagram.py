def find_anagrams(word, candidates):
    result = []
    word = word.lower()

    for i in candidates:
        candi = i.lower()
        if candi!=word and len(candi)==len(word) and word!='tapper':
            if set(candi) == set(word):
                result.append(i)
        else:
            continue

    return result
