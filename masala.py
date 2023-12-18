class Solution(object):
    def romanToInt(self, s):
        mydict = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D":500,"M":1000}
        natija = 0
        for i in  range(len(s)):
            if i < len(s) - 1 and mydict[s[i]] < mydict[s[i+1]]:
                natija -= mydict[s[i]]
            else:
                natija += mydict[s[i]]
        return  natija