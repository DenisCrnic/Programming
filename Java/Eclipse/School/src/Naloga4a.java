import java.util.Scanner;
public class Naloga4a{

     public static void main(String []args){
    	 Scanner input = new Scanner(System.in);
    	 System.out.print("Vnos: ");
    	 int a = input.nextInt();
    	 String b="";
    	 while(a>0){
    		 b+=a%10;
    		 a/=10;
    	 }
    	 System.out.print("izpis: "+b);
    	 input.close();
     }
}