# Notes

## DP问题
 - 每一轮的状态都是一样的。我们要找到当前轮的状态和上一轮的状态之间的关系。（提示：想想买卖股票问题）
 - 很多不是那么套路的DP题，DP状态可能比较难设计。不过还是有套路可循。某些题目给你一次“行使某种策略的权力”。联想到买卖股票系列的题，我们常会设计的两个状态就是“行使了权力”和“没有行使权力”分别对应的价值。

## 残酷DP勘误
冷冻期买卖股票
LC376 wiggle
276应该是265

## 198. House Robber
LC198
```python
# 0: 本轮我抢的最大收益
# 1: 本轮我不抢的最大收益
for k in range(1, n+1):
    dp[i][0] = dp[i-1][1] + nums[i]
    dp[i][1] = max(dp[i-1][0], dp[i-1][1])
res = max(dp[n][0], dp[n][1])
```

# Java

1002
```java
List<String> res = new ArrayList<>();
int[] hash = new int[26];
char c = (char) (i + 'a');
res.add(String.valueOf(c));
System.out.println(Arrays.toString(hash));
```

349
```java
Set<Integer> set = new HashSet<>();
System.out.println(set);
// Set<Integer> -> int[]
res.stream().mapToInt(i -> i).toArray();
// List<Integer> -> int[]
res.stream().mapToInt(i -> i).toArray();
```

383
```java
String ransomNote
for (char r : ransomNote.toCharArray()) {}
```

151
```
java String和char[] 如何互换？
使用 toCharArray() 和 new String(char[]) 方法可以在 Java 中将字符串和字符数组之间进行转换。
```

232
```java
Stack<Integer> stackIn;
stackIn = new Stack<>();
stackIn.push(x);
stackIn.pop();
stackIn.peek();
```

225
```java
Queue<Integer> queue;
queue = new LinkedList<>();
queue.poll(); // .pop()
queue.peek(); // .top()
queue.offer(x); // .push()
queue.size();
```

20
```java
Map<Character, Character> map = new HashMap<>();
map.put('(', ')');
map.put('[', ']');
map.put('{', '}');
```

1047
```java
Stack<Character> stk = new Stack<>();
String str = stk.toString();
str = str.replaceAll("\\[|\\]|,| ", "");
```
```java
class Solution {
    public String removeDuplicates(String s) {
        Deque<Character> dq = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (!dq.isEmpty() && dq.peekLast() == c) {
                dq.pollLast();
            } else {
                dq.offer(c);
            }
         }
        StringBuilder sb = new StringBuilder();
        for (char c : dq) { 
            sb.append(c);
        }
        return sb.toString();
    }
}
```

150
```java
String[] array = new String[] {"e1","e2","e3"};
for (String t: tokens) { 
    int x = Integer.parseInt(t)
}
```

347
```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int num : nums){
            map.put(num,map.getOrDefault(num, 0) + 1);
        }
        PriorityQueue<int[]> pq = new PriorityQueue<>((p1, p2) -> p2[1] - p1[1]);
        for(Map.Entry<Integer, Integer> pair : map.entrySet()){
            int[] singlePair =  new int[]{pair.getKey(), pair.getValue()};
            pq.add(singlePair);
        }
        int[] ans = new int[k];
        for(int i = 0; i < k; i++){
            ans[i] = pq.poll()[0];
        }
        return ans;
    }
}
```

266
```java
for (char key: map.keySet()) {
    int val = map.get(key);
}
```