package domain;

public class ControlSoftware extends FlightControl{

    int version;


    public ControlSoftware(String code, boolean maintenance, int version) {
        super(code, maintenance);
        this.version = version;
    }

    @Override
    public double getPrice() {
        double price;
        if(version<10) price = 100f;
        else price =200f;
        if(maintenance)
            price*=2;
        return price;
    }

    @Override
    public String toString() {
        return "ControlSoftware{" +
                "version=" + version +
                ", code='" + code + '\'' +
                ", price='" + this.getPrice() + '\'' +
                ", maintenance=" + maintenance +
                '}';
    }


}
