# Notes

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