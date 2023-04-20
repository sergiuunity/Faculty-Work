package domain;

import repository.AppointmentsRepo;
import repository.PatientsRepo;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Dentist implements Entity<String> {

    private String id;

    private String name;

    private PatientsRepo patients;

    private AppointmentsRepo appointments;

    public Dentist(String id, String name, PatientsRepo patients, AppointmentsRepo appointments) {
        this.id = id;
        this.name = name;
        this.patients = patients;
        this.appointments = appointments;
    }

    @Override
    public String getId() {
        return id;
    }

    @Override
    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PatientsRepo getPatients() {
        return patients;
    }

    public void setPatients(PatientsRepo patients) {
        this.patients = patients;
    }

    public AppointmentsRepo getAppointments() {
        return appointments;
    }

    public void setAppointments(AppointmentsRepo appointments) {
        this.appointments = appointments;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Dentist dentist = (Dentist) o;
        return Objects.equals(id, dentist.id) && Objects.equals(name, dentist.name) && Objects.equals(patients, dentist.patients) && Objects.equals(appointments, dentist.appointments);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, name, patients, appointments);
    }

    @Override
    public String toString() {
        return "Dentist{" +
                "id=" + id +
                ", name=" + name + '\n' +
                "patients=" + patients + ";" + '\n' +
                "appointments=" + appointments + '}';
    }

    public void addPatient(String newPatientID, String newName, String newPhoneNumber){
        Patient givenPatient = new Patient(newPatientID, newName, newPhoneNumber);
        patients.add(newPatientID, givenPatient);
    }

    public void addPatient(Patient newPatient){
        patients.add(newPatient.getId(), newPatient);
    }

    public String returnPatientDetailsString(String givenPatientID)
    {
        return patients.findById(givenPatientID).toString();
    }

    public void modifyPatient(String givenPatientID, String newName, String newPhoneNumber)
    {
        Patient newPatient = new Patient(givenPatientID, newName, newPhoneNumber);
        patients.modify(givenPatientID, newPatient);
    }

    public void removePatient(String givenPatientID)
    {
        patients.delete(givenPatientID);
    }

    public void removePatient(Patient givenPatient){
        patients.delete(givenPatient.getId());
    }

    public void addAppointment(Appointment newAppointment)
    {
        appointments.add(newAppointment.getId(), newAppointment);
    }

    public void addAppointment(String newAppointmentID, String givenPatientID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        LocalDateTime dateTime = LocalDateTime.of(newYear, newMonth, newDay, newHour, newMinute);
        Duration duration = Duration.of(newDuration, ChronoUnit.MINUTES);
        Appointment newAppointment = new Appointment(newAppointmentID, givenPatientID, dateTime, duration);
        appointments.add(newAppointmentID, newAppointment);
    }

    public void removeAppointment(String givenAppointmentID)
    {
        appointments.delete(givenAppointmentID);
    }

    public void removeAppointment(Appointment givenAppointment){
        appointments.delete(givenAppointment.getId());
    }

    public void modifyAppointment(String givenAppointmentID, String newPatientID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        LocalDateTime dateTime = LocalDateTime.of(newYear, newMonth, newDay, newHour, newMinute);
        Duration duration = Duration.of(newDuration, ChronoUnit.MINUTES);
        Appointment newAppointment = new Appointment(givenAppointmentID, newPatientID, dateTime, duration);
        appointments.modify(givenAppointmentID, newAppointment);
    }

    public ArrayList<Appointment> appointmentsOfPatient(String givenID)
    {
        return appointments.appointmentsOfPatient(givenID);
    }

    public ArrayList<String> phoneNumberOfPatient(String givenID)
    {
        return patients.phoneNumberOfPatient(givenID);
    }

    public ArrayList<Appointment> appointmentsOnDate(String givenDate)
    {
        return appointments.appointmentsOnDate(givenDate);
    }

    public ArrayList<Appointment> appointmentsOrderedByDate()
    {
        return appointments.appointmentsOrderedByDate();
    }

    public ArrayList<Patient> patientsOrderedAlphabetically()
    {
        return patients.patientsOrderedAlphabetically();
    }

    public Patient getPatientAtID(String givenID)
    {
        return patients.findById(givenID);
    }

    public Appointment getAppointmentAtID(String givenID)
    {
        return appointments.findById(givenID);
    }

}
