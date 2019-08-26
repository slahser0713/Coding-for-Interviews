class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        #  方法二，堆排序
        n = len(tinput)
        if k > n:
            return []
        def heap_sort(tinput):
            def heapify(root,end):
                lchild = root * 2 + 1
                rchild = root * 2 + 2
                if lchild > end:
                    return
                min = root
                if lchild <=  end and tinput[lchild] < tinput[min]:
                    min = lchild
                if rchild <= end and tinput[rchild] < tinput[min]:
                    min = rchild
                if min != root:
                    tinput[min],tinput[root] = tinput[root], tinput[min]
                    heapify(min,end)
            for i in range(n-2 // 2,-1,-1):
                heapify(i,n-1)
            res = []
            for j in range(1,k+1):
                res.append(tinput[0])
                tinput[0],tinput[-j] = tinput[-j],tinput[0]
                heapify(0,n-1-j)
            return res
        result = heap_sort(tinput)
        return result




