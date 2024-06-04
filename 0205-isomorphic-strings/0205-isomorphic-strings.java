class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s == null || t == null || s.length() != t.length())
            return false;

        int n = s.length();
        Map<Character, Character> mapping = new HashMap<>();
        Set<Character> mappedBefore = new HashSet<>();

        for (int i = 0; i < n; i++) {
            char c1 = s.charAt(i);
            char c2 = t.charAt(i);

            if (!mapping.containsKey(c1)) {
                if (mappedBefore.contains(c2))
                    return false;
                mapping.put(c1, c2);
                mappedBefore.add(c2);
            } else {
                if (mapping.get(c1) != c2)
                    return false;
            }
        }

        return true;
    }
}