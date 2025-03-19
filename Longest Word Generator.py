#Takes user input to print the longest word in their sentence
def longest_word_finder(sentence):
    words = sentence.split()
    longest_word = max(words, key=len).capitalize()
    return longest_word

#Creates a loop which keeps running
while True:
    sentence = input("Please add a sentence here: ")
    
    if sentence.lower() == "exit":
        print("Goodbye!")
        break
    
    print(longest_word_finder(sentence))



    

