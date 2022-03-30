# [Leetcode] 804. Unique Morse Code Words

## Description

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: `"a"`maps to `".-"`, `"b"` maps to `"-..."`, `"c"` maps to `"-.-."`, and so on.

>  국제 모스 부호는 다음과 같이 각 문자가 일련의 점과 대시에 매핑되는 표준 인코딩을 정의한다. 다음과 같이  `"a"` 는  `".-"` , `"b"` 는  `"-..."` , `"c"` 는  `"-.-."`  등으로 맵핑된다.

For convenience, the full table for the 26 letters of the English alphabet is given below:

>  편의상 영어 알파벳 26 자의 전체 표가 아래에 주어져 있다.

```
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
```



Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

> 이제 단어 목록이 주어지면 각 단어는 각 문자의 모스 부호를 연결 한 것으로 작성할 수 있다. 예를 들어, "cab"는 "-.- .- ....-"("-.-."+ "-..."+ ".-"을 연결한 것)로 작성 될 수 있다. 우리는 이러한 연결을 단어의 변환(the transformation of a word) 이라고 부를 것이다.

Return the number of different transformations among all words we have.

> 우리가 가지고 있는 모든 단어들 사이의 다른 변환의 수를 반환해라.



```
Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
```

 

**Note:**

- The length of `words` will be at most `100`.
- Each `words[i]` will have length in range `[1, 12]`.
- `words[i]` will only consist of lowercase letters.

> * 단어의 길이는 최대 100이다. 
> * 각 단어 [i]의 길이는 [1, 12] 이다.
> * words [i]는 소문자로만 구성된다.





## Idea

일단 모스부호와 알파벳을 일대일 대응 시켜서 변환해야 할 것 같다. 아스키코드값을 반환받아서 for문을 통해 일대일 변환 가능하다. 

Hash 구조로 만들어서 알파벳 문자의 해당 모스부호를 찾고 결합해준 후 비교한다.

Hash를 쓰려는 이유는 시간 복잡도가 낮아지기 때문이다.



## 구현























