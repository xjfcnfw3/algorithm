package beakjoon.implement;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class BJ10866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> deque = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            String[] command = br.readLine().split(" ");
            switch (command[0]) {
                case "push_back":
                    deque.addLast(Integer.parseInt(command[1]));
                    break;
                case "push_front":
                    deque.addFirst(Integer.parseInt(command[1]));
                    break;
                case "front":
                    if (deque.isEmpty()) sb.append("-1\n");
                    else sb.append(deque.getFirst()).append("\n");
                    break;
                case "back":
                    if (deque.isEmpty()) sb.append("-1\n");
                    else sb.append(deque.getLast()).append("\n");
                    break;
                case "size":
                    sb.append(deque.size()).append("\n");
                    break;
                case "pop_front":
                    if (deque.isEmpty()) sb.append("-1\n");
                    else sb.append(deque.poll()).append("\n");
                    break;
                case "pop_back":
                    if (deque.isEmpty()) sb.append("-1\n");
                    else sb.append(deque.pollLast()).append("\n");
                    break;
                case "empty":
                    if (deque.isEmpty()) sb.append("1\n");
                    else sb.append("0\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}
