package repository;

import domain.FlightControl;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Repo {

    List<FlightControl> repo;

    public Repo() {
        repo = new ArrayList<FlightControl>();
    }

    @Override
    public String toString() {
        return "Repo{" +
                "repo=" + repo +
                '}';
    }

    public void addControl(FlightControl elem)
    {
        if(repo.contains(elem))
            throw new RuntimeException("Element already exists");
        repo.add(elem);
    }

    public List<FlightControl> getRepo() {
        return repo;
    }


}
