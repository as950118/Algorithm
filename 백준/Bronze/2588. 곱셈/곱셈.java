import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer var1 = sc.nextInt();
        Integer var2 = sc.nextInt();        
        System.out.println(var1 * (var2%10));
        System.out.println(var1 * (int) (var2%100/10));
        System.out.println(var1 * (int) (var2%1000/100));
        System.out.println(var1 * var2);
    }
}