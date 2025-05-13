class Solution {
    public int myAtoi(String s) {
        int num = 1;
        int str_idx = -1;
        int end_idx = -1;
        String str = s.trim();
        String ans = "";
        boolean sign = false;
        for (int i=0; i<str.length(); i++) {
            char ch = str.charAt(i);
            boolean isDigit = Character.isDigit(ch);
            if(ch=='-' && !sign){
                // System.out.println("condition1");
                num = -1;
                sign = true;
                continue;
            }
            if(ch=='+' && !sign){
                // System.out.println("condition2");
                sign = true;
                continue;
            }
            if(!isDigit && ans==""){
                // System.out.println("condition3");
                return 0;
            }
            if(isDigit){
                sign = true;
                // System.out.println("condition4");
                ans+=ch;
            } else {
                // System.out.println("condition5");
                break;
            }
        }
        
        System.out.println(ans);
        if ( ans ==""){
            return 0;
        }
        int n = 1;
        try {
            n = Integer.parseInt(ans);
        } catch(NumberFormatException e) {
            n = Integer.MAX_VALUE;
            if(num==-1){
                n+=1;
            }
        }
        // if(n>Integer.MAX_VALUE) {
        //     return Integer.MAX_VALUE;
        // } else if (n<Integer.MIN_VALUE) {
        //     return Integer.MIN_VALUE;
        // }
        return n*num;
    }
}