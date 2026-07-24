class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int sol = 0;
        int prefLength = pref.length();
        for(string word : words){
            if(prefLength <= word.length() && word.substr(0, prefLength) == pref){
                sol++;
            }
        }
        return sol;
    }
};