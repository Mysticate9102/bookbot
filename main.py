def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(count_words(file_contents))
        print(count_characters(file_contents))

def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    for c in text:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

main()
