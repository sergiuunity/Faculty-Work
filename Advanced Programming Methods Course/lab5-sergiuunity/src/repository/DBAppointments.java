package repository;

import domain.Appointment;
import domain.Patient;
import repository.AppointmentsRepo;

import java.sql.*;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.HashMap;
import java.util.Iterator;

public class DBAppointments {
    public static void exportToDB(String database, String table, AppointmentsRepo appointmentsRepo, String dentistID)
    {
        String url = "jdbc:sqlserver://localhost;database=".concat(database).concat(";trustServerCertificate=true");
        String username = "sa";
        String password = "paroladeSmecher/5";

        try {
            Connection connection = DriverManager.getConnection(url,username, password);
            Statement statement = connection.createStatement();

            //delete content
            String currentQuery = "DELETE FROM " + table;
            statement.executeUpdate(currentQuery);

            //export
            Iterator<Appointment> it = appointmentsRepo.getAll().iterator();
            for(;it.hasNext();)
            {
                Appointment element = (Appointment)it.next();
                String date = element.getDateTime().toString().replace('T', ' ').concat(":00");
                Integer x = (int)element.getDuration().toMinutes();
                String duration = x.toString();
                String values = "('".concat(element.getId()).concat("', '")  +
                        element.getPatientId().concat("', '").concat(date).concat("', ") +
                        duration + ", '".concat(dentistID).concat("')");
                currentQuery = "INSERT INTO " + table + " VALUES " + values;
                statement.executeUpdate(currentQuery);
            }
            //('1(appointmentID)', '2(PatientID)', '2022-12-30', 10, '4(dentistID)')";

            statement.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public static HashMap<String, Appointment> importFromDB(String database, String table)
    {
        String url = "jdbc:sqlserver://localhost;database=".concat(database).concat(";trustServerCertificate=true");
        String username = "sa";
        String password = "paroladeSmecher/5";

        HashMap<String, Appointment> returnedAppointments = new HashMap<String, Appointment>();

        try
        {
            Connection connection = DriverManager.getConnection(url,username, password);
            Statement statement = connection.createStatement();

            String query = "SELECT AppointmentID, PatientID, DateTime, DurationInMinutes FROM " + table;
            ResultSet rs = statement.executeQuery(query);
            while(rs.next())
            {
                String appointmentID = rs.getString("AppointmentID").replace(" ", "");
                String patientID = rs.getString("PatientID").replace(" ", "");
                String time = rs.getString("DateTime");
                String[] timeParts1 = time.split(" ");
                String[] timeParts2 = timeParts1[0].split("-");
                String[] timeParts3 = timeParts1[1].split(":");
                LocalDateTime dateTime = LocalDateTime.of(Integer.parseInt(timeParts2[0]),
                        Integer.parseInt(timeParts2[1]), Integer.parseInt(timeParts2[2]),
                        Integer.parseInt(timeParts3[0]), Integer.parseInt(timeParts3[1]));
                Duration duration = Duration.of(rs.getInt("DurationInMinutes"), ChronoUnit.MINUTES);
                Appointment currentAppointment = new Appointment(appointmentID, patientID, dateTime, duration);
                returnedAppointments.put(appointmentID, currentAppointment);
            }
            statement.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return returnedAppointments;
    }
}
