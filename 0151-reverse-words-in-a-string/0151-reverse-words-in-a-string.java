class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        StringBuilder reverse = new StringBuilder();
        int end = s.length();

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') {
                reverse.append(s.substring(i + 1, end)).append(" ");
                while (i >= 0 && s.charAt(i) == ' ') i--; // Skip extra spaces
                end = i + 1;
            }
        }
        reverse.append(s.substring(0, end)); // Append the first word

        return reverse.toString();
    }
}
