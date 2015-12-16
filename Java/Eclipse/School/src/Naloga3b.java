import java.util.Scanner;
public class Naloga3b {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("Vnos besede: ");
		String a = input.next();
		System.out.print("Vnos črke: ");
		char c = input.next().charAt(0);
		int stevec=0;
		for(int i=a.indexOf(c); i<a.length(); i++)
			if(a.charAt(i)==c)
				stevec++;
		System.out.println("Izpis: "+stevec);
		input.close();
	}
}