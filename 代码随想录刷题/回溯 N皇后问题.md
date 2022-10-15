# N皇后问题

## [leetcode 51](https://leetcode.cn/problems/n-queens/)

题目描述：

```
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

示例 1：


输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：[["Q"]]


```

### 思路
确定约束条件：

* 不能同行
* 不能同列
* 不能同斜线

可以考虑使用二维矩阵，矩阵当中的高就是树形结构的高，宽就是树形的宽

#### 回溯三部曲

* 确定递归函数的参数
```
vector<vector<string>> result;
void backtracking(int n,int row,vector<string>& chessboard)
```

* 确定递归终止条件
递归到叶子节点的时候，就可以收集结果并返回。

```
if (row==n){
    result.push_back(chessboard);
    return;
}
```


* 单层遍历
递归深度就是row控制棋盘行数，for循环每一行用col记录

```
for (int col = 0;col < n ; col++){
    if (isValid(row,col,chessboard, n)){
        chessboard[row][col] = 'Q'; //放置，皇后
        backtracking(n, row + 1,chessboard);
        chessboard[row][col] = '.'; //回溯，撤销皇后
    }
}
```

* 根据约束条件验证棋牌合法性

```
bool isValid(int row,int col, vector<string>& chessboard,int n)
{
    int count = 0;
    //检查列
    for (int i = 0;i < row;i++)
    {
        if (chessboard[i][col] == 'Q')
        {
            return false;
        }
    }
    //检查45°角直线上是否有皇后
    for (int i = row - 1,j = col - 1; i>=0 && j >= 0;i--,j--)
    {
        if (chessboard[i][j] == 'Q'){
            return false;
        }
    }
    //检查135°角直线上是否有皇后
    for (int i = row - 1,j = col + 1; i>=0 && j < n;i--,j++)
    {
        if (chessboard[i][j] == 'Q'){
            return false;
        }
    }
    return true;
}
```