import java.util.Scanner;
public class test {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		String x = prepis("denis je najaci", 6, 10);
		System.out.print(x);
		input.close();
	}
	
	public static String prepis(String a, int from, int to){
		String b = "";
		for (int i = from; i < to; i++){
			b += a.charAt(i);
		}
		return b;
	}
}