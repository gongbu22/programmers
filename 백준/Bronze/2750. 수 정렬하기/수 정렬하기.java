import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int[] arr = new int[num];
        
        for (int i=0; i<num; i++){
            int n = sc.nextInt();
            arr[i] = n;
        }
        
        Arrays.sort(arr);
        for (int n : arr) {
            System.out.println(n);
        }
        sc.close();
    }
}