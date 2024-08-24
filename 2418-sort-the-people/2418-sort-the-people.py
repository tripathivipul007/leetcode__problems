class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired = zip(names, heights)
        sorted_pairs = sorted(paired, key=lambda x: x[1], reverse=True)
        result = [name for name, height in sorted_pairs]
        return result
    