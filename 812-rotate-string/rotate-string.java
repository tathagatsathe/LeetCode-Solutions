class Solution {
    public boolean rotateString(String s, String goal) {
        int goalLength = goal.length();
        int n = s.length();

        if (n == goalLength) {
            for (int i = 0; i<goalLength; i++) {
                if (goal.charAt(i) == s.charAt(0)) {
                    int j = 0;
                    while (j < n && (i+j)%goalLength < goalLength) {
                        if (goal.charAt((i+j)%goalLength) != s.charAt(j)) {
                            break;
                        }
                        j++;
                    }
                    if (j==n) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}