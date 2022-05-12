input_data = """Choosing to do nothing is still a choice, after all after all nothing nothing
choice, choice, or choice, ,,       , that is choice of nothing """


def get_most_freq_words_counter(input_data):
    words_occurrence_dict = dict()
    cursor_position = 0
    for char_idx, char in enumerate(input_data):
        if char == " " or char == "\n" or char == ",":
            _word = input_data[cursor_position:char_idx]
            _word = _word.replace(",", "")
            _word = _word.replace(" ", "")
            _word = _word.replace("\n", "")
            if _word and _word.isspace():
                continue
            if not _word:
                continue

            try:
                words_occurrence_dict[_word] += 1
            except KeyError:
                words_occurrence_dict[_word] = 1

            cursor_position = char_idx

    return sorted(
        [x for x in words_occurrence_dict.items()], key=lambda item: item[1],
        reverse=True
    )[0:5]


def test_word_count_counter():
    assert get_most_freq_words_counter(input_data) == [
        ('choice', 5),
        ('nothing', 4),
        ('is', 2),
        ('after', 2),
        ('all', 2)
    ]


print(get_most_freq_words_counter(input_data))
test_word_count_counter()
