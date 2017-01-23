class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return t.strip(s)
        
a = input ('Input a  ')
b= input('Input b  ')
c=Solution()
print('Difference is', c.findTheDifference(a,b))