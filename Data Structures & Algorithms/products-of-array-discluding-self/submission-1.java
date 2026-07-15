class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] sol = new int[nums.length];
        sol[0] = 1;
        for(int i = 1; i < nums.length; i++){ // fill postfix
            sol[i] = sol[i - 1] * nums[i - 1];
        }

        int postFix = 1;
        for(int i = nums.length - 2; i >= 0; i--){ // multiply postfix by prefix
            postFix *= nums[i + 1];
            sol[i] *= postFix;
        }

        return sol;
    }
}  
