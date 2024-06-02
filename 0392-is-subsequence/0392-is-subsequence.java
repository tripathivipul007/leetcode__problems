class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length()==0){
            return true;
        }
        int index =0;
        int i=0;
        while(i <t.length()  ){
            char c = s.charAt(index);
            if(t.charAt(i) == c && index == s.length()-1){
                return true;
            }
            else if(t.charAt(i) == c){
                i++;
                index++;
            }
            else if(t.charAt(i) != c){
                i++;
            }
        }
        return false;
    }
}