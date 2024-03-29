---
date: 2018-04-09
title: "[Algorithms] 807.Max Increase to Keep City Skyline"
excerpt: "LeetCode #807, medium"
categories: algorithms
comments: true
---



 ### 807.Max Increase to Keep City Skyline

#### 문제

> In a 2 dimensional array `grid`, each value `grid[i][j]` represents the height of a building located there. 
>
> 2차원 배열 그리드(grid)에서, 각각의 `grid[i][j]` 값은 그곳에 위치한 건물의 높이를 나타낸다.
>
> We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 
>
> 우리는 임의의 수의 건물 높이를 어느정도 증가시킬 수 있다(정도는 건물마다 다를 수 있다). 일반적으로 높이가 0인 건물도 건물이다.
>
> At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.
>
> 마지막으로, 그리드의 4 가지 방향 (위, 아래, 왼쪽, 오른쪽)에서 보았을 때의 "스카이 라인"은 원래 그리드의 스카이 라인과 동일해야한다. 도시의 스카이 라인은 거리를 두고 볼 때 모든 건물에 의해 형성되는 사각형의 외곽선이다. 다음 예를 참조하라.
>
> What is the maximum total sum that the height of the buildings can be increased?
>
> 건물의 높이를 올릴 수있는 최대 합계는 얼마인가?
>
> 
>
> ```
> Example:
> Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
> Output: 35
> Explanation: 
> The grid is:
> [ [3, 0, 8, 4], 
>   [2, 4, 5, 7],
>   [9, 2, 6, 3],
>   [0, 3, 1, 0] ]
>
> The skyline viewed from top or bottom is: [9, 4, 8, 7]
> The skyline viewed from left or right is: [8, 7, 9, 3]
>
> The grid after increasing the height of buildings without affecting skylines is:
>
> gridNew = [ [8, 4, 8, 7],
>             [7, 4, 7, 7],
>             [9, 4, 8, 7],
>             [3, 3, 3, 3] ]
> ```
>
> **Notes:**
>
> - `1 < grid.length = grid[0].length <= 50`.
> - All heights `grid[i][j]` are in the range `[0, 100]`.
> - All buildings in `grid[i][j]` occupy the entire grid cell: that is, they are a `1 x 1 x grid[i][j]` rectangular prism.



#### 접근

 주어진 Example을 그림으로 그려서 문제를 파악해보았다.

 2차원 배열이 Example과 같이 주어져 있을 때, 위, 아래, 왼쪽, 오른쪽에서 살펴 본 후 가장 큰 값이 스카이라인이다. 즉, 노란화살표는 열(column) 기준으로 바라봤을 때 최댓값이고, 파란 화살표는 행(row) 기준으로 봤을 때 최댓값인 것이다.

 아래 그림을 참고하여 열 기준으로 최댓값을 찾아보면 1열은 9, 2열은 4, 3열은 8, 4열은 7이 된다. 행을 기준으로 최댓값을 찾아보면 1행은 8, 2행은 7, 3행은 9, 4행은 3이다.

 ![](https://raw.githubusercontent.com/lovesignal/lovesignal.github.io/master/img/post/Algorithms/Leetcode807_algorithm1.png)

 다음은 스카이 라인에 영향을 미치지 않고 건물 높이를 증가시킨 후의 그리드를 찾는다. 찾는 방법을 생각해보면 먼저 기준되는 값에서 행과 열을 살펴봤을 때 앞서 구한 행과 열의 max값 중 자기 자신보다는 크고 max값 중 작은 값까지 스카이라인을 올릴 수 있다.

 아래 그림을 살펴보면, 3을 기준으로 했을 때 행(row)에는 8, 열(column)에는 9가 스카이라인이다. 8과 9 중 작은 값까지는 스카이라인을 올릴 수 있다. 그렇게 해야 열에서 봤을 때, 행에서 봤을 때 모두 기존의 스카이라인을 넘어서지 않기 때문이다.



![](https://raw.githubusercontent.com/lovesignal/lovesignal.github.io/master/img/post/Algorithms/Leetcode807_algorithm2.png)



### 알고리즘 짜기

알고리즘을 세분화 시켜보면 주어진 2차원 array를 2차원 matrix 처럼 생각했을 때, 

1. 각 행의 최댓값을 구한다. **row_max(각각의 행)**

2. 각 열의 최댓값을 구한다. **col_max(각각의 열)**

3. 각 원소를 돌면서 해당 원소의 값을 행의 최댓값, 열의 최댓값 중 작은 값까지 올린다. **min(행의 최댓값, 열의 최댓값)**

4. 증가시킬 수 있는 최대 합계를 구하기 위해 새로 구한 그리드의 합에서 처음 주어진 그리드의 합을 뺀다.

   **sum(새로 증가시킨 그리드) - sum(처음 그리드 값)**



### Solution

```javascript
// javascript
const maxIncreaseKeepingSkyline = (grid) => {
    let rowMaxes = [];
    let colMaxes = [];
    
    // max each row
    grid.map(row => rowMaxes.push(Math.max(...row)));
    
    // transpose from stackoverflow
    const transposedGrid = grid[0].map((col, i) => grid.map(row => row[i]));
    // max each column
    transposedGrid.map(col => colMaxes.push(Math.max(...col)));
    
    // traverse grid => each cell raise till first max
    let sum = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            sum += Math.min(rowMaxes[i], colMaxes[j]) - grid[i][j];
        }
    }
    return sum;
};
```



```javascript
transpose = m => m[0].map((x,i) => m.map(x => x[i]))

var maxIncreaseKeepingSkyline = function(grid) {
    let rowMaxes = grid.map( row => Math.max(...row))
    let colMaxes = transpose(grid).map( row => Math.max(...row))
    
    let increase = 0;
    for(let i = 0; i < grid.length; i++) {
        for(let j = 0; j < grid[i].length; j++){
            let newTotal = Math.min(rowMaxes[i], colMaxes[j])
            increase += newTotal - grid[i][j];
        }
    }
    return increase
};
```



### Complexity Analysis

* Time Complexity

  $$O(n^2)$$

- Space Complexity: O(N), the space used by `row_maxes` and `col_maxes`.

