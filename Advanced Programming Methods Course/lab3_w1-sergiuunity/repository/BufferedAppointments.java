package repository;

import domain.Appointment;

import java.io.*;
import java.time.Duration;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Iterator;

//ID; PATIENT_ID; DATETIME; DURATION
public class BufferedAppointments {
    public static HashMap<String, Appointment> readAppointments(String path)
    {
        HashMap<String, Appointment> returnedAppointments = new HashMap<String, Appointment>();
        try {
            BufferedReader in = new BufferedReader(new FileReader(path));
            String line = null;
            while ((line = in.readLine()) != null)
            {
                String[] parts = line.split("; ");
                if (parts.length < 4)
                    continue;
                Appointment currentAppointment = new Appointment(parts[0], parts[1], LocalDateTime.parse(parts[2]), Duration.parse(parts[3]));
                returnedAppointments.put(parts[0], currentAppointment);
            }
            in.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return returnedAppointments;
    }

    public static void writeAppointments(AppointmentsRepo givenAppointments, String path)
    {

        try {
            BufferedWriter out = new BufferedWriter(new FileWriter(path));
            Iterator<Appointment> it = givenAppointments.getAll().iterator();
            for(;it.hasNext();)
            {
                Appointment element = (Appointment)it.next();
                out.write(element.getId() + "; " + element.getPatientId() + "; " + element.getDateTime() + "; " + element.getDuration());
                out.newLine();
            }
            out.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }
}
