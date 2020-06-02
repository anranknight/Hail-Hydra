# 1431. 拥有糖果最多的孩子
给你一个数组 candies 和一个整数 extraCandies ，其中 candies[i] 代表第 i 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 extraCandies 个糖果分配给孩子们之后，此孩子有 最多 的糖果。注意，允许有多个孩子同时拥有 最多 的糖果数目。


## 思路一
先求一个最大值，然后比较每个孩子本身的糖果数+额外的糖果数后是否不小于最大值

## 复杂度分析
max函数的复杂度是O(n)

## 总结与思考
留意一下这种用法，在一个list中处理单个数据

```ret = [candy + extraCandies >= maxCandies for candy in candies]```
