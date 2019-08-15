class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        count_space = 0
        for i in s:
            if i == " ":
                count_space += 1
        len_s = len(s)
        len_s += 2*count_space#替换成%20后多了2倍空格的字符
        new_list = [" "]*len_s
        j = 0
        for i in range(len(s)):#遍历原字符串
            if s[i] == " ":#遇到空格，在新列表中一次加入%20，下标前进3
                new_list[j] = "%"
                new_list[j+1] = "2"
                new_list[j+2] = "0"
                j += 3
            else:
                new_list[j] = s[i]#不是空格时，在新列表的当前下标添加字符串的非空格字符
                j += 1
        return "".join(new_list)

if __name__ ==  "__main__":
    A = Solution()
    SS = A.replaceSpace("dsa wd wqw wd")
    print(SS)
