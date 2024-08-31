def validPalindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        if not isAlphaNum(s[l]):
            l += 1
            continue
        if not isAlphaNum(s[r]):
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return "false"
        l += 1
        r -= 1             #this l, r will be incremented and decremented when the if(two strings are not equal) statement is not executed
    return "true" 
        
def isAlphaNum(c):
    return "A" <= c <= "Z" or "a" <= c <= "z" or "0" <= c <= "9"

# out = validPalindrome("A man, a plan, a canal: Panama")
out = validPalindrome("race a car")
# out = validPalindrome(" ")
print(out)