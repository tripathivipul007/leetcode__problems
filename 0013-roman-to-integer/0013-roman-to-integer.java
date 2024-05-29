class Solution {
    public int romanToInt(String s) {
         Map<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);

        int sum = 0;
        int prevValue = 0;

        // Process each character from the end of the string to the beginning
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            int currentValue = romanMap.get(c);

            // If the current value is less than the previous value, subtract it
            // Otherwise, add it
            if (currentValue < prevValue) {
                sum -= currentValue;
            } else {
                sum += currentValue;
            }

            // Update the previous value
            prevValue = currentValue;
        }

        return sum;
    }
}