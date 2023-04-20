package repository;

import domain.Appointment;
import domain.Patient;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.HashMap;
import java.util.Iterator;

public class JSONPatients {
    public static Patient objectToPatient(JSONObject fullObject)
    {
        JSONObject patientObject = (JSONObject)fullObject.get("patient");
        String ID = (String) patientObject.get("ID");
        String name = (String) patientObject.get("name");
        String phoneNumber = (String) patientObject.get("phoneNumber");
        Patient returnedPatient = new Patient(ID, name, phoneNumber);
        return returnedPatient;
    }

    public static HashMap<String, Patient> readPatients(String path)
    {
        HashMap<String, Patient> returnedPatients = new HashMap<String, Patient>();
        JSONParser jsonParser = new JSONParser();
        try {
            FileReader in = new FileReader(path);

            Object obj  = jsonParser.parse(in);
            JSONArray fullArray = (JSONArray) obj;

            for(int i = 0; i< fullArray.size(); i++)
            {
                Patient currentPatient = objectToPatient((JSONObject) fullArray.get(i));
                returnedPatients.put(currentPatient.getId(), currentPatient);
            }


            in.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }
        return returnedPatients;
    }

    public static void writePatients(PatientsRepo givenPatients, String path) {
        try {
            FileWriter out = new FileWriter(path);
            Iterator<Patient> it = givenPatients.getAll().iterator();
            JSONArray fullArray = new JSONArray();
            for (; it.hasNext(); ) {
                Patient element = (Patient) it.next();
                JSONObject currentObject = new JSONObject();
                currentObject.put("ID", element.getId());
                currentObject.put("name", element.getName());
                currentObject.put("phoneNumber", element.getPhoneNumber());
                JSONObject fullObject = new JSONObject();
                fullObject.put("patient", currentObject);
                fullArray.add(fullObject);
            }
            out.write(fullArray.toJSONString());
            out.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

}
