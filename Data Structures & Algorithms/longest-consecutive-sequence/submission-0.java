class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> values = new HashSet<>();
        for(int num : nums){
            values.add(num);
        }

        int longestStreak = 0;
        for(int num : nums){
            int streak = 1;
            int curr = num;
            while(values.contains(curr + 1) && !values.contains(num - 1)){
                streak++;
                curr++;
            }

            if(streak > longestStreak){
                longestStreak = streak;
            }
        }

        return longestStreak;
    }
}
