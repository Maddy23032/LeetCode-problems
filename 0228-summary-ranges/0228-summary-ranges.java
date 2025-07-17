class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> res=new ArrayList<>();
        if(nums.length==0) return res;
        int st=0;
        for(int i=1;i<nums.length;i++){
            if(nums[i]!=nums[i-1]+1){
                if(st!=i-1){
                    res.add(nums[st]+"->"+nums[i-1]);
                }else{
                    res.add(String.valueOf(nums[st]));
                }
                st=i;
            }
        }
        if(st==nums.length-1){
            res.add(String.valueOf(nums[st]));
        }
        else{
            res.add(nums[st]+"->"+nums[nums.length-1]);
        }
        return res;
    }
}