public class assignment_4 {
    public static void main(String[] args)
    {
        System.out.println("gcd = "+gcd(Integer.parseInt(args[0]), Integer.parseInt(args[1])));
    }
    public static int gcd(int x, int y)
    {
        while(x!=y)
            if(x>y)
                x-=y;
            else
                y-=x;
        return x;
    }
}
