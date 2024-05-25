class Solution {
    public boolean canJump(int[] nums) {
        if (nums.length == 0) {
            return false;
        }

        int maxReach = 0;  // The farthest point that can be reached
        for (int i = 0; i < nums.length; i++) {
            if (i > maxReach) {
                return false;  // If current index is beyond the farthest point we can reach
            }
            maxReach = Math.max(maxReach, i + nums[i]);  // Update the farthest point
            if (maxReach >= nums.length - 1) {
                return true;  // If we can reach or go beyond the last index
            }
        }

        return false;  // If the loop ends without reaching the last index
    }
}
