class Solution(object):
    def findTheDifference(self, s, t):
        ssort = ''.join(sorted(s))
        tsort = ''.join(sorted(t))
        diff_char = t[0]
        i=0
        while i<len(ssort):
           if ssort[i]!=tsort[i]:
               diff_char = tsort[i]
               i=len(ssort)
           elif i == len(ssort)-1:
               diff_char = tsort[i+1]
               i=i+1
           else:
                i=i+1
        return diff_char


s = input ('Input a  ')
t= input('Input b  ')
c=Solution()
print(c.findTheDifference(s,t))