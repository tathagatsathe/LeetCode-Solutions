class Solution {
    public int rotatedDigits(int n) {
        int ans = 0;
        
        for (int i = 1; i <= n; i++) {
            String num = String.valueOf(i);
            boolean invalidDigitFound = false;
            boolean rotatingDigitFound = false;

            for (char digit : num.toCharArray()) {
                if (digit == '2' || digit == '5' || digit == '6' || digit == '9') {
                    rotatingDigitFound = true;
                } else if (digit == '3' || digit == '4' || digit == '7'){
                    invalidDigitFound = true;
                    break;
                }
            }
            if (rotatingDigitFound && !invalidDigitFound){
                ans+=1;
            }
        }
        return ans;
    }
}