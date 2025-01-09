class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, j = 0;
        int tmp;
        
        while (j < nums.size())
        {
            if (nums[j] == 0)
                j++;
            else
            {
                tmp = nums[j];
                nums[j] = nums[i];
                nums[i] = tmp;
                i++;
                j++;                
            }                 
        }
    }
