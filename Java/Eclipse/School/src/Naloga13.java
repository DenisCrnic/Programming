import java.util.Scanner;
public class Naloga13 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		String s = input.nextLine();
		String[] y = {"pizda", "kurac", "fuck"};
		String censored = cenzura(s, y);
		System.out.print(censored);
		input.close();
	}
	
	public static String cenzura(String a, String tab[]){
		String[] vnos = a.split(" ");
		String cenzuriranStavek = "";
		
		for(int i = 0; i < vnos.length; i++){
			for(int j = 0; j < tab.length; j++){
				if(vnos[i].equals(tab[j])){
					vnos[i]=zamenjavaBesede(vnos[i]);
				}
			}
			cenzuriranStavek=cenzuriranStavek + vnos[i] + " ";
		}
		
		return cenzuriranStavek;
	}
	public static String zamenjavaBesede(String a){
		String b="";
		for(int i = 0; i < a.length(); i++){
			b+='*';
		}
		return b;
	}
}