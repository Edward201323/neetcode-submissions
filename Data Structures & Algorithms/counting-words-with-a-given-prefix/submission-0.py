class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        sol = 0
        for word in words:
            if pref == word[:len(pref)]:
                sol += 1

        return sol
                    