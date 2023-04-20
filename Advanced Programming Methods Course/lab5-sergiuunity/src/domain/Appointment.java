package domain;

import java.io.Serializable;
import java.time.Duration;
import java.time.LocalDateTime;
import java.util.Objects;

public class Appointment implements Entity<String>,Serializable, Comparable<Appointment>{

    private String id;

    private String patientId;

    private LocalDateTime dateTime;

    private Duration duration;


    public Appointment(String id, String patientId, LocalDateTime dateTime, Duration duration) {
        this.id = id;
        this.dateTime = dateTime;
        this.duration = duration;
        this.patientId = patientId;
    }

    @Override
    public String getId() {
        return id;
    }

    @Override
    public void setId(String id) {
        this.id = id;
    }

    public String getPatientId() {
        return patientId;
    }

    public void setPatientId(String patientId) {
        this.patientId = patientId;
    }

    public LocalDateTime getDateTime() {
        return dateTime;
    }

    public void setDateTime(LocalDateTime dateTime) {
        this.dateTime = dateTime;
    }

    public Duration getDuration() {
        return duration;
    }

    public void setDuration(Duration duration) {
        this.duration = duration;
    }



    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Appointment that = (Appointment) o;
        return Objects.equals(id, that.id) && Objects.equals(dateTime, that.dateTime) && Objects.equals(duration, that.duration) && Objects.equals(patientId, that.patientId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, dateTime, duration, patientId);
    }

    @Override
    public String toString() {
//        return "Appointment(" +
//                "patientId=" + patientId +
//                ", dateTime=" + dateTime +
//                ", duration=" + duration +
//                ')';
        return id + "\t" + "patientID:" + patientId + "\t" + dateTime + "\t" + duration;
    }

    @Override
    public int compareTo(Appointment other)
    {
        return this.getDateTime().compareTo(other.getDateTime());
    }

}
