def isValidAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = {}
    for c in str1:
        counter[c] = counter.get(c,0) +1
    for c in str2:
        if c not in counter or counter[c] == 0:
            return False
        counter[c] = counter.get(c) -1

    return True

print(isValidAnagram("eat", "tea"))