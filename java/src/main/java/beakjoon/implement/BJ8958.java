package beakjoon.implement;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ8958 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            int result = 0;
            int temp = 1;
            for (char c : str.toCharArray()) {
                if (c == 'O') result += temp++;
                else temp = 1;
            }
            System.out.println(result);
        }
    }
}
