from typing import Any

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1
    return char_count

def sort_chars_by_count(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        # A chave deve ser "num" para corresponder à função de ordenação
        sorted_list.append({"char": char, "num": count})

    # A função de ordenação pode ser definida aqui
    def sort_on(item):
        return item["num"]

    # A chamada de sort usa o nome correto da função
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
