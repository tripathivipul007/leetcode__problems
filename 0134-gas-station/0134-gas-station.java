class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total_tank = 0;
        int curr_tank = 0;
        int starting_station = 0;
        
        for (int i = 0; i < gas.length; i++) {
            total_tank += gas[i] - cost[i];
            curr_tank += gas[i] - cost[i];
            
            // If curr_tank is negative, it means we cannot proceed from the current starting station
            if (curr_tank < 0) {
                // Move the starting station to the next station
                starting_station = i + 1;
                // Reset curr_tank
                curr_tank = 0;
            }
        }
        
        // If total gas is greater than or equal to total cost, there is a valid starting station
        return total_tank >= 0 ? starting_station : -1;
    }
}