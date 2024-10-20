package beakjoon.implement;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class J31797 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] command = br.readLine().split(" ");
        int n = Integer.parseInt(command[0]);
        int m = Integer.parseInt(command[1]);
        int max = m * 2;
        List<int[]> hands =  new ArrayList<>();
        for (int i = 1; i <= m; i++) {
            String[] hand = br.readLine().split(" ");
            hands.add(new int[]{i, Integer.parseInt(hand[0])});
            hands.add(new int[]{i, Integer.parseInt(hand[1])});
        }
        Collections.sort(hands, (a, b) -> a[1] - b[1]);
        int floor = n % max == 0 ? max : n % max;
        System.out.println(hands.get(floor - 1)[0]);
    }
}
