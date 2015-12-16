import java.util.Scanner;
public class Naloga9 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.print("Vnos prve besede: ");
		String a = input.nextLine();
		System.out.print("Vnos druge besede: ");
		String b = input.nextLine();
		
		int samoglasnikA = steviloSamoglasnikov(a);
		int samoglasnikB = steviloSamoglasnikov(b);
		
		if(samoglasnikA != samoglasnikB)
			if(samoglasnikA > samoglasnikB){
				System.out.println("Prva beseda ima več samoglasnikov kot druga");
				System.out.println("Niz ki ima več samoglasnikov " + (jePalindrom(a) ?
						"je palindrom" : "ni palindrom"));
			}else{
				System.out.println("Prva beseda ima manj samoglasnikov kot druga");
				System.out.println("Niz ki ima več samoglasnikov " + (jePalindrom(b) ?
						"je palindrom" : "ni palindrom"));
			}
		else
			System.out.println("Besedi imata enako stevilo samoglasnikov");
		input.close();
	}
	
	public static int steviloSamoglasnikov(String a){
		int st=0;
		char[] samoglasniki = {'a', 'e', 'i', 'o', 'u'};
		for(int i = 0; i < a.length(); i++){
			for(int j = 0; j < samoglasniki.length; j++){
				if(a.charAt(i) == samoglasniki[j]){
					st++;
				}
			}
		}
		return st;
	}
	public static boolean jePalindrom(String a){
		String b = "";
		for(int i = a.length() - 1; i >= 0; i--){
			b += a.charAt(i);
		}
		if (b.equals(a)){
			return true;
		}else{
			return false;
		}
	}
}