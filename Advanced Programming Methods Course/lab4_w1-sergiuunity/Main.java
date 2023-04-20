/*used resources to learn:
https://www.jetbrains.com/help/idea/db-tutorial-connecting-to-ms-sql-server.html#connect-by-using-sql-server-authentication-macos-and-linux

https://www.jetbrains.com/help/idea/configuring-database-connections.html

https://ubbcluj.sharepoint.com/sites/AdvancedProgrammingMethods/Class%20Materials/Lectures/Lecture_5.pdf?CT=1670419636349&OR=ItemsView

https://docs.oracle.com/javase/tutorial/jdbc/basics/processingsqlstatements.html

https://alvinalexander.com/java/edu/pj/jdbc/jdbc0002/
 */
import UI.UI;
import domain.Appointment;
import domain.Dentist;
import domain.Patient;
import repository.*;
import service.DentistService;

import java.io.*;
import java.sql.*;
import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Properties;
public class Main {

    //all the appointments for a certain patient
    //the phone number of a certain patient (given by id)
    //all the appointments on a certain date
    //all the appointments ordered by date
    //all the patients ordered alphabetically

    public static void main(String args[])
    {
        //dateTimes & durations
        LocalDateTime dateTime1 = LocalDateTime.of(2022, 11, 20, 14, 0);
        LocalDateTime dateTime2 = LocalDateTime.of(2023, 11, 20, 17, 0);
        LocalDateTime dateTime3 = LocalDateTime.of(2022, 11, 20, 12, 0);
        LocalDateTime dateTime4 = LocalDateTime.of(2022, 12, 5, 18, 0);
        LocalDateTime dateTime5 = LocalDateTime.of(2023, 1, 5, 9, 0);
        LocalDateTime dateTime6 = LocalDateTime.of(2023, 2, 2, 15, 0);
        Duration duration30 = Duration.of(30, ChronoUnit.MINUTES);
        Duration duration60 = Duration.of(60, ChronoUnit.MINUTES);
        Duration duration120 = Duration.of(120, ChronoUnit.MINUTES);

        //patients
        Patient p1 = new Patient("1", "Emilia Traian", "0723615106");
        Patient p2 = new Patient("2", "Rafael Daniel", "0744531013");
        Patient p3 = new Patient("3", "Natalia Miruna", "0768477915");
        Patient p4 = new Patient("4", "Paul Roman", "0722555281");
        Patient p5 = new Patient("5", "Monica Elena", "0723326856");

        //appointments
        Appointment ap1 = new Appointment("1", "1", dateTime1, duration120);
        Appointment ap2 = new Appointment("2", "1", dateTime2, duration30);
        Appointment ap3 = new Appointment("3", "2", dateTime3, duration60);
        Appointment ap4 = new Appointment("4", "3", dateTime4, duration120);
        Appointment ap5 = new Appointment("5", "4", dateTime5, duration60);
        Appointment ap6 = new Appointment("6", "5", dateTime6, duration30);

        //dentist
        PatientsRepo patientsRepo = new PatientsRepo();
        AppointmentsRepo appointmentsRepo = new AppointmentsRepo();
        Dentist dentist = new Dentist("1", "Dr. Andrei Pop", patientsRepo, appointmentsRepo);

        //adding patients to dentist
        dentist.addPatient(p1);
        dentist.addPatient(p2);
        dentist.addPatient(p3);
        dentist.addPatient(p4);
        dentist.addPatient(p5);

        //adding appointments to dentist
        dentist.addAppointment(ap1);
        dentist.addAppointment(ap2);
        dentist.addAppointment(ap3);
        dentist.addAppointment(ap4);
        dentist.addAppointment(ap5);
        dentist.addAppointment(ap6);

        //controller
        DentistService dentistService = new DentistService(dentist);

        //ui
        UI ui = new UI(dentistService);

        ui.start();

    }

}

