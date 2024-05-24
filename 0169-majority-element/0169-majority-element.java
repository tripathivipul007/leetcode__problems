class Solution {
    public int majorityElement(int[] nums) {
        int candidate = 0;
        int count = 0;

        // Phase 1: Find a candidate
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        // Phase 2: Verify the candidate (optional)
        count = 0;
        for (int num : nums) {
            if (num == candidate) {
                count++;
            }
        }

        if (count > nums.length / 2) {
            return candidate;
        } else {
            // Ideally, we should never reach here given the problem constraints
            // that guarantee a majority element.
            throw new IllegalArgumentException("No majority element found");
        }
    }

    
}
