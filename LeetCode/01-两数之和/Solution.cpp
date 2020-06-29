class Solution {

public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        map<int, int>hashmap;
        for (int i = 0; i < nums.size(); i++) {
            if (hashmap[target - nums[i]] && hashmap[target - nums[i]] != i + 1) {
                ans.push_back(i);
                ans.push_back(hashmap[target - nums[i]] - 1);
                return ans;
            }
        hashmap[nums[i]] = i + 1
        }
        return ans;
    }
};
