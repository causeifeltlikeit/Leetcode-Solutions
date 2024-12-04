class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzList = []
        for i in range(1,n+1):
            fizzString = ''
            if i % 3 == 0:
                fizzString = fizzString + 'Fizz'
            if i % 5 == 0:
                fizzString = fizzString + 'Buzz'
            if fizzString:
                fizzList.append(fizzString)
            else:
                fizzList.append(str(i))
        return fizzList
