# 238. Product of Array Except Self

Given an array nums of n integers where n > 1, 
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

> Input:  [1,2,3,4] 
>
>Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## 思路一
look like an easy problem, but we can't use division and need O(n).

Direct idea is to multiple one by one.

okay, let's see the standard solution.

We need to multiple the production fo left numbers and the production of right numbers.

1. new two list L and R. L[i] is the production of left and R[i] is right.
2. Two *for* are used to fill L and R. L[i] = L[i-1] * nums[i-1].
3. We can obtain L[i] * R[i] with iteration on input array.

# 思路二
L and R with can be calculated array because the output array does not count as extra space.
We calculate output array as L array then construct R dynamically to obtain the result.

1. 


## 复杂度分析
时间复杂度：O(n)

空间复杂度：O(n), use L and R array to construct the Solution1, the length of L and R is the length of nums.



