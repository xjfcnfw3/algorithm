import java.util.*;
import java.lang.*;

class Solution {

    public String[][] bfs(String[][] arr, int row, int col, String container) {
        boolean[][] visited = new boolean[row][col];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];

            for (int[] move : new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1 ,0}}) {
                int nx = move[0] + x;
                int ny = move[1] + y;

                if (0 <= nx && 0 <= ny && nx < row && ny < col) {
                    if (!visited[nx][ny]) {
                        visited[nx][ny] = true;
                        if (arr[nx][ny] == null) {
                            queue.offer(new int[]{nx, ny});
                        } else if (arr[nx][ny].equals(container)) {
                            arr[nx][ny] = null;
                        }
                    }
                }
            }
        }

        return arr;
    }

    public int solution(String[] storage, String[] requests) {
        int row = storage.length + 2;
        int col = storage[0].length() + 2;
        int answer = 0;
        String[][] arr = new String[row][col];

        for (int i = 1; i < row - 1; i++) {
            String st = storage[i - 1];
            String[] row_char = st.split("");
            for (int j = 0; j < col - 2; j++) {
                arr[i][j + 1] = row_char[j];
            }
        }

        for (String request : requests) {
            String container = request.substring(0, 1);
            int command = request.length();
            if (command == 2) {
                for (int i = 1; i < row - 1; i++)
                    for (int j = 1; j < col - 1; j++) {
                        if (arr[i][j] != null && arr[i][j].equals(container)) {
                            arr[i][j] = null;
                        }
                    }
            } else {
                arr = bfs(arr, row, col, container);
            }
        }

        for (int i = 1; i < row - 1; i++) {
            for (int j = 1; j < col - 1; j++) {
                if (arr[i][j] != null) answer++;
            }
        }

        return answer;
    }
}