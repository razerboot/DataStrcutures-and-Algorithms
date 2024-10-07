package org.example;

public class LaserBeams {
    //example 1
    // 00
    // 11

    //example 2
    // 01
    // 10

    //example 3
    // 11
    // 01
    // 00
    // 10

    public int numberOfBeams(String[] bank) {
        int rows = bank.length;
        int numBeams = 0;
        int prevDevices = 0;
        for(int i = 0; i < rows; i++) {
            String row = bank[i];
            int devices = numberOfDevices(row);
            if(prevDevices != 0) {
               numBeams +=  devices * prevDevices;
            }
            if(devices != 0) {
                prevDevices = devices;
            }
        }
        return numBeams;
    }

    private int numberOfDevices(String row) {
        int numDevices = 0;
        for(int i = 0; i < row.length(); i++) {
            numDevices += row.charAt(i) == '1' ? 1 : 0;
        }
        return numDevices;
    }
}
