class Solution {
    public int maximumGain(String s, int x, int y) {
        int maxgain=0;
        Stack<Character> st1=new Stack<>();
        String fp=x > y ? "ab" : "ba";
        int fs=Math.max(x,y);
        int ss=Math.min(x,y);
        for(int i=0;i<s.length();i++){
            if(!st1.isEmpty() && s.charAt(i)==fp.charAt(1) && st1.peek()==fp.charAt(0)){
                st1.pop();
                maxgain+=fs;
            }
            else{
                st1.push(s.charAt(i));
            }
        }
        StringBuilder sb=new StringBuilder();
        for(char c:st1){
            sb.append(c);
        }
        Stack<Character> st2=new Stack<>();
        for(char c:sb.toString().toCharArray()){
            if(!st2.isEmpty() && c==fp.charAt(0) && st2.peek()==fp.charAt(1)){
                st2.pop();
                maxgain+=ss;
            }
            else{
                st2.push(c);
            }
        }
        return maxgain;
    }
}