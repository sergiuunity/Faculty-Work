package domain;

import repository.AppointmentsRepo;
import repository.SerializePatients;

import java.io.*;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.HashMap;
import java.util.Objects;
import java.util.function.Consumer;

public class Patient implements Entity<String>, Serializable {

    private String id;

    private String name;

    private String phoneNumber;

    public Patient(String id, String name, String phoneNumber) {
        this.name = name;
        this.id = id;
        this.phoneNumber = phoneNumber;
    }

    public Patient() {
        this.name = "";
        this.id = "";
        this.phoneNumber = "";
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

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Patient patient = (Patient) o;
        return Objects.equals(name, patient.name) && Objects.equals(id, patient.id) && Objects.equals(phoneNumber, patient.phoneNumber);
    }

    @Override
    public String toString() {
        return "Patient(" +
                "name=" + name +
                ", phoneNumber=" + phoneNumber  +
                ')';
    }

    public void printPatient()
    {
        System.out.println(this.toString());
    }

    public boolean checkNameM()
    {
        return (new Character(this.getName().charAt(0)).equals((new Character('M'))));
    }

}