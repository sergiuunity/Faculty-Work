package service;

import domain.FlightControl;
import repository.Repo;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Comparator;

public class RepoService {
    Repo repo;

    public RepoService(Repo repo) {
        this.repo = repo;
    }

    public void addControl(FlightControl elem)
    {
        repo.addControl(elem);
    }

    public String toString()
    {
        return repo.toString();
    }

    public void showCheaper(double givenPrice)
    {
        repo.getRepo().stream().filter(s-> s.isCheaperThan(givenPrice)).sorted().forEach(System.out::println);
    }

    public void saveToFile(String path)
    {
        try {
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(path));


        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
