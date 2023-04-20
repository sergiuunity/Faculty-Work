package ui;

import domain.ControlSoftware;
import domain.FlightControl;
import domain.Instrument;
import service.RepoService;

import java.util.Scanner;

public class UI {

    RepoService repoService;

    public UI(RepoService repoService) {
        this.repoService = repoService;
    }


    public void printMenu()
    {
        System.out.println("0-exit");
        System.out.println("1-show all");
        System.out.println("2-add new flight control");
        System.out.println("3-show all flight controls cheaper than");
        System.out.println("4-save to a text file with condition");
        System.out.println("menu");
        System.out.println("------------------------");
    }

    public void start(){
        printMenu();
        System.out.println("command...");
        Scanner sc = new Scanner(System.in);
        String command = sc.next();
        while(!(command.equals("0")))
        {
            if(command.equals("2"))
            {
                //read
                try
                {
                    System.out.println("controlType(controlSoftware/instrument):");
                    Scanner sc1 = new Scanner(System.in);
                    String controlType = sc.next();
                    if(controlType.equals("controlSoftware"))
                    {
                        System.out.println("code:");
                        String code = sc1.next();
                        System.out.println("maintenance(yes/no):");
                        String maintenance = sc1.next();
                        System.out.println("version:");
                        int version = sc1.nextInt();
                        boolean ok = true;
                        if(maintenance.equals("yes")) ok = true;
                        else if (maintenance.equals("no")) ok = false;
                        else throw new RuntimeException("Invalid input. Try a new command.");
                        ControlSoftware controlSoftware = new ControlSoftware(code, ok, version);
                        repoService.addControl(controlSoftware);

                    }
                    else if(controlType.equals("instrument"))
                    {
                        System.out.println("code:");
                        String code = sc1.next();
                        System.out.println("maintenance(yes/no):");
                        String maintenance = sc1.next();
                        System.out.println("measurementType:");
                        String measurementType = sc1.next();
                        boolean ok = true;
                        if(maintenance.equals("yes")) ok = true;
                        else if (maintenance.equals("no")) ok = false;
                        else throw new RuntimeException("Invalid input. Try a new command.");
                        Instrument instrument = new Instrument(code, ok, measurementType);
                        repoService.addControl(instrument);
                    }
                    else
                    {
                        System.out.println("No such type exists. Try a new command.");
                    }

                }
                catch (RuntimeException re)
                {
                    System.out.println(re);
                }
            }
            else if (command.equals("1"))
            {
                System.out.println(repoService.toString());
            }
            else if (command.equals("3"))
            {
                try
                {
                    System.out.println("cheaper than:");
                    Scanner sc1 = new Scanner(System.in);
                    double givenPrice = sc1.nextDouble();
                    repoService.showCheaper(givenPrice);
                }
                catch (RuntimeException re)
                {
                    System.out.println(re);
                }
            }
            else if (command.equals("4"))
            {
                String path = "example.txt";
                repoService.saveToFile(path);
            }
            else if (command.equals("menu"))
            {
                printMenu();
            }
            else
            {
                System.out.println("No such command exists. Try a new one.");
            }
            System.out.println("command...");
            command = sc.next();
        }
        System.out.println("exiting...");
    }
}
