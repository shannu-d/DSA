class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;

        String str = "" + x;
        String rev = "";

        for (int i = str.length() - 1; i >= 0; i--) {
            rev = rev + str.charAt(i);
        }

     return str.equals(rev);
    }
}
