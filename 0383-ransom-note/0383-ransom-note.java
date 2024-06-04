class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> map = new HashMap<>();
        int temp;
        for(int i=0; i<magazine.length(); i++){
            if(map.containsKey(magazine.charAt(i))){
                temp = map.get(magazine.charAt(i));
                map.put(magazine.charAt(i), temp+1);
            }
            else{
            map.put(magazine.charAt(i), 1);
            }
        }
        for(int i=0; i<ransomNote.length(); i++){
            if(!map.containsKey(ransomNote.charAt(i)) || map.get(ransomNote.charAt(i)) == 0) {

                return false;
            }
            else{
                temp = map.get(ransomNote.charAt(i));
                map.put(ransomNote.charAt(i), temp-1);
            }
        }
        return true;
    }
}