def is_palindrome(strng):
    rev_str = ""
    ngidx = -1
    for i in range(len(strng)):
        rev_str += strng[ngidx]
        ngidx -=1
        
    if rev_str == strng:
        return True
    else:
        return False
    
welcome = True
gamecont = ["y", "n"]
while welcome == True:
    word = input("Give me a word and I will tell you if it is a palindrome or not: ")
    lword = word.lower()
    if lword.isalpha():
        if is_palindrome(lword) ==  True:
            print(f"{is_palindrome(lword)}, ".upper() + word + " is a palindrome!")
        else:
            print(f"{is_palindrome(lword)}, ".upper() + word + " is not a palindrome!")
    else:
        print("input error, type in a word")
    while welcome == True:
        newattempt = input("Try another word (y/n)? ")
        if newattempt in gamecont and newattempt == "n":
            welcome = False
        elif newattempt in gamecont and newattempt == "y":
            break
        else:
            print("Wrong input!")
    print()