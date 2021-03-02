def print_upper_words(words):
    """Prints each word in a list in all caps on separate lines"""  

    for word in words:
        print(f"{word.upper()}\n")


print("------------------------");
print("print_upper_words");
print("------------------------");
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])



def print_upper_words_with_e(words):
    """Prints each word that starts with e or E in a list in all caps on separate lines """  

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(f"{word.upper()}\n")


print("------------------------");
print("print_upper_words_with_e");
print("------------------------");
print_upper_words_with_e(["hello", "everybody", "goodbye", "yo", "yes", "Everyone"])



def print_upper_words_with_arg(words, must_start_with):
    """Prints each word that starts with letters provided in must_start
         in a list in all caps on separate lines """  

    for word in words:
        for char in must_start_with:
            if word.startswith(char):
                print(f"{word.upper()}\n")



print("------------------------");
print("print_upper_words_with_arg");
print("------------------------");
print_upper_words_with_arg(["hello", "hey", "everybody", "goodbye", "yo", "yes", "Everyone"], must_start_with={"h", "y"})