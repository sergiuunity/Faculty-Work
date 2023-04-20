package domain;

public abstract class FlightControl implements Comparable<FlightControl>{
    protected String code;
    protected boolean maintenance;

    public FlightControl(String code, boolean maintenance) {
        this.code = code;
        this.maintenance = maintenance;
    }

    public abstract double getPrice();

    public boolean isCheaperThan(double givenPrice)
    {
        return getPrice()<givenPrice;
    }

    @Override
    public String toString() {
        return "FlightControl{" +
                "code='" + code + '\'' +
                ", maintenance=" + maintenance +
                '}';
    }

    public int compareTo(FlightControl other)
    {
        Double d = other.getPrice();
        return d.compareTo(this.getPrice());
    }
}
