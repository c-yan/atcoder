import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int bisectLeft(int[] a, int key) {
        int idx = Arrays.binarySearch(a, key);
        if (idx < 0) {
            return -idx - 1;
        }
        while (a[idx] == key) {
            idx--;
        }
        idx++;
        return idx;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] L = new int[N];
        for (int i = 0; i < N; i++) {
            L[i] = sc.nextInt();
        }

        Arrays.sort(L);
        int result = 0;
        for (int i = 0; i < N - 2; i++) {
            for (int j = i + 1; j < N - 1; j++) {
                result += bisectLeft(L, L[i] + L[j]) - j - 1;
            }
        }
        System.out.println(result);
    }
}
