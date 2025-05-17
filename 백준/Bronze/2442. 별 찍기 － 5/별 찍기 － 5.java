import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        
        for (int i=1; i<=num; i++){
            for (int j=num-1; j>=i; j--){
                System.out.print(" ");
            }
            for (int s=1; s<=i+(i-1); s++){
                System.out.print("*");
            }
            System.out.println();
        }
        sc.close();
    }
}