package repository;

import domain.Appointment;
import domain.Patient;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;

public class PatientsRepo extends GenericRepo<String, Patient> {

    public PatientsRepo(HashMap<String, Patient> patientsMap) {
        this.repository = patientsMap;
    }

    public PatientsRepo() {
        this.repository = new HashMap<String, Patient>();
    }

    public ArrayList<String> phoneNumberOfPatient(String givenID)
    {
        List<Patient> list = new ArrayList<Patient>(repository.values());
        return (ArrayList<String>) list.stream().filter(s->s.getId().equals(givenID)).map(s->s.getPhoneNumber()).collect(Collectors.toList());
    }

    public ArrayList<Patient> patientsOrderedAlphabetically()
    {
        List<Patient> list = new ArrayList<Patient>(repository.values());
        return (ArrayList<Patient>) list.stream().sorted().collect(Collectors.toList());
    }

}
