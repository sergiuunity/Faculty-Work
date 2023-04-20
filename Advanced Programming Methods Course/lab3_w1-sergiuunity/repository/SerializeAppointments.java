package repository;

import domain.Appointment;
import domain.Patient;

import java.io.*;
import java.util.HashMap;

public class SerializeAppointments {
    public static HashMap<String, Appointment> readAppointments(String path)
    {
        HashMap<String, Appointment> hashMap = new HashMap<String, Appointment>();
        try {
            ObjectInputStream in = new ObjectInputStream(new FileInputStream(path));
            hashMap = (HashMap<String, Appointment>) in.readObject();
            in.close();

        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
        return hashMap;
    }

    public static void writeAppointments(AppointmentsRepo givenAppointments, String path)
    {
        try {
            ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(path));
            HashMap<String, Appointment> hashMap = givenAppointments.getHashMap();
            out.writeObject(hashMap);
            out.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
