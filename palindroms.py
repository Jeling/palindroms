import re

def is_palindrome(word): 
    
    text = re.sub('[^a-z]+', '', word.lower())
    for i in range(0, int(len(text)/2)):  
        if text[i] != text[len(text)-i-1]: 
            return False
    return True

    #for i in range(0, int(len(word)/2)):  
        #if word[i] != word[len(word)-i-1]: 
            #return False
    #return True
    
word_to_check = input("Podaj słowo do sprawdzenia\n")
ans = is_palindrome(word_to_check) 

if (ans): 
    print(f"""Tak, {word_to_check} to palindrom""") 
else: 
    print(f"""Nie, {word_to_check} to nie palindrom""") 
