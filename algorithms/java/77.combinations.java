/*
 * @lc app=leetcode id=77 lang=java
 *
 * [77] Combinations
 */

// @lc code=start
// for循环用来横向遍历，递归的过程是纵向遍历
class Solution {
    List<List<Integer>> result = new ArrayList<>();
    LinkedList<Integer> path = new LinkedList<>();
    public List<List<Integer>> combine(int n, int k) {
        combineHelper(n, k, 1);
        return result;
    }
    private void combineHelper(int n, int k, int startIndex){
        if (path.size() == k){
            result.add(new ArrayList<>(path));
            return;
        }
        int needed = k - path.size();
        int right = n - needed + 1;
        for (int i = startIndex; i <= right; i++){
            path.add(i);
            combineHelper(n, k, i + 1);
            path.removeLast();
        }
    }
}
// @lc code=end

