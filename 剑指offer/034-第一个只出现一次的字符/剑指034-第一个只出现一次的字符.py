class Solution:
    #  用字典存储每个字符出现的次数，再从头遍历字符串，遇到第一个字典值为1的字符，返回其位置
    def FirstNotRepeatingChar(self, s):
        dict1 = {}
        for i in range(len(s)):
            if not dict1.__contains__(s[i]):
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
        for i in range(len(s)):
            if dict1[s[i]] == 1:
                return i
        return -1