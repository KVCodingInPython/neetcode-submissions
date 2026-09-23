class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sumOfSquares(n)

        return n == 1

        



    def sumOfSquares(self, a: int) -> int:
        sum = 0
        while (a > 0):
            sum += pow((a % 10), 2)
            a //= 10
        return sum
        

