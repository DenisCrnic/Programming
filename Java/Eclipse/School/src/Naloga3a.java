public class Naloga3a{

     public static void main(String []args){
        String a="allahuakhbar";
        int stevec=0;
        int b=0;
        for(int i=0;i<a.length();i++){
            if(a.indexOf('a',b)==(-1))
                break;
            else{
                stevec++;
                b=a.indexOf('a',b)+1;
            }
        }
        System.out.println(stevec);
        
     }
}