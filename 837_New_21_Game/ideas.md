# 837. New 21 Game 
Alice plays the following game, 
loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  
During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  
Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  
What is the probability that she has N or less points?

input is N, K,W

# 思路一
得分少于K时抽取，抽的是区间[1, W]的整数，在得分等于K或大于K时抽取。得分不大于N的概率 (p)。

得分必然小于K，抽第一张牌，得分不大于N的概率
- N <= W, p = N/W
- N > W, p = 1 

如果得分大于等于K，return p；否则抽第二张牌，得分不大于N的概率（两数之和不大于N的概率）
- N <= W, p = N/W
- N > W, p = 1 
...

# 思路二（动态规划）
dp[x] denote the winning probability when the game start from the score of x.

The target is to calculate dp[0].

when K <= x <= min(N, K+W-1), dp[x] = 1，where K+W-1 is the max score can obtain

when x > min(N, K+W-1), dp[x] = 0

so how to calculate dp[x] when 0 <= x < K?
It can been seen that the probability of each integer is equal every time draw an integer in [1, W], so:
```
dp[x] = (dp[x+1]+dp[x+2]+...+dp[x+W])/W
```
