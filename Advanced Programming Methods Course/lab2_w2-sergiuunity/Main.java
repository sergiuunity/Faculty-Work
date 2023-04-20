import UI.UI;
import domain.Appointment;
import domain.Dentist;
import domain.Patient;
import repository.AppointmentsRepo;
import repository.PatientsRepo;
import service.DentistService;

import java.time.temporal.ChronoUnit;
import java.time.temporal.TemporalUnit;
import java.util.Iterator;


import java.time.*;

public class Main {

    public static void main(String args[])
    {
        //dateTimes & durations
        LocalDateTime dateTime1 = LocalDateTime.of(2022, 11, 20, 14, 0);
        LocalDateTime dateTime2 = LocalDateTime.of(2023, 11, 20, 17, 0);
        LocalDateTime dateTime3 = LocalDateTime.of(2022, 11, 21, 12, 0);
        LocalDateTime dateTime4 = LocalDateTime.of(2022, 12, 5, 18, 0);
        LocalDateTime dateTime5 = LocalDateTime.of(2023, 1, 5, 9, 0);
        LocalDateTime dateTime6 = LocalDateTime.of(2023, 2, 2, 15, 0);
        Duration duration30 = Duration.of(30, ChronoUnit.MINUTES);
        Duration duration60 = Duration.of(60, ChronoUnit.MINUTES);
        Duration duration120 = Duration.of(120, ChronoUnit.MINUTES);

        //appointments
        Appointment ap1 = new Appointment("1", dateTime1, duration120);
        Appointment ap2 = new Appointment("2", dateTime2, duration30);
        Appointment ap3 = new Appointment("3", dateTime3, duration60);
        Appointment ap4 = new Appointment("4", dateTime4, duration120);
        Appointment ap5 = new Appointment("5", dateTime5, duration60);
        Appointment ap6 = new Appointment("6", dateTime6, duration30);

        //patients
        AppointmentsRepo apRe = new AppointmentsRepo();
        Patient p1 = new Patient("1", "Emilia Traian", "0723615106");
        Patient p2 = new Patient("2", "Rafael Daniel", "0744531013");
        Patient p3 = new Patient("3", "Natalia Miruna", "0768477915");
        Patient p4 = new Patient("4", "Paul Roman", "0722555281");
        Patient p5 = new Patient("5", "Monica Elena", "0723326856");

        //adding appointments to patients
        p1.addAppointment(ap1);
        p1.addAppointment(ap2);
        p2.addAppointment(ap3);
        p3.addAppointment(ap4);
        p4.addAppointment(ap5);
        p5.addAppointment(ap6);

        //dentist
        PatientsRepo patientsRepo = new PatientsRepo();
        Dentist dentist = new Dentist("1", "Dr. Andrei Pop", patientsRepo);

        //adding patients to dentist
        dentist.addPatient(p1);
        dentist.addPatient(p2);
        dentist.addPatient(p3);
        dentist.addPatient(p4);
        dentist.addPatient(p5);

        //controller
        DentistService dentistService = new DentistService(dentist);

        //ui
        UI ui = new UI(dentistService);


        ui.start();
    }

}

