/*
 * @lc app=leetcode id=59 lang=java
 *
 * [59] Spiral Matrix II
 */

// @lc code=start
class Solution {
    public int[][] generateMatrix(int n) {
        int [][] res = new int[n][n];
        int loop = 0;
        int num = 1;
        int s = 0;
        int i, j;
        while (loop++ < n / 2) {
            for (j = s; j < n - loop; j++) {
                res[s][j] = num++;
            }
            for (i = s; i < n - loop; i++) {
                res[i][j] = num++;
            }
            for (; j >= loop; j--) {
                res[i][j] = num++;
            }
            for (; i >= loop; i--) {
                res[i][j] = num++;
            }
            s++;
        }
        if (n % 2 != 0) {
            res[s][s] = num;
        }
        return res;
    }
}
// @lc code=end

