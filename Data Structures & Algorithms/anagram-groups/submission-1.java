class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> sol = new HashMap<>();
        for(String str : strs){ 
            int[] curr = new int[26];
            for(char c : str.toCharArray()){
                int index = c - 'a';
                curr[index]++;
            }
            
            String key = Arrays.toString(curr);
            if(!sol.containsKey(key)){
                sol.put(key, new ArrayList<>());
            }
            sol.get(key).add(str);
        }

        return new ArrayList<>(sol.values());

    }
}
