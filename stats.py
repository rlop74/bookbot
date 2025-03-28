def get_num_words(text):
    split_text = text.split()
    return len(split_text)

def get_char_count(text):
    result = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_on(dict):
    return dict["num"]

def convert_chardict_to_listofdict(dict):
    list = []
    for char in dict:
        list.append({"char": char, "num": dict[char]})
    list.sort(reverse=True,key=sort_on)
    return list
