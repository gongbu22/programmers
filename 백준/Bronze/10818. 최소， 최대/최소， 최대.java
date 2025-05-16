import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int num = sc.nextInt();
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        
        for (int i=0; i<num; i++){
            int n = sc.nextInt();
            if (n < min) min = n;
            if (n > max) max = n;
        }

        System.out.println(min + " " + max);
        sc.close();
    }
}