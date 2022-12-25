import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        sc.close();
        /* Enter your code here. Print output to STDOUT. */
        String rev = "";
        char c;
        
        for (int i = 0; i < A.length(); i++ ) {
            c = A.charAt(i);
            rev = c+rev;
        }
        if (rev.equals(A)) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}