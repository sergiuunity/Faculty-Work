package service;

import domain.*;
import repository.*;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.Stack;

public class DentistService {

    public Dentist dentist;

    private Stack<IAction> undoStack;

    private Stack<IAction> redoStack;

    public Dentist getDentist() {
        return dentist;
    }

    public void setDentist(Dentist dentist) {
        this.dentist = dentist;
    }

    public DentistService(Dentist dentist) {
        this.dentist = dentist;
        undoStack = new Stack<>();
        redoStack = new Stack<>();
    }

    public void undo()
    {
        if(undoStack.isEmpty())
            throw new RuntimeException("No operations available in the undoStack.");
        else
        {
            undoStack.peek().executeUndo();
            redoStack.push(undoStack.pop());
        }
    }

    public void redo()
    {
        if(redoStack.isEmpty())
            throw new RuntimeException("No operations available in the redoStack.");
        else
        {
            redoStack.peek().executeRedo();
            undoStack.push(redoStack.pop());
        }
    }


    @Override
    public String toString() {
        return dentist.toString();
    }

    public void modifyDentistDetails(String newName)
    {
        dentist.setName(newName);
    }


    public String returnPatientDetailsString(String givenPatientID)
    {
        return dentist.returnPatientDetailsString(givenPatientID);
    }

    public void addPatient(String newPatientID, String newName, String newPhoneNumber)
    {
        dentist.addPatient(newPatientID, newName, newPhoneNumber);
        Patient newPatient = new Patient(newPatientID, newName, newPhoneNumber);
        ActionAdd actionAdd = new ActionAdd<>(dentist.getPatients(), newPatientID, newPatient);
        undoStack.push(actionAdd);
    }

    public void modifyPatient(String givenPatientID, String newName, String newPhoneNumber)
    {
        Patient copyOldPatient = getPatientAtID(givenPatientID);
        Patient copyNewPatient = new Patient(givenPatientID, newName, newPhoneNumber);
        dentist.modifyPatient(givenPatientID, newName, newPhoneNumber);
        ActionUpdate actionUpdate = new ActionUpdate<>(dentist.getPatients(), givenPatientID, copyOldPatient, copyNewPatient);
        undoStack.push(actionUpdate);
    }

    public void removePatient(String givenPatientID)
    {
        Patient copyPatient = getPatientAtID(givenPatientID);
        dentist.removePatient(givenPatientID);
        ActionRemove actionRemove = new ActionRemove<>(dentist.getPatients(), givenPatientID, copyPatient);
        undoStack.push(actionRemove);
    }

    public void removePatient(Patient givenPatient){
        dentist.removePatient(givenPatient);
        ActionRemove actionRemove = new ActionRemove<>(dentist.getPatients(), givenPatient.getId(), givenPatient);
        undoStack.push(actionRemove);
    }

    public Patient getPatientAtID(String givenID)
    {
        return dentist.getPatientAtID(givenID);
    }

    public Appointment getAppointmentAtID(String givenID)
    {
        return dentist.getAppointmentAtID(givenID);
    }

    public void addAppointment(String newAppointmentID, String givenPatientID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        dentist.addAppointment(newAppointmentID, givenPatientID, newYear, newMonth, newDay, newHour, newMinute, newDuration);
        LocalDateTime dateTime = LocalDateTime.of(newYear, newMonth, newDay, newHour, newMinute);
        Duration duration = Duration.of(newDuration, ChronoUnit.MINUTES);
        Appointment newAppointment = new Appointment(newAppointmentID, givenPatientID, dateTime, duration);
        ActionAdd actionAdd = new ActionAdd<>(dentist.getAppointments(), newAppointmentID, newAppointment);
        undoStack.push(actionAdd);
    }


    public void removeAppointment(String givenAppointmentID)
    {
        Appointment copyAppointment = getAppointmentAtID(givenAppointmentID);
        dentist.removeAppointment(givenAppointmentID);
        ActionRemove actionRemove = new ActionRemove<>(dentist.getAppointments(), givenAppointmentID, copyAppointment);
        undoStack.push(actionRemove);
    }

    public void removeAppointment(Appointment givenAppointment)
    {
        dentist.removeAppointment(givenAppointment);
        ActionRemove actionRemove = new ActionRemove<>(dentist.getAppointments(), givenAppointment.getId(), givenAppointment);
        undoStack.push(actionRemove);
    }

    public void modifyAppointment(String givenAppointmentID, String givenPatientID, Integer newYear, Integer newMonth, Integer newDay, Integer newHour, Integer newMinute, Integer newDuration)
    {
        Appointment copyOldAppointment = getAppointmentAtID(givenAppointmentID);
        LocalDateTime dateTime = LocalDateTime.of(newYear, newMonth, newDay, newHour, newMinute);
        Duration duration = Duration.of(newDuration, ChronoUnit.MINUTES);
        Appointment copyNewAppointment = new Appointment(givenAppointmentID, givenPatientID, dateTime, duration);
        dentist.modifyAppointment(givenAppointmentID, givenPatientID, newYear, newMonth, newDay, newHour, newMinute, newDuration);
        ActionUpdate actionUpdate = new ActionUpdate<>(dentist.getAppointments(), givenAppointmentID, copyOldAppointment, copyNewAppointment);
        undoStack.push(actionUpdate);
    }

    public void retrieveData(String propertiesRepository, String location, String pathPatients, String  pathAppointments)
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
        else if(propertiesRepository.equals("database"))
        {
            dentist.setPatients(new PatientsRepo(DBPatients.importFromDB(location, pathPatients)));
            dentist.setAppointments(new AppointmentsRepo(DBAppointments.importFromDB(location, pathAppointments)));
        }
        else if(propertiesRepository.equals("json"))
        {
            dentist.setPatients(new PatientsRepo(JSONPatients.readPatients(pathPatients)));
            dentist.setAppointments(new AppointmentsRepo(JSONAppointments.readAppointments(pathAppointments)));
        }
    }

    public void storeData(String propertiesRepository, String location, String pathPatients, String pathAppointments)
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
        else if(propertiesRepository.equals("database"))
        {
            DBPatients.exportToDB(location, pathPatients, dentist.getPatients(), dentist.getId());
            DBAppointments.exportToDB(location, pathAppointments, dentist.getAppointments(), dentist.getId());
        }
        else if(propertiesRepository.equals("json"))
        {
            JSONPatients.writePatients(dentist.getPatients(), pathPatients);
            JSONAppointments.writeAppointments(dentist.getAppointments(), pathAppointments);
        }
    }

    public ArrayList<Appointment> appointmentsOfPatient(String givenID)
    {
        return dentist.appointmentsOfPatient(givenID);
    }

    public ArrayList<String> phoneNumberOfPatient(String givenID)
    {
        return dentist.phoneNumberOfPatient(givenID);
    }

    public ArrayList<Appointment> appointmentsOnDate(String givenDate)
    {
        return dentist.appointmentsOnDate(givenDate);
    }

    public ArrayList<Appointment> appointmentsOrderedByDate()
    {
        return dentist.appointmentsOrderedByDate();
    }

    public ArrayList<Patient> patientsOrderedAlphabetically()
    {
        return dentist.patientsOrderedAlphabetically();
    }
}
