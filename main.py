import string  


def get_text(path):
     with open(path) as f:
        return f.read()

def get_num_of_words(text):
    words = text.split()
    return len(words)

def get_num_of_letters(text):
    obj = {}
    my_string = ",".join(str(element) for element in text.split()).lower()
    only_letters = []
    lower = list(string.ascii_lowercase)  
    for char in my_string:
         if char in lower:
            only_letters.append(char)
    for letter in only_letters:
        if letter in obj:
              obj[letter] += 1
        else:
             obj[letter] = 1
        
    return obj

def print_report(path, num_of_words, list):
    print(f"--- Begin report of {path} ---")
    print(f"{num_of_words} words found in the document\n\n")
    
    for item in list:
        print(f"The '{item[0]}' was found {item[1]} times")
    print("--- End report ---")

def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    num_of_words = get_num_of_words(text)
    num_of_letters = list(get_num_of_letters(text).items())
    print_report(path, num_of_words, sorted(num_of_letters))    


if __name__ == "__main__":
    main()