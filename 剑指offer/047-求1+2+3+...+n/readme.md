### 题目描述

求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

### 思路

在python中，A and B如果A为True返回B,如果A为Faule返回A，这里递归到n = 0时，返回res = 0，完成累加