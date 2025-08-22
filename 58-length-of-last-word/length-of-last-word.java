class Solution {
    public int lengthOfLastWord(String s) {
        String [] words =  s.split(" ");
        String lword = words[ words.length - 1 ];
        return lword.length();
    }
}