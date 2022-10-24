class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for x in range(1, n + 1):
            temporary = ''
            if x % 3 == 0:
                temporary += 'Fizz'
            if x % 5 == 0:
                temporary += 'Buzz'
            if x % 3 != 0 and x % 5 !=0:
                temporary +=str(x)
            result.append(temporary)
        return result