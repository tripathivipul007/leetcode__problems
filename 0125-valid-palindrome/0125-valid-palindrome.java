class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        int end = s.length();
        for(int i=0; i<end/2; i++){
            if(s.charAt(i) != s.charAt(end-1-i)){
                return false;
            }
            
        }
        return true;
    }
}