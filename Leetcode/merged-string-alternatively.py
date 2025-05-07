def merged_strings_alternatively(word1, word2):
    merged_strings = []
    size = min(len(word1), len(word2))
    for i in range(size):
        merged_strings.append(word1[i])
        merged_strings.append(word2[i])
    merged_strings.append(word1[size:])
    merged_strings.append(word2[size:])
    return "".join(merged_strings)


word1 = "abc"
word2 = "pq"
print(merged_strings_alternatively(word1, word2))