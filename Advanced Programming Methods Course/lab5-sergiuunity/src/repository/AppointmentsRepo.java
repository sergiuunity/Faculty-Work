package repository;

import domain.Appointment;

import java.io.Serializable;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class AppointmentsRepo extends GenericRepo<String, Appointment> {

    public AppointmentsRepo(HashMap<String, Appointment> appointmentsMap) {
        this.repository = appointmentsMap;
    }

    public AppointmentsRepo() {
        this.repository = new HashMap<String, Appointment>();
    }

    public ArrayList<Appointment> appointmentsOfPatient(String givenID)
    {
        List<Appointment> list = new ArrayList<Appointment>(repository.values());
        return (ArrayList<Appointment>) list.stream().filter(s->s.getPatientId().equals(givenID)).collect(Collectors.toList());
    }

    public ArrayList<Appointment> appointmentsOnDate(String givenDate)
    {
        String[] dateParts = givenDate.split("-");
        LocalDate dateToCompare = LocalDate.of(Integer.parseInt(dateParts[0]),
                Integer.parseInt(dateParts[1]), Integer.parseInt(dateParts[2]));
        List<Appointment> list = new ArrayList<Appointment>(repository.values());
        return (ArrayList<Appointment>) list.stream().filter(s->s.getDateTime().toLocalDate().equals(dateToCompare)).collect(Collectors.toList());
    }

    public ArrayList<Appointment> appointmentsOrderedByDate()
    {
        List<Appointment> list = new ArrayList<Appointment>(repository.values());
        return (ArrayList<Appointment>) list.stream().sorted().collect(Collectors.toList());
    }

}
