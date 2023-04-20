package domain;

import repository.AppointmentsRepo;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.Objects;

public class Patient implements Entity<String>/*, Comparable<Patient>*/{

    private String id;

    private String name;

    private String phoneNumber;

    private AppointmentsRepo appointments;

    public Patient(String id, String name, String phoneNumber, AppointmentsRepo appointments) {
        this.name = name;
        this.id = id;
        this.phoneNumber = phoneNumber;
        this.appointments = appointments;
    }

    public Patient(String id, String name, String phoneNumber) {
        this.name = name;
        this.id = id;
        this.phoneNumber = phoneNumber;
        this.appointments = new AppointmentsRepo();
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

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
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
        Patient patient = (Patient) o;
        return Objects.equals(name, patient.name) && Objects.equals(id, patient.id) && Objects.equals(phoneNumber, patient.phoneNumber) && Objects.equals(appointments, patient.appointments);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, id, phoneNumber, appointments);
    }

    @Override
    public String toString() {
        return "Patient{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                ", phoneNumber='" + phoneNumber + '\'' +
                ", appointments=" + appointments +
                '}';
    }

    public void addAppointment(String newAppointmentID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        LocalDateTime dateTime = LocalDateTime.of(newYear, newMonth, newDay, newHour, newMinute);
        Duration duration = Duration.of(newDuration, ChronoUnit.MINUTES);
        Appointment newAppointment = new Appointment(newAppointmentID, dateTime, duration);
        appointments.add(newAppointmentID, newAppointment);
    }

    public void addAppointment(Appointment newAppointment){
        appointments.add(newAppointment.getId(), newAppointment);
    }

    public void removeAppointment(String givenAppointmentID)
    {
        appointments.delete(givenAppointmentID);
    }

    public void modifyAppointment(String givenAppointmentID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        LocalDateTime dateTime = LocalDateTime.of(newYear, newMonth, newDay, newHour, newMinute);
        Duration duration = Duration.of(newDuration, ChronoUnit.MINUTES);
        Appointment newAppointment = new Appointment(givenAppointmentID, dateTime, duration);
        appointments.modify(givenAppointmentID, newAppointment);
    }

}
