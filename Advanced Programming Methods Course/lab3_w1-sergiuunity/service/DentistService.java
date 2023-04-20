package service;

import domain.Dentist;
import repository.*;

import java.util.Objects;

public class DentistService {

    public Dentist dentist;

    public Dentist getDentist() {
        return dentist;
    }

    public void setDentist(Dentist dentist) {
        this.dentist = dentist;
    }

    public DentistService(Dentist dentist) {
        this.dentist = dentist;
    }


    @Override
    public String toString() {
        return dentist.toString();
    }

    public void modifyDentistDetails(String newName)
    {
        dentist.setName(newName);
    }

    public void addPatient(String newPatientID, String newName, String newPhoneNumber)
    {
//        AppointmentsRepo newAppointmentsRepo = new AppointmentsRepo();
        dentist.addPatient(newPatientID, newName, newPhoneNumber);
    }

    public String returnPatientDetailsString(String givenPatientID)
    {
        return dentist.returnPatientDetailsString(givenPatientID);
    }

    public void modifyPatient(String givenPatientID, String newName, String newPhoneNumber)
    {
        dentist.modifyPatient(givenPatientID, newName, newPhoneNumber);
    }

    public void removePatient(String givenPatientID)
    {
        dentist.removePatient(givenPatientID);
    }

    public void addAppointment(String newAppointmentID, String givenPatientID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        dentist.addAppointment(newAppointmentID, givenPatientID, newYear, newMonth, newDay, newHour, newMinute, newDuration);
    }

    public void removeAppointment(String givenAppointmentID)
    {
        dentist.removeAppointment(givenAppointmentID);
    }

    public void modifyAppointment(String givenAppointmentID, String givenPatientID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
       dentist.modifyAppointment(givenAppointmentID, givenPatientID, newYear, newMonth, newDay, newHour, newMinute, newDuration);
    }

    public void retrieveData(String propertiesRepository, String pathPatients, String  pathAppointments)
    {
        if(propertiesRepository.equals("text")) {
            dentist.setPatients(new PatientsRepo(BufferedPatients.readPatients(pathPatients)));
            dentist.setAppointments(new AppointmentsRepo(BufferedAppointments.readAppointments(pathAppointments)));
        }
        else if(propertiesRepository.equals("binary"))
        {
            dentist.setPatients(new PatientsRepo(SerializePatients.readPatients(pathPatients)));
            dentist.setAppointments(new AppointmentsRepo(SerializeAppointments.readAppointments(pathAppointments)));
        }
    }

    public void storeData(String propertiesRepository, String pathPatients, String  pathAppointments)
    {
        if(propertiesRepository.equals("text")) {
            BufferedPatients.writePatients(dentist.getPatients(), pathPatients);
            BufferedAppointments.writeAppointments(dentist.getAppointments(), pathAppointments);
        }
        else if(propertiesRepository.equals("binary"))
        {
            SerializePatients.writePatients(dentist.getPatients(), pathPatients);
            SerializeAppointments.writeAppointments(dentist.getAppointments(), pathAppointments);
        }
    }

    public void printDentist()
    {
        dentist.printDentist();
    }
}
