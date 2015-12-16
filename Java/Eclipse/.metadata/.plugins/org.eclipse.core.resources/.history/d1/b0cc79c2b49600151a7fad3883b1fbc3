public class Naloga6{
     public static void main(String []args){
    	 int vsota = 0;
    	 int x = 0;
    	 int stevec = 0;
    	 double avg = 0.0;
    	 while(true){
    		 x = randomRange(-5, 5);
    		 if(x == 0){
    			 break;
    		 }else{
    			 System.out.print(x+" ");
    			 vsota+=x;
    		 }
    		 stevec++;
    	 }
    	 avg=vsota/stevec;
		 System.out.println(x);
    	 System.out.println("Vsota: "+vsota);
    	 System.out.println("Povprecje: "+avg);
     }
     
     public static int randomRange(int min, int max){
    	 return (int)(Math.random() * ((max - min) + 1)) + min;
     }
}