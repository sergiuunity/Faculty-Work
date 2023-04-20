package service;

import domain.Dentist;
import domain.Patient;
import repository.AppointmentsRepo;

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

    public void addAppointmentToPatient(String givenPatientID, String newAppointmentID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        dentist.addAppointmentToPatient(givenPatientID, newAppointmentID, newYear, newMonth, newDay, newHour, newMinute, newDuration);
    }

    public void removeAppointmentFromPatient(String givenPatientID, String givenAppointmentID)
    {
        dentist.removeAppointmentFromPatient(givenPatientID, givenAppointmentID);
    }

    public void modifyAppointmentOfPatient(String givenPatientID, String givenAppointmentID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
       dentist.modifyAppointmentOfPatient(givenPatientID, givenAppointmentID, newYear, newMonth, newDay, newHour, newDay, newDuration);
    }
}
