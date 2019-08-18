import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();

        int result = 0;
        for(int i = 1; i <= n; i++) {
            int sum = 0;
            int j = i;
            while (j != 0) {
              sum += j % 10;
              j /= 10;
            }
            if ((a <= sum) && (sum <= b)) {
                result += i;
            }
        }
        System.out.println(result);
    }
}
