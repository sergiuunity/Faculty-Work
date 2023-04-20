package repository;

import domain.Patient;

import java.io.*;
import java.util.HashMap;

public class SerializePatients {
    public static HashMap<String, Patient> readPatients(String path)
    {
        HashMap<String, Patient> hashMap = new HashMap<String, Patient>();
        try {
            ObjectInputStream in = new ObjectInputStream(new FileInputStream(path));
            hashMap = (HashMap<String, Patient>) in.readObject();
            in.close();

        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
        return hashMap;
    }

    public static void writePatients(PatientsRepo givenPatients, String path)
    {
        try {
            ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(path));
            HashMap<String, Patient> hashMap = givenPatients.getHashMap();
            out.writeObject(hashMap);
            out.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
