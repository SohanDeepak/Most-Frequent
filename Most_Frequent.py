def most_frequent(my_word):
    my_word = my_word.lower()
    word_split = []
    letter_dict = {}
    for i in range(0,len(my_word)):
        word_split.append(my_word[i])  

    word_split.sort()
    for letter in word_split:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    
    
    for j in letter_dict:
        print(str(j) + " = " + str(letter_dict[j]))
        
word = input("Please enter a string: ")
most_frequent(word)