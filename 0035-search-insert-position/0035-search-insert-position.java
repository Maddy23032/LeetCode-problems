class Solution {
    public int searchInsert(int[] nums, int target) {
        int res=binSearch(nums,target);
        return res;
    }
    private int binSearch(int[] nums,int target){
        int l=0,r=nums.length-1;
        int m=(l+r)/2;
        while(l<=r){
            m=(l+r)/2;
            if(nums[m]==target){
                return m;
            }else if(nums[m]<target){
                l=m+1;
            }else{
                r=m-1;
            }
        }
        return l;
    }

}