package beakjoon.implement;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class J29718 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] command = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int n = command[0];
        int m = command[1];
        int[] arr = new int[m];

        for (int i = 0; i < n; i++) {
            int[] row = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            for (int j = 0; j < m; j++) {
                arr[j] += row[j];
            }
        }
        int a = Integer.parseInt(br.readLine());
        int temp = 0;
        int answer = 0;
        for (int i = 0; i < m; i++) {
            if (i < a - 1) temp += arr[i];
            else if (i == a - 1) {
                temp += arr[i];
                answer += temp;
            }
            else {
                temp += arr[i];
                temp -= arr[i - a];
                if (temp > answer) answer = temp;
            }
        }

        System.out.println(answer);
    }
}
