def is_palindrome(word): 
    
    for i in range(0, int(len(word)/2)):  
        if word[i] != word[len(word)-i-1]: 
            return False
    return True
    
word_to_check = input("Podaj słowo do sprawdzenia\n")
ans = is_palindrome(word_to_check) 

if (ans): 
    print(f"""Tak, słowo {word_to_check} to palindrom""") 
else: 
    print(f"""Nie, słowo {word_to_check} to nie palindrom""") 
