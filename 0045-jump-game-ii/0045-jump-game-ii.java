class Solution {
    public int jump(int[] nums) {
        if(nums.length<=1){
            return 0;
        }
        
        int jumps = 0;  // Number of jumps taken
        int currentEnd = 0;  // The end of the range that can be reached with the current jump
        int farthest = 0;  // The farthest point that can be reached with the next jump

        for (int i = 0; i < nums.length - 1; i++) {
            // Update the farthest point that can be reached
            farthest = Math.max(farthest, i + nums[i]);

            // If we reach the end of the current jump range
            if (i == currentEnd) {
                jumps++;
                currentEnd = farthest;  // Move to the next jump range

                // If we can reach or exceed the last index, break early
                if (currentEnd >= nums.length - 1) {
                    break;
                }
            }
        }

        return jumps;
    }
}