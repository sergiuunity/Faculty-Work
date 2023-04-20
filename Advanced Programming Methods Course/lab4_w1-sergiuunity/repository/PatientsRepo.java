package repository;

import domain.Appointment;
import domain.Patient;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class PatientsRepo extends GenericRepo<String, Patient> {

    public PatientsRepo(HashMap<String, Patient> patientsMap) {
        this.repository = patientsMap;
    }

    public PatientsRepo() {
        this.repository = new HashMap<String, Patient>();
    }

    public void phoneNumberOfPatient(String givenID)
    {
        List<Patient> list = new ArrayList<Patient>(repository.values());
        list.stream().filter(s->s.getId().equals(givenID)).forEach(s-> System.out.println(s.getPhoneNumber()));
    }

    public void patientsOrderedAlphabetically()
    {
        List<Patient> list = new ArrayList<Patient>(repository.values());
        list.stream().sorted().forEach(System.out::println);
    }

}
