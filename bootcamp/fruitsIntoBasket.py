class Solution:
    def totalFruit(self, tree) -> int:
        fruit_count = {}
        max_count = 0
        start = 0
        end = 0
        count = 0
        for fruit in tree:
            fruit_count[fruit] = fruit_count.get(fruit,0) + 1
            while len(fruit_count) > 2:
                if fruit_count[tree[start]] != 1:
                    fruit_count[tree[start]] -= 1
                else:
                    del fruit_count[tree[start]]
                start += 1
            if len(fruit_count) <= 2: 
                max_count = max(max_count, sum(fruit_count.values()))
           
        return max_count 
                
            
        