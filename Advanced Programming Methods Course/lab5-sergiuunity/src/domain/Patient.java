package domain;

import java.io.Serializable;
import java.util.Objects;

public class Patient implements Entity<String>,Serializable, Comparable<Patient>{

    private String id;

    private String name;

    private String phoneNumber;

    public Patient(String id, String name, String phoneNumber) {
        this.id = id;
        this.name = name;
        this.phoneNumber = phoneNumber;
    }

    public Patient() {
        this.id = "";
        this.name = "";
        this.phoneNumber = "";
    }


    @Override
    public String getId() {
        return id;
    }

    @Override
    public void setId(String id) {
        this.id=id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
//        return "Patient(" +
//                "name=" + name +
//                ", phoneNumber=" + phoneNumber  +
//                ')';
        return id + "\t" + name + "\t" + phoneNumber;
    }

    @Override
    public int compareTo(Patient other) {
        return this.getName().compareTo(other.getName());
    }

}