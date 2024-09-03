def single_root_words(root_word, *other_words):
    same_words = []
    root_word.lower()

    for i in other_words:
        i.lower()
        if i.count(root_word) or i in root_word:
            same_words.append(i)

    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
