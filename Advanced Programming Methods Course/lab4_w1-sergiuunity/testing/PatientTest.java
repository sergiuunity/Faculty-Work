import domain.Patient;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

//assertEquals(x1,x2), assertTrue, assertFalse
public class PatientTest {

    @Test
    void testConstructor()
    {
        Patient patient = new Patient();
        assertEquals("", patient.getId());
        assertEquals("", patient.getName());
        assertEquals("", patient.getPhoneNumber());
        patient = new Patient("1", "name1", "0712345678");
        assertEquals("1", patient.getId());
        assertEquals("name1", patient.getName());
        assertEquals("0712345678", patient.getPhoneNumber());
    }

    @Test
    void testEquals()
    {
        Patient p1 = new Patient();
        Patient p2 = new Patient();
        assertTrue(p1.equals(p2));
        p1.setId("2");
        assertFalse(p1.equals(p2));
        p2.setId("2");
        assertTrue(p1.equals(p2));
        p2.setName("name");
        assertFalse(p1.equals(p2));
        p1.setName("name");
        p1.setPhoneNumber("0712345678");
        assertFalse(p1.equals(p2));
        p2.setPhoneNumber("0712345678");
        assertTrue(p1.equals(p2));
    }

    @Test
    void testToString()
    {
        Patient p1 = new Patient("1", "name1", "0712345678");
        String patientString =  "Patient(" + "name=" + p1.getName() + ", phoneNumber=" + p1.getPhoneNumber()  + ')';
        assertEquals(patientString, p1.toString());
    }

}
