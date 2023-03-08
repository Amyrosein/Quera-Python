import string


def words_check(text):
    k = 0
    alph = string.ascii_letters
    text_list = text.replace("\n", " ").split()
    new_text_list = []
    for texts in text_list:
        l = len(texts)/2
        c = 0
        for i in texts:
            if i not in alph:
                c += 1
                texts = texts.replace(i, '')
        if c < l:
            new_text_list.append(texts.capitalize())
        k += 1
    text_dict = dict([[x, new_text_list.count(x)] for x in set(new_text_list)])
    return text_dict
