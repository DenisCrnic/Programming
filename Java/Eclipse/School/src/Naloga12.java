import java.util.Scanner;
public class Naloga12 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("Vnesite poved: ");
		StringBuffer b = new StringBuffer(input.nextLine());
		b.setCharAt(0, 'x');
		for(int i = 0; i < b.length(); i++){
			if(b.charAt(i)==' ')
				b.setCharAt(i+1, 'x');
		}
		System.out.print("Spremenjena poved: " + b);
		input.close();
	}
}