#using tuple
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # mapping char count to list of anagrams
        for string in strs:
            count = [0] * 26  # creates a list of 26 zeros for letter frequency
            for char in string:  # iterating through each character in the string
                count[ord(char) - ord("a")] += 1
            anagrams[tuple(count)].append(string)
        return list(anagrams.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #creating a dictionary (key value pair still) + MUST SPECIFY DATA TYPE OF VALUE
        anagrams = defaultdict(list)

        #iterating through each string
        for string in strs:
            #sorted list sorts the characters in ascending order so ex: "eat" -> {['a', 'e', 't']: value}
            sorted_list = ''.join(sort(string))
            anagrams[sorted_list].append(string) #"eat" -> {['a', 'e', 't']: ["eat"]}
        return list(anagrams.values()) #returning thr list version of the anagrams values, since each value is a list of the grouped anagrams
