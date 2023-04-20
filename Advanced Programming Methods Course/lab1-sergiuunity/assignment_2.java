public class assignment_2 {
    public static void main(String args[])
    {
        if(args.length>0)
        {
            int max = Integer.parseInt(args[0]);
            for(int i=1;i<args.length;i++)
                if(Integer.parseInt(args[i])> max)
                    max = Integer.parseInt(args[i]);
            System.out.println("max = "+ max);
        }
        else
        {
            System.out.println("No command-line parameters were given");
        }
    }
}