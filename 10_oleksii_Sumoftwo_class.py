#Чесно кажучи підгледів в інеті - сам би не додумався так додавати )

class Solution(object):
    def getSum(self, a, b):
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)
		

a = int (input ('Input a  '))
b= int(input ('Input b  '))
c=Solution()
print('Sum is', c.getSum(a,b))
