/*
 * @lc app=leetcode id=216 lang=java
 *
 * [216] Combination Sum III
 */

// @lc code=start
class Solution {
	List<List<Integer>> result = new ArrayList<>();
	LinkedList<Integer> path = new LinkedList<>();

	public List<List<Integer>> combinationSum3(int k, int n) {
		backTracking(n, k, 1, 0);
		return result;
	}

	private void backTracking(int targetSum, int k, int startIndex, int sum) {
		if (sum > targetSum) {
			return;
		}
		if (path.size() == k) {
			if (sum == targetSum) {
                result.add(new ArrayList<>(path));
            }
			return;
		}

        int right = 9 - (k - path.size()) + 1;
		for (int i = startIndex; i <= right; i++) {
			path.add(i);
			sum += i;
			backTracking(targetSum, k, i + 1, sum);
			path.removeLast();
			sum -= i;
		}
	}
}
// @lc code=end

