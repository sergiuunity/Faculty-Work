package main;

import domain.Appointment;
import domain.Dentist;
import domain.Patient;
import gui.DentistGUI;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import repository.*;
import service.DentistService;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.Properties;

public class Main extends Application {

    @Override
    public void start(Stage stage) throws IOException {
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

        DentistGUI dentistGUI = new DentistGUI(dentistService);

        FXMLLoader loader = new FXMLLoader(getClass().getResource("/gui/DentistGUI.fxml"));
        loader.setController(dentistGUI);
        Parent root = (Parent)loader.load();

        Scene scene = new Scene(root, 1280, 720);
        stage.setTitle("Dentist GUI");
        stage.setScene(scene);
        stage.show();
    }
}
