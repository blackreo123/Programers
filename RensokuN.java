public class RensokuN {
    public static void main(String[] args) {
        int n = 15;
        int count = 0;
        for(int i = 1; i<n+1; i++){
            int a = 0;
            for(int j = i; j<n+1; j++){
                a = a+j;
                if(a == n){
                    
                    count++;
                }
            }
        }
        System.out.println(count);
    }
}
