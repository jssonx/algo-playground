## Similar problems
 - binary-search
   - 1539, 1060

## Template
list -> string
```python
s = "".join(s_list)
```

isalpha() & isdigit()
```python
def isLetter(self, char):
        return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z')

char1 = 'a'
print(char1.isalpha())  # 输出 True
```

isPrime()
```python
def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
```
binary search
```python
def binarySearch(self, nums: List[int], target: int) -> int:
    left = -1
    right = len(nums)
    while left + 1 != right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    return -1

def binarySearch(self, nums: List[int], target: int) -> int:
    idx = bisect.bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1
```