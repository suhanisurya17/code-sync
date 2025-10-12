class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		else:
			sMap = {}
			for char in s:	
				sMap[char] = sMap.get(char, 0) + 1
			
			tMap = {}
			for char in t:	
				tMap[char] = tMap.get(char, 0) + 1
			return sMap == tMap