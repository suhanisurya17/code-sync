class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # mapping char count to list of anagrams
        for string in strs:
            count = [0] * 26  # creates a list of 26 zeros for letter frequency
            for char in string:  # iterating through each character in the string
                count[ord(char) - ord("a")] += 1
            anagrams[tuple(count)].append(string)
        return list(anagrams.values())
