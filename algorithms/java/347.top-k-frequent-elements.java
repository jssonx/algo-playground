/*
 * @lc app=leetcode id=347 lang=java
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
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
// @lc code=end

