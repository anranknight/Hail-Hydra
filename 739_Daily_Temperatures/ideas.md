# 739. Daily Temperatures
Given a list of daily temperatures T, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. 
Each temperature will be an integer in the range [30, 100].

## 思路一
最直观的想法就是每个位置都进行一次遍历，但是超时了。

## 思路二
借助栈来解决（栈是在栈顶操作，后进先出-LIFO）。递减栈：栈中只有递减元素。
放进去当前值，拿下一个数，比较其和栈顶的大小，如果小于则放进去，如果大于则求index差。
依次执行最终全部数据都搞定。