public class assignment_1 {

    public static void main(String args[])
    {
        for (int i=0;i<args.length;i++)
        {
            if (isPrime(Integer.parseInt(args[i])))
                System.out.println(Integer.parseInt(args[i]) + " ");
        }
    }
    public static boolean isPrime(int x)
    {
        if(x<2)
            return false;
        else
        {
            for(int j=2;j*j<=x;j++)
            {
                if(x%j==0)
                    return false;
            }
            return true;
        }
    }

}
