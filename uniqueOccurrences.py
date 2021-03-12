from collections import Counter , List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numbers_count = Counter(arr)      
        values_counter = Counter(numbers_count.values())
        for number in values_counter.values():
            if number > 1:
                return False
        
        return True