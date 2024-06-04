import java.util.HashMap;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        // Initialize a frequency map for characters in magazine
        HashMap<Character, Integer> freqMap = new HashMap<>();

        // Populate the frequency map
        for (char ch : magazine.toCharArray()) {
            freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
        }

        // Check if ransomNote can be constructed
        for (char ch : ransomNote.toCharArray()) {
            if (!freqMap.containsKey(ch) || freqMap.get(ch) == 0) {
                return false;
            }
            freqMap.put(ch, freqMap.get(ch) - 1);
        }

        return true;
    }
}
