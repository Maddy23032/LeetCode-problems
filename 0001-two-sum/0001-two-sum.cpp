class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> hm;
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            int sum=target-nums[i];
            if(hm.find(sum)!=hm.end()){
                res.push_back(hm[sum]);
                res.push_back(i);
                return res;
            }
            hm[nums[i]]=i;
        }
        return res;
    }
};