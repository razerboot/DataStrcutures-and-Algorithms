package org.example;

public class ShiftingLetters {

    // ex 1
    // ab [1,1]
    //ab [2,1]
    //cc

    public String shiftingLetters(String s, int[] shifts) {
        int n = s.length();
        int[] suffixShifts = new int[n];

        suffixShifts[n-1] = shifts[n-1]%26;

        for(int i = n - 2; i >= 0; i--) {
            suffixShifts[i] = (suffixShifts[i + 1] + shifts[i]) % 26;
        }

        char[] charArray = new char[n];
        for(int i = 0; i < n; i++) {
            charArray[i] = (char) (97 + (s.charAt(i) - 97 + suffixShifts[i])%26);
        }
        return new String(charArray);
    }
}
