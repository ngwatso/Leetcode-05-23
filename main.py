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