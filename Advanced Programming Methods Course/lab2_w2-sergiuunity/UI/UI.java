package UI;

import service.DentistService;

import java.util.Scanner;

//dentist class, having repo with patients as field, and each patient has appointments as a field

//comparable appointments by time&date

//reports

//optional: nicer toString()'s

public class UI {

    private DentistService dentistService;

    public UI(DentistService dentistService) {
        this.dentistService = dentistService;
    }

    public void menu() {
        System.out.println("0.exit");
        System.out.println("1.menu");
        System.out.println("2.show dentist's details & patients");
        System.out.println("3.modify dentist's details");
        System.out.println("4.add a patient");
        System.out.println("5.show a patient's details & appointments");
        System.out.println("6.update a patient's details");
        System.out.println("7.remove a patient");
        System.out.println("8.add an appointment to a patient");
        System.out.println("9.cancel an appointment from an patient");
        System.out.println("10. modify an appointment from an patient");
    }

    public void start() {
        menu();
        while (true) {
            Scanner sc = new Scanner(System.in);
            System.out.println("command...");
                String command = sc.next();
                if (command.equals("0"))
                    break;
                else if (command.equals("1"))
                    menu();
                else if (command.equals("2")) {
                    System.out.println(dentistService.toString());
                } else if (command.equals("3")) {
                    try {
                        Scanner sc1 = new Scanner(System.in);
                        System.out.print("newName...");
                        String newName = sc1.next();
                        dentistService.modifyDentistDetails(newName);
                    } catch (RuntimeException re) {
                        System.out.println(re.getMessage());
                        System.out.println("Try new command.");
                    }
                } else if (command.equals("4")) {
                    try {
                        Scanner sc1 = new Scanner(System.in);
                        System.out.print("newPatientID...");
                        String newPatientID = sc1.next();
                        System.out.print("newName...");
                        String newName = sc1.next();
                        System.out.print("newPhoneNumber...");
                        String newPhoneNumber = sc1.next();
                        dentistService.addPatient(newPatientID, newName, newPhoneNumber);
                    } catch (RuntimeException re) {
                        System.out.println(re.getMessage());
                        System.out.println("Try new command.");
                    }

                } else if (command.equals("5")) {
                    try {
                        Scanner sc1 = new Scanner(System.in);
                        System.out.print("patientID...");
                        String givenPatientID = sc1.next();
                        System.out.println(dentistService.returnPatientDetailsString(givenPatientID));
                    } catch (RuntimeException re) {
                        System.out.println(re.getMessage());
                        System.out.println("Try new command.");
                    }

                } else if (command.equals("6")) {
                    try {
                        Scanner sc1 = new Scanner(System.in);
                        System.out.print("patientID...");
                        String givenPatientID = sc1.next();
                        System.out.print("newName...");
                        String newName = sc1.next();
                        System.out.print("newPhoneNumber...");
                        String newPhoneNumber = sc1.next();
                        dentistService.modifyPatient(givenPatientID, newName, newPhoneNumber);
                    } catch (RuntimeException re) {
                        System.out.println(re.getMessage());
                        System.out.println("Try new command.");
                    }
                } else if (command.equals("7")) {
                    try {
                        Scanner sc1 = new Scanner(System.in);
                        System.out.print("PatientID...");
                        String givenPatientID = sc1.next();
                        dentistService.removePatient(givenPatientID);
                    } catch (RuntimeException re) {
                        System.out.println(re.getMessage());
                        System.out.println("Try new command.");
                    }
                } else if (command.equals("8")) {
                    try {
                        Scanner sc1 = new Scanner(System.in);
                        System.out.print("patientID...");
                        String givenPatientID = sc1.next();
                        System.out.print("newAppointmentID...");
                        String newAppointmentID = sc1.next();
                        System.out.print("Year...");
                        Integer newYear = sc1.nextInt();
                        System.out.print("Month...");
                        Integer newMonth = sc1.nextInt();
                        System.out.print("Day...");
                        Integer newDay = sc1.nextInt();
                        System.out.print("Hour...");
                        Integer newHour = sc1.nextInt();
                        System.out.print("Minute...");
                        Integer newMinute = sc1.nextInt();
                        System.out.print("Duration(minutes)...");
                        Integer newDuration = sc1.nextInt();
                        dentistService.addAppointmentToPatient(givenPatientID, newAppointmentID, newYear, newMonth, newDay, newHour, newMinute, newDuration);
                    } catch (RuntimeException re) {
                        if (!(re.getMessage().equals("null"))) {
                            System.out.println(re.getMessage());
                        } else {
                            System.out.println("Invalid data type introduced.");
                        }
                        System.out.println("Try new command.");
                    }
                } else if (command.equals("9")) {
                    try {
                        Scanner sc1 = new Scanner(System.in);
                        System.out.print("patientID...");
                        String givenPatientID = sc1.next();
                        System.out.print("appointmentID...");
                        String givenAppointmentID = sc1.next();
                        dentistService.removeAppointmentFromPatient(givenPatientID, givenAppointmentID);
                    } catch (RuntimeException re) {
                        System.out.println(re.getMessage());
                        System.out.println("Try new command.");
                    }
                } else if (command.equals("10")) {
                    try {
                        Scanner sc1 = new Scanner(System.in);
                        System.out.print("patientID...");
                        String givenPatientID = sc1.next();
                        System.out.print("AppointmentID...");
                        String givenAppointmentID = sc1.next();
                        System.out.print("Year...");
                        Integer newYear = sc1.nextInt();
                        System.out.print("Month...");
                        Integer newMonth = sc1.nextInt();
                        System.out.print("Day...");
                        Integer newDay = sc1.nextInt();
                        System.out.print("Hour...");
                        Integer newHour = sc1.nextInt();
                        System.out.print("Minute...");
                        Integer newMinute = sc1.nextInt();
                        System.out.print("Duration(minutes)...");
                        Integer newDuration = sc1.nextInt();
                        dentistService.modifyAppointmentOfPatient(givenPatientID, givenAppointmentID, newYear, newMonth, newDay, newHour, newMinute, newDuration);
                    } catch (RuntimeException re) {
                        if (!(re.getMessage().equals("null"))) {
                            System.out.println(re.getMessage());
                        } else {
                            System.out.println("Invalid data type introduced.");
                        }
                        System.out.println("Try new command.");
                    }
                }
                else
                {
                    System.out.println("Invalid command introduced.");
                    System.out.println("Try new command.");
                }

            System.out.println("...exiting");
        }
    }
}
