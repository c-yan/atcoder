import java.util.Scanner;

public class Main {
    static long A;
    static long B;
    static long X;

    static int getLength(long n) {
       return String.valueOf(n).length();
    }

    static boolean isOk(long N) {
        return A * N + B * getLength(N) <= X;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        A = sc.nextLong();
        B = sc.nextLong();
        X = sc.nextLong();

        if (isOk(1000000000)) {
            System.out.println(1000000000);
            return;
        }

        if (!isOk(1)) {
            System.out.println(0);
            return;
        }

        long N = 1000000000;
        while (!isOk(N)) {
            N /= 10;
        }

        long t = (X - B * getLength(N)) / A;
        if (t < N * 10 - 1) {
            System.out.println(t);
        } else {
            System.out.println(N * 10 - 1);
        }
    }
}
