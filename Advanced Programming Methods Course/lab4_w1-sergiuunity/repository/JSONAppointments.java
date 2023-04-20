package repository;

import domain.Appointment;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.*;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.HashMap;
import java.util.Iterator;

public class JSONAppointments {

    public static Appointment objectToAppointment(JSONObject fullObject)
    {
        JSONObject appointmentObject = (JSONObject)fullObject.get("appointment");
        JSONObject dateTimeObject = (JSONObject) appointmentObject.get("dateTime");
        JSONObject durationObject = (JSONObject) appointmentObject.get("duration");
        String patientID = (String) appointmentObject.get("patientID");
        String ID = (String) appointmentObject.get("ID");
        int durationMinutes = ((Long) durationObject.get("minutes")).intValue();
        Duration duration = Duration.of(durationMinutes, ChronoUnit.MINUTES);
        int year = ((Long) dateTimeObject.get("year")).intValue();
        int month = ((Long) dateTimeObject.get("month")).intValue();
        int day = ((Long) dateTimeObject.get("day")).intValue();
        int hour = ((Long) dateTimeObject.get("hour")).intValue();
        int minute = ((Long) dateTimeObject.get("minute")).intValue();
        LocalDateTime dateTime = LocalDateTime.of(year, month, day, hour, minute);
        Appointment returnedAppointment = new Appointment(ID, patientID, dateTime, duration);
        return returnedAppointment;
    }

    public static HashMap<String, Appointment> readAppointments(String path)
    {
        HashMap<String, Appointment> returnedAppointments = new HashMap<String, Appointment>();
        JSONParser jsonParser = new JSONParser();
        try {
            FileReader in = new FileReader(path);

            Object obj  = jsonParser.parse(in);
            JSONArray fullArray = (JSONArray) obj;

            for(int i = 0; i< fullArray.size(); i++)
            {
                Appointment currentAppointment = objectToAppointment((JSONObject) fullArray.get(i));
                returnedAppointments.put(currentAppointment.getId(), currentAppointment);
            }


            in.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } catch (ParseException e) {
            throw new RuntimeException(e);
        }
        return returnedAppointments;
    }

    public static void writeAppointments(AppointmentsRepo givenAppointments, String path) {
        try {
            FileWriter out = new FileWriter(path);
            Iterator<Appointment> it = givenAppointments.getAll().iterator();
            JSONArray fullArray = new JSONArray();
            for (; it.hasNext(); ) {
                Appointment element = (Appointment) it.next();
                JSONObject dateObject = new JSONObject();
                JSONObject durationObject = new JSONObject();
                JSONObject currentObject = new JSONObject();
                dateObject.put("year", element.getDateTime().getYear());
                dateObject.put("month", element.getDateTime().getMonthValue());
                dateObject.put("day", element.getDateTime().getDayOfMonth());
                dateObject.put("hour", element.getDateTime().getHour());
                dateObject.put("minute", element.getDateTime().getMinute());
                durationObject.put("minutes", element.getDuration().toMinutes());
                currentObject.put("ID", element.getId());
                currentObject.put("patientID", element.getPatientId());
                currentObject.put("dateTime", dateObject);
                currentObject.put("duration", durationObject);
                //currentObject.put("duration", element.getDuration());
                //gotta format date and duration first then i can format them into the currentObject
                JSONObject fullObject = new JSONObject();
                fullObject.put("appointment", currentObject);
                fullArray.add(fullObject);
                //out.write(element.getId() + "; " + element.getPatientId() + "; " + element.getDateTime() + "; " + element.getDuration());
            }
            out.write(fullArray.toJSONString());
            out.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

}
