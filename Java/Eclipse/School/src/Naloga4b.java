import java.util.Scanner;
public class Naloga4b{

     public static void main(String []args){
    	 Scanner input = new Scanner(System.in);
    	 System.out.print("Vnos: ");
    	 String a = input.next();
    	 String b="";
    	 for(int i = a.length()-1; i > 0; i--){
    		 b+=a.charAt(i);
    	 }
    	 System.out.print("izpis: "+b);
    	 input.close();
     }
}