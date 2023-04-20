package testing;

import domain.Patient;
import org.junit.jupiter.api.Test;
import repository.PatientsRepo;

import java.util.HashMap;

import static org.junit.jupiter.api.Assertions.*;

public class PatientsRepoTest {

    @Test
    void testOperations()
    {
        PatientsRepo patientsRepo = new PatientsRepo();
        assertEquals(0, patientsRepo.size());
        HashMap<String, Patient> map = new HashMap<String, Patient>();
        Patient p1 = new Patient("1", "name1", "0712345678");
        map.put(p1.getId(), p1);
        patientsRepo = new PatientsRepo(map);
        assertEquals(1, patientsRepo.size());
        assertEquals(p1, patientsRepo.findById(p1.getId()));
        patientsRepo.delete(p1.getId());
        assertEquals(0, patientsRepo.size());
        try
        {
            patientsRepo.delete("1");
            assert false;
        }
        catch (RuntimeException e)
        {
            assert true;
        }
        try
        {
            patientsRepo.findById("1");
            assert false;
        }
        catch (RuntimeException e)
        {
            assert true;
        }
        try
        {
            patientsRepo.modify("1", p1);
            assert false;
        }
        catch (RuntimeException e)
        {
            assert true;
        }
        patientsRepo.add(p1.getId(), p1);
        assertEquals(1, patientsRepo.size());
        assertEquals(p1, patientsRepo.findById("1"));
        try
        {
            patientsRepo.add("1", p1);
            assert false;
        }
        catch (RuntimeException e)
        {
            assert true;
        }

    }
}
