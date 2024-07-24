import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        double b[] = new double[a];
        double max = Double.MIN_VALUE;
        for(int i = 0; i<a; i++){
            b[i] = sc.nextDouble();
            if(b[i]>max){
                max = b[i];
            }   
        }
        double d = 0;
        for(int i = 0; i<a; i++){
            double c = (b[i]/max)*100;
            d+=c;
        }
        System.out.println(d/a);
    }
}