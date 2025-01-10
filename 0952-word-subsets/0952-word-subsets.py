class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required_chars = Counter()
        for subset_word in words2:
            required_chars |= Counter(subset_word)
        l = []
        for candidate_word in words1:
            if not (required_chars - Counter(candidate_word)):
                l.append(candidate_word)
        return l