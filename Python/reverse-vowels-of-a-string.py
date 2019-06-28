class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = list('aeiou')
        s = list(s)
        vlist = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                vlist.append(i)
        print(vlist)
        for j in range(len(vlist)//2):
            s[vlist[j]],s[vlist[-j-1]] = s[vlist[-j-1]], s[vlist[j]]
        return "".join(s)
