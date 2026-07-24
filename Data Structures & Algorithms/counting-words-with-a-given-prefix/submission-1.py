class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        sol = 0
        pref_length = len(pref)
        for word in words:
            if pref == word[:pref_length]:
                sol += 1

        return sol
                    