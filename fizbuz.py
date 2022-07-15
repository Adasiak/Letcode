class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        for i in range(n):
            print(i)
            if (i % 3 == 0) and i % 5==0:
                return "FizzBuzz"
            elif i % 3==0:
                return "Fizz"
            elif i % 5==0:
                return "Buzz"
            else:
                return str(n)
            
        
def clear():
    import os 
    os.system("clear")
clear()
somprob = Solution

ans = somprob.fizzBuzz(15,15)
print(ans)