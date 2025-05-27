def get_num_words(astring):
    return f"{len(astring.split())} total words"

def count_char(astring):
    adict = dict.fromkeys(astring.lower())
    for x in adict:
        adict[x] = astring.lower().count(x)
    return adict

def sort_on(dict):
    return dict["num"]

def sort_dict(aDict):
    sList = []
    for x in aDict:
        sList.append({"char" : x , "num" : aDict[x] })
    sList.sort(reverse = True , key=sort_on)
    return sList