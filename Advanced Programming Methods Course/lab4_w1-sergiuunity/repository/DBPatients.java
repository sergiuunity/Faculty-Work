package repository;

import domain.Appointment;
import domain.Patient;

import java.sql.*;
import java.util.HashMap;
import java.util.Iterator;

public class DBPatients {
    public static void exportToDB(String database, String table, PatientsRepo patientsRepo, String dentistID)
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
            Iterator<Patient> it = patientsRepo.getAll().iterator();
            for(;it.hasNext();)
            {
                Patient element = (Patient) it.next();
                String values = "('".concat(element.getId()).concat("', '").concat(element.getName()).
                        concat("', '").concat(element.getPhoneNumber()).concat("', '").
                        concat(dentistID).concat("')");
                currentQuery = "INSERT INTO " + table + " VALUES " + values;
                statement.executeUpdate(currentQuery);
            }
            //('2(PatientID)', 'Name', '0712345678', '4(dentistID)');

            statement.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }

    public static HashMap<String, Patient> importFromDB(String database, String table)
    {
        String url = "jdbc:sqlserver://localhost;database=".concat(database).concat(";trustServerCertificate=true");
        String username = "sa";
        String password = "paroladeSmecher/5";

        HashMap<String, Patient> returnedPatients = new HashMap<String, Patient>();

        try
        {
            Connection connection = DriverManager.getConnection(url,username, password);
            Statement statement = connection.createStatement();

            String query = "SELECT PatientID, Name, PhoneNumber FROM " + table;
            ResultSet rs = statement.executeQuery(query);
            while(rs.next())
            {
                String patientID = rs.getString("PatientID").replace(" ", "");
                String name = rs.getString("Name");
                String phoneNumber = rs.getString("PhoneNumber");
                Patient currentPatient = new Patient(patientID, name, phoneNumber);
                returnedPatients.put(patientID, currentPatient);
            }
            statement.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        return returnedPatients;
    }

}
