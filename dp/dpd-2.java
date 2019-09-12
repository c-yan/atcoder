import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int W = sc.nextInt();

        long[] dp = new long[W + 1];
        Arrays.fill(dp, -1);

        dp[0] = 0;
        int maxW = 0;
        for (int i = 0; i < N; i++) {
            int w = sc.nextInt();
            int v = sc.nextInt();
            for (int j = Math.min(maxW, W - w); j != -1; j--) {
                if (dp[j] == -1) continue;

                dp[j + w] = Math.max(dp[j + w], dp[j] + v);
                maxW = Math.max(maxW, j + w);
            }
        }

        System.out.println(Arrays.stream(dp).max().getAsLong());
    }
}
