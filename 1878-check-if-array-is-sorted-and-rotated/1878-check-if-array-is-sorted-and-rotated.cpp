class Solution {
public:
    bool check(vector<int>& nums) {
        int ic=0;
        for(int i=1;i<nums.size();i++){
            if(nums[i]<nums[i-1]){
                ic++;
            }
        }
        if(nums[0]<nums[nums.size()-1]) ic++;
        return ic<=1;
    }
};