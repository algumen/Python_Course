class Solution(object):
    def fizzBuzz(self, n):
        record = []
        i = 1
        while i<= n:
           if i%3 ==0 and i%5 ==0:
               record.append('FizzBuzz')
               i+=1
           elif i%3 ==0 and i%5 !=0:
	           record.append('Fizz')
	           i+=1
           elif i%3 !=0 and i%5 ==0:
	           record.append('Buzz')
	           i+=1
           else:
               record.append(str(i))
               i+=1
        return record

n = int(input ('Input n  '))
c = Solution()
print (c.fizzBuzz(n))
