import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int W = sc.nextInt();

        long[][] dp = new long[N + 1][W + 1];
        for (int i = 0; i <= N; i++) {
            Arrays.fill(dp[i], -1);
        }

        dp[0][0] = 0;
        for (int i = 0; i < N; i++) {
            int w = sc.nextInt();
            int v = sc.nextInt();
            for (int j = 0; j <= W; j++) {
                if (dp[i][j] == -1) {
                    continue;
                }
                dp[i + 1][j] = Math.max(dp[i + 1][j], dp[i][j]);
                if (j + w > W) {
                    continue;
                }
                dp[i + 1][j + w] = Math.max(dp[i + 1][j + w], dp[i][j] + v);
            }
        }

        System.out.println(Arrays.stream(dp[N]).max().getAsLong());
    }
}
