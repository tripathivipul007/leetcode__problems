class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim();
        int i = s.length()-1;
        int counter = 0;
        while (i>=0 && s.charAt(i) !=' '){
            counter++;
            i--;
        }
        return counter;
    }
}