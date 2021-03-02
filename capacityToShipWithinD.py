class Solution:
    def shipWithinDays(self, weights, D):
        left ,right = 1, sum(weights)
        ans = 0
        while left <= right:
            mid = left + (right-left) //2
            day_count = self.get_day_count(weights,mid, D)
            if day_count <= D:
                ans = mid
                prev_day = day_count
                right = mid -1
            else:
                left = mid + 1
                
        return ans
            
    
    
    def get_day_count(self,weights,cur_weight, D):
        count = 0
        cur_sum = 0
        for value in weights:
            cur_sum += value
            if value > cur_weight:
                return D + 1
            if cur_sum > cur_weight:
                count += 1
                cur_sum = value
        return count +1