def full_words_search_function(pattern, text):
    words_split = text.split(" ")

    def _get_position(i):
        return len(" ".join(words_split[0:i]))

    return [
        _get_position(i) + 1 if i > 0 else _get_position(i)
        for i, word in enumerate(words_split)
        if word == pattern
    ]


print(full_words_search_function("abc", "xyz abc def abc mno"))
