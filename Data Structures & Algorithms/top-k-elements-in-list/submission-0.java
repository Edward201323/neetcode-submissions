class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> count = new HashMap<>();
        for(int num : nums){
            if(!count.containsKey(num)){
                count.put(num, 1);
            } else {
                int currCount = count.get(num) + 1;
                count.put(num, currCount);
            }
        }

        List<Integer>[] freq = new ArrayList[nums.length + 1];
        for(int i = 0; i < freq.length; i++){
            freq[i] = new ArrayList<>();
        }

        for(Map.Entry<Integer, Integer> entry : count.entrySet()){
            int num = entry.getKey();
            int occurences = entry.getValue();
            freq[occurences].add(num);
        }

        int sol[] = new int[k];
        int solIndex = 0;
        int i = freq.length - 1;
        while(solIndex < k && i > 0){
            List<Integer> currArr = freq[i];
            int j = 0;
            while(!currArr.isEmpty() && j < currArr.size()){
                sol[solIndex] = currArr.get(j);
                solIndex++;
                j++;
            }
            i--;
        }

        return sol;
    }
}
