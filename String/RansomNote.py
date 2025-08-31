class RansomNote:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool :
        character_map = {}
        for char in magazine :
            character_map[char] = character_map.get(char, 0) + 1

        for char in ransomNote:
            if char not in character_map or character_map.get(char) == 0:
                return False
            else:
                character_map[char] = character_map.get(char, 0) - 1
        return True

r = RansomNote()
print(r.canConstruct("ab","aab"))

        