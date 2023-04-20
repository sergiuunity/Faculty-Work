package repository;

import domain.Appointment;
import domain.Patient;

import java.io.Serializable;
import java.util.HashMap;
import java.util.function.Consumer;

public class AppointmentsRepo extends GenericRepo<String, Appointment> {

    public AppointmentsRepo(HashMap<String, Appointment> appointmentsMap) {
        this.repository = appointmentsMap;
    }

    public AppointmentsRepo() {
        this.repository = new HashMap<String, Appointment>();
    }

    public void printAppointments(){
        for(Appointment appointment:this.getAll())
        {
            Consumer<Appointment> consumer = Appointment::printAppointment;
            consumer.accept(appointment);

        }
    }


}
