public class Naloga8{
	public static void main(String[] args){
		String stavek = args[0];
		char znak = args[1].charAt(0);
		int pojavitev = 0;
		int stevec = 0;
		while(stevec<stavek.length()){
			if(stavek.charAt(stevec) == znak){
				pojavitev++;
			}
			stevec++;
		}
		if(pojavitev == 0){
			System.out.println("Znak " + znak + " se v stavku \"" + stavek + "\" ne pojavi");
			stavek = stavek.substring(1, stavek.length()-1);
			System.out.println("Spremenjen stavek: " + stavek);
		}else
			System.out.println("Znak " + znak + " se v stavku \"" + stavek + "\" pojavi " + pojavitev + "x");
	}
}