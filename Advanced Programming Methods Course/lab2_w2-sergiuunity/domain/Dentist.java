package domain;

import repository.AppointmentsRepo;
import repository.PatientsRepo;

import java.util.Objects;

public class Dentist implements Entity<String> {

    private String id;

    private String name;

    private PatientsRepo patients;

    public Dentist(String id, String name, PatientsRepo patients) {
        this.name = name;
        this.id = id;
        this.patients = patients;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String getId() {
        return id;
    }

    @Override
    public void setId(String id) {
        this.id = id;
    }

    public PatientsRepo getPatients() {
        return patients;
    }

    public void setPatients(PatientsRepo patients) {
        this.patients = patients;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Dentist dentist = (Dentist) o;
        return Objects.equals(name, dentist.name) && Objects.equals(id, dentist.id) && Objects.equals(patients, dentist.patients);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, id, patients);
    }

    @Override
    public String toString() {
        return "Dentist{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", patients=" + patients +
                '}';
    }

    public void addPatient(String newPatientID, String newName, String newPhoneNumber){
        AppointmentsRepo appointmentsRepo = new AppointmentsRepo();
        Patient givenPatient = new Patient(newPatientID, newName, newPhoneNumber, appointmentsRepo);
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
        Patient newPatient = new Patient(givenPatientID, newName, newPhoneNumber, patients.findById(givenPatientID).getAppointments());
        patients.modify(givenPatientID, newPatient);
    }

    public void removePatient(String givenPatientID)
    {
        patients.delete(givenPatientID);
    }

    public void addAppointmentToPatient(String givenPatientID, String newAppointmentID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        patients.findById(givenPatientID).addAppointment(newAppointmentID, newYear, newMonth, newDay, newHour, newMinute, newDuration);
    }

    public void removeAppointmentFromPatient(String givenPatientID, String givenAppointmentID)
    {
        patients.findById(givenPatientID).removeAppointment(givenAppointmentID);
    }

    public void modifyAppointmentOfPatient(String givenPatientID, String givenAppointmentID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        patients.findById(givenPatientID).modifyAppointment(givenAppointmentID, newYear, newMonth, newDay, newHour, newDay, newDuration);
    }
}
