def lines_startswith(file, letter):

    matches = []

    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))
                                        
    return matches

def write_to_file(file, sentences):

    file.write(sentences)


def make_pairs(list1, list2):

    pairs = []

    inner_list = []
    for i in range(len(list1)):
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)
        

    return pairs





