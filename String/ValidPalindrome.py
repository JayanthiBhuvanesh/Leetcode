from curses.ascii import isalnum


def isValidPalindrome(s: str) -> bool :
    i, j = 0, len(s)-1
    while i<j:
        while i<j and not isalnum(s[i]): i+=1
        while i<j and not isalnum(s[j]): j-=1

        if s[i].lower() != s[j].lower():
            return False
        i+=1
        j-=1
    return True

print(isValidPalindrome("A man, a plan, a canal: Panama"))


