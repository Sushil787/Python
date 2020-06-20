import json

def condition(wor,worr):
    if wor in worr:
        final=worr[wor]
        return final
    else:
        print("Not in dictionery :/")
        from difflib import get_close_matches
        if len(get_close_matches(wor,worr))>0:
            sugges=get_close_matches(wor,worr)
            print(f"\nDo you mean {sugges}")
while 2<4:
    word=json.load(open("original.json"))
    print("\n\n")
    uword=input("Enter the word you want to search meaning of or enter x for exit: ")
    if uword=="x" or uword=="X":
        break
        exit()
    uword=uword.lower()
    output=condition(uword,word)
    if type(output)==list:
        for i in output:
            print("\n\t"+i)
    else:
        print(output)