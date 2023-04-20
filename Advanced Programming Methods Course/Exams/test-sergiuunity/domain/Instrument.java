package domain;

public class Instrument extends FlightControl{

    String measurementType;

    public Instrument(String code, boolean maintenance, String measurementType) {
        super(code, maintenance);
        if(measurementType.equals("altitude") || measurementType.equals("direction") || measurementType.equals("engine_state"))
            this.measurementType = measurementType;
        else
            throw new RuntimeException("Invalid measurementType");
    }

    @Override
    public double getPrice() {
        double price;
        if(measurementType.equals("altitude") || measurementType.equals("direction")) price = 50f;
        else price = 500f;
        if(maintenance)
            price*=2;
        return price;
    }

    @Override
    public String toString() {
        return "Instrument{" +
                "measurementType='" + measurementType + '\'' +
                ", code='" + code + '\'' +
                ", price='" + this.getPrice() + '\'' +
                ", maintenance=" + maintenance +
                '}';
    }
}
