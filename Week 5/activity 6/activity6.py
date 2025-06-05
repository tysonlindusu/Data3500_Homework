"""
Programming Activity 6

Create a variable that stores the sentence below, and print the sentence to 
the console, before making any changes. Change the first letter in the 
sentence to be capitalized. Change the first instance of Whoa to be whoa 
(all lower case), and the second instance of Whoa to be WHOA(all upper case).  
Append a exclamation point to the end of the sentence. 
Then re-print the sentence to the console.

sentence = "dude, I just biked down that mountain and at first I was like 
Whoa, and then I was like Whoa"
 - using the string variable sentence, change the first letter to upper 
   case using capitalize()
 - create a list called "words" that stores all the words in the sentence 
   in a list using the split() function.
 - change the first "Whoa" to "whoa", and the second "Whoa" to "WHOA".
 - append an exclamation point.
 - print the new sentence.
"""
sentence = "dude, I just biked down that mountain and at first I was like Whoa, and then I was like Whoa"
print("Original sentence:")
print(sentence)
sentence = sentence[0].upper() + sentence[1:]
whoa_index_1 = sentence.find("Whoa")
if whoa_index_1 != -1:
    sentence = sentence[:whoa_index_1] + "whoa" + sentence[whoa_index_1 + 4:]

    whoa_index_2 = sentence.find("Whoa", whoa_index_1 + 4)
    if whoa_index_2 != -1:
        sentence = sentence[:whoa_index_2] + "WHOA" + sentence[whoa_index_2 + 4:]
sentence += "!"
print("\nModified sentence:")
print(sentence)
