# 868. Transpose Matrix

Given a matrix `A`, return the transpose of `A`.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

<br>

**Example 1:**

```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

**Example 2:**

```
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

 <br>

**Note:**

1. `1 <= A.length <= 1000`
2. `1 <= A[0].length <= 1000`

<br>

<br>

## Alogrithms

행렬 A가 주어졌을 때 전치시킨 값을 반환하는 문제이다.

전치시키려면 대각선을 기준으로 행과 열의 위치가 반대가 되어 입력되면 된다.

예를들어, 1행 2열 값은 2행 1열로 가고, 3행 2열 값은 2행 3열 값으로 가는 것이다.

문제를 쪼개보면,

1. 행렬 A를 입력 받는다.
2. 행렬 A의 길이를 파악한다.
3. 행렬 A의 길이만큼 행과 열의 위치를 바꾼다.



```javascript
var transpose = function(A) {
    let output = [];
    for(let i = 0; i < A[0].length ; i++) {
        output[i] = []
        for(let j = 0; j < A.length; j++ ) {          
            output[i][j] = A[j][i]
        }
    }
    return output;
};
```



```javascript
var transpose = function(A) {
    return A[0].map((val, ind) => A.map(row => row[ind]));
};

// val : 요소
// ind : index

```







```javascript
var transpose = function(A) {
    return A[0].map((val, ind) => A.map(row => row[ind]));
};


1) var transpose = function(A) {
};
A라는 배열을 매개변수로 넣고 그 결과를 tranpose로 참조한다.

2) var transpose = function(A) {
    return A[0].map();
};
A[0]의 map 함수를 사용해서 결과를 반환한다. 


/*
https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map

var array1 = [1, 4, 9, 16];

// pass a function to map
const map1 = array1.map(x => x * 2);

console.log(map1);
// expected output: Array [2, 8, 18, 32]

*/

3) var transpose = function(A) {
    return A[0].map((val, ind) =>    );
};

// A[0]에 들어있는 값이 val, ind에 입력으로 들어간다 [1, 0], [2, 1], [3, 2]
                    
                                  
4)
    var transpose = function(A) {
    return A[0].map((val, ind) => A.map(row => row[ind]));
};
```





### 학습한 내용

* `이중 for문`
* `Array`
* `map()` 메서드





