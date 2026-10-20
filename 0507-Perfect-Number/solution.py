
class Solution:
    def checkPerfectNumber(self, n):
        if n <= 1:
            return False

        total = 1
        i = 2

        while i * i <= n:
            if n % i == 0:
                total += i

                other = n // i
                if other != i:
                    total += other

            i += 1

        return total == n
