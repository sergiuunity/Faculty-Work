package service;

import domain.Gene;
import repository.Repository;

import java.util.ArrayList;

import static javafx.collections.FXCollections.observableArrayList;

public class Service {
    private Repository repo;

    public Service(Repository repo) {
        this.repo = repo;
    }

    public void importDataFromDB()
    {
        repo.importDataFromDB();
    }

    public void exportDataToDB()
    {
        repo.exportDataToDB();
    }

    public ArrayList<String> getComboBoxOptions()
    {
        return repo.getComboBoxOptions();
    }


    public ArrayList<Gene> getListSorted()
    {
        return repo.getListSorted();
    }

    public ArrayList<Gene> getFilteredListForComboBox(String currentText, String selectedOption)
    {
        return repo.getFilteredListForComboBox(currentText, selectedOption);
    }
}
