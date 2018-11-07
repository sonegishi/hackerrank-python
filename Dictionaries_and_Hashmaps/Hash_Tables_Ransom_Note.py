def check_magazine(magazine, note):
    note_dict = dict()
    for word in note:
        if word not in note_dict:
            note_dict[word] = 1
        else:
            note_dict[word] += 1

    for word in magazine:
        if word in note_dict:
            note_dict[word] -= 1
            if note_dict[word] <= 0:
                del note_dict[word]
        if len(note_dict) == 0:
            return 'Yes'

    return 'No'
