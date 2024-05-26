class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int hIndex=0;
        int n = citations.length;
        for (int i = 0; i < n; i++) {
            int h = n - i; // Number of papers with at least `h` citations
            if (citations[i] >= h) {
                hIndex = h;
                break;
            }
        }

        return hIndex;
    }
}