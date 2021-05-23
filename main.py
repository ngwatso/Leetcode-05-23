class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        
        count = 0
        
        for i in stones:
            if i in jewels:
                count += 1
            else:
                continue
                
        return count
        

'''

U:

jewels = "Ain"
stones = "AAdSaffnnnNi"
output = 6

P:

iterate through stones; if i is in jewels, increase var count by 1

'''

# ===============

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        nums_2 = 0
        
        for num in nums:
            if nums.count(num) == 1:
                nums_2 += num
                
        return nums_2
        
'''

U:

[1, 2, 3, 4, 5, 3, 2]
output = 10

P:

create var nums_2; iterate through nums, if integer is unique, add to nums_2, if not; skip

'''

# ===============

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counts = {}
        
        for i in arr:
            if i not in counts:
                counts[i] = arr.count(i)
                
        if len(counts) != len(set(counts.values())):
            return False
            
        return True
        
        
'''

U:

[1, 2, 2, 1, 1, 3]
output = True

[1, 2, 3, 4, 5]
output = False

[1, 1, 2, 3, 3, 3, 4]
output = False

P:

Create Dict count; iterate through arr.  if i is not in count, add to count, with count()  set as value.  If all values in count are unique, return True, otherwise, return False

'''

# ===============