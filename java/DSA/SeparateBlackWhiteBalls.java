package org.example;

public class SeparateBlackWhiteBalls {

    // ex 1
    // 0 0 1

    // ex 2
    // 1 0

    // ex 3
    // 0 1 0 1 0

    public long minimumSteps(String s) {
        long numSteps = 0;
        int n = s.length();
        int blackBallsSeen = 0;
        for(int i = n - 1; i >= 0; i--) {
            if(s.charAt(i) == '1') {
                int desired = n - 1 - blackBallsSeen;
                int current = i;
                numSteps += desired - current;
                blackBallsSeen++;
            }
        }
        return numSteps;
    }
}
