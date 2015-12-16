import java.util.Scanner;
public class Naloga5b{
     public static void main(String []args){
    	 Scanner input = new Scanner(System.in);
    	 System.out.print("Vnos: ");
    	 String a = input.next(), b="";
    	 for(int i = a.length() - 1; i >= 0; i--)
    		 b+=a.charAt(i);
    	 if(a.equals(b)){
    		 System.out.println("Beseda je palindrom");
    	 }
    	 else{
    		 System.out.println("Beseda ni palindrom");
    	 input.close();
    	 }
     }
}