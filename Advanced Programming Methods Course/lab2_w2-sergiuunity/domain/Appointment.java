package domain;

import java.time.*;
import java.util.Objects;

public class Appointment implements Entity<String> {

    private String id;

    private LocalDateTime dateTime;

    private Duration duration;

    public Appointment(String id, LocalDateTime dateTime, Duration duration) {
        this.id = id;
        this.dateTime = dateTime;
        this.duration = duration;
    }

    @Override
    public String getId() {
        return id;
    }

    @Override
    public void setId(String id) {
        this.id = id;
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
        return Objects.equals(id, that.id) && Objects.equals(dateTime, that.dateTime) && Objects.equals(duration, that.duration);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, dateTime, duration);
    }

    @Override
    public String toString() {
        return "Appointment{" +
                "id=" + id +
                ", dateTime=" + dateTime +
                ", duration=" + duration +
                '}';
    }
}
