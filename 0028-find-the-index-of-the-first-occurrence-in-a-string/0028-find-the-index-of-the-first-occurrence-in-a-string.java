class Solution {
    public int strStr(String haystack, String needle) {
        int hayLen = haystack.length();
        int needleLen = needle.length();
        
        // Edge cases
        if (needleLen == 0) return 0;
        if (hayLen < needleLen) return -1;
        
        for (int i = 0; i <= hayLen - needleLen; i++) {
            if (haystack.substring(i, i + needleLen).equals(needle)) {
                return i;
            }
        }
        
        return -1;
    }
}
