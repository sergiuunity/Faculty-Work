package repository;

import domain.Patient;

import java.io.Serializable;
import java.util.HashMap;
import java.util.function.Consumer;

public class PatientsRepo extends GenericRepo<String, Patient> {

    public PatientsRepo(HashMap<String, Patient> patientsMap) {
        this.repository = patientsMap;
    }

    public PatientsRepo() {
        this.repository = new HashMap<String, Patient>();
    }

    public void printPatients(){
        for(Patient patient:this.getAll())
        {
            Consumer<Patient> consumer = Patient::printPatient;
            consumer.accept(patient);

        }
    }

}
