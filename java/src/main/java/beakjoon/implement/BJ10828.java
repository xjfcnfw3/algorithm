package beakjoon.implement;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class BJ10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String[] command = br.readLine().split(" ");

            if (command[0].equals("push")) {
                stack.push(Integer.parseInt(command[1]));
            } else if (command[0].equals("top")) {
                if (stack.isEmpty()) {
                    sb.append("-1\n");
                    continue;
                }
                sb.append(stack.peek()).append("\n");
            } else if (command[0].equals("size")) {
                sb.append(stack.size()).append("\n");
            } else if (command[0].equals("empty")) {
                if (stack.isEmpty()) {
                    sb.append("1\n");
                    continue;
                }
                sb.append("0\n");
            } else {
                if (stack.isEmpty()) {
                    sb.append("-1\n");
                    continue;
                }
                sb.append(stack.pop()).append("\n");
            }
        }
        System.out.println(sb);
    }
}
