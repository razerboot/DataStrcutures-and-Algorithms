package org.example;

public class SentenceScreenFitting {

    public int wordsTyping(String[] sentence, int rows, int cols) {
        int m = sentence.length;

        int[] nextWord = new int[m];
        int[] endsFound = new int[m];

        for(int i = 0; i < m; i++) {

            String currWord = sentence[i];
            int currPos = i;
            int spacesAvailable = cols + 1;
            int spacesNeeded = currWord.length() + 1;
            int ends = 0;
            while (spacesNeeded <= spacesAvailable) {
                spacesAvailable -= spacesNeeded;
                if(currPos == m - 1) {
                    ends++;
                }
                currPos = (currPos + 1) % m;
                spacesNeeded = sentence[currPos].length() + 1;
            }
            nextWord[i] = currPos;
            endsFound[i] = ends;
        }

        int startWord = 0;
        int fittings = 0;
        for(int i =0; i<rows;i++) {
            fittings += endsFound[startWord];
            startWord = nextWord[startWord];
        }
        return fittings;
    }
}
