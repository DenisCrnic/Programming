import java.util.Scanner;
public class Naloga5a{
     public static void main(String []args){
    	 Scanner input = new Scanner(System.in);
    	 System.out.print("Vnos: ");
    	 String a = input.next();
    	 StringBuffer b = new StringBuffer(a);
    	 StringBuffer c = new StringBuffer(b);
    	 if(c.toString().equals(b.reverse().toString())){
    		 System.out.print("Beseda je palindrom");
    	 }else{
    		 System.out.print("Beseda ni palindrom");
    	 }
    	 input.close();
     }
}