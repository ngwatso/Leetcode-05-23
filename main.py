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

