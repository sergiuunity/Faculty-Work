package repository;

import domain.Patient;

import java.io.*;
import java.util.HashMap;
import java.util.Iterator;

//ID; NAME; PHONE_NUMBER
public class BufferedPatients
{
    public static HashMap<String, Patient> readPatients(String path)
    {
        HashMap<String, Patient> returnedPatients = new HashMap<String, Patient>();
        try {
            BufferedReader in = new BufferedReader(new FileReader(path));
            String line = null;
            while ((line = in.readLine()) != null)
            {
                String[] parts = line.split("; ");
                if (parts.length < 3)
                    continue;
                Patient currentPatient = new Patient(parts[0], parts[1], parts[2]);
                returnedPatients.put(parts[0], currentPatient);
            }
            in.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return returnedPatients;
    }

    public static void writePatients(PatientsRepo givenPatients, String path)
    {

        try {
            BufferedWriter out = new BufferedWriter(new FileWriter(path));
            Iterator<Patient> it = givenPatients.getAll().iterator();
            for(;it.hasNext();)
            {
                Patient element = (Patient)it.next();
                out.write(element.getId() + "; " + element.getName() + "; " + element.getPhoneNumber());
                out.newLine();
            }
            out.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }



}