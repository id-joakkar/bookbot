def printext():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return(file_contents)
    
if __name__ == "__main__":
    words = printext()
    total = len(words.split())
    charcount = {}
    for l in words:
        low = l.lower()
        if  charcount.get(low) != None:
            charcount[low] += 1
        elif l.isalpha():
             charcount[low] = 1
    chartuple = [(k, v) for k, v in charcount.items()]
    newsort = sorted(chartuple,key = lambda tup:tup[1], reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total} words were found in the document")
    for n in newsort:
        print(f"The '{n[0]}' character was found {n[1]} times")
    print("--- End report ---")
