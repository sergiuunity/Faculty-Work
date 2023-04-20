package repository;

import domain.Gene;

import java.sql.*;
import java.util.ArrayList;
import java.util.Iterator;

public class Repository {

    ArrayList<Gene> repo;

    public Repository() {
        repo = new ArrayList<Gene>();
    }

    public void setRepo(ArrayList<Gene> newRepo)
    {
        repo = newRepo;
    }

    @Override
    public String toString() {
        return "["+ repo + "]";
    }

    public void addRoute(Gene elem)
    {
        if(repo.contains(elem))
            throw new RuntimeException("Element already exists");
        repo.add(elem);
    }

    public void removeRoute(Gene elem)
    {
        if(repo.contains(elem))
            repo.remove(elem);
        else
            throw new RuntimeException("Element already exists");
    }

    public int size()
    {
        return repo.size();
    }

    public void importDataFromDB()
    {
        String url = "jdbc:sqlserver://localhost;database=".concat("Practice").concat(";trustServerCertificate=true");
        String username = "sa";
        String password = "paroladeSmecher/5";

        ArrayList<Gene> newList = new ArrayList<>();

        try
        {
            Connection connection = DriverManager.getConnection(url,username, password);
            Statement statement = connection.createStatement();

            String query = "SELECT name, organism, [function], sequence FROM myTable";
            ResultSet rs = statement.executeQuery(query);
            while(rs.next())
            {
                String name = rs.getString("name");
                String organism = rs.getString("organism");
                String function = rs.getString("function");
                String sequence = rs.getString("sequence");
                Gene currentElem = new Gene(name, organism, function, sequence);
                newList.add(currentElem);
            }
            statement.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
        setRepo(newList);
    }

    public void exportDataToDB()
    {
        String url = "jdbc:sqlserver://localhost;database=".concat("Practice").concat(";trustServerCertificate=true");
        String username = "sa";
        String password = "paroladeSmecher/5";
        try {
            Connection connection = DriverManager.getConnection(url,username, password);
            Statement statement = connection.createStatement();

            //delete content
            String currentQuery = "DELETE FROM Table";
            statement.executeUpdate(currentQuery);

            //export
            Iterator<Gene> it = repo.iterator();
            for(;it.hasNext();)
            {
                Gene elem = (Gene)it.next();
                String values = elem.getName() + "," + elem.getOrganism() + "," + elem.getFunction() + "," + elem.getSequence();
                currentQuery = "INSERT INTO myTable(" + " VALUES (" + values +")";
                statement.executeUpdate(currentQuery);
            }

            statement.close();

        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }


    public ArrayList<Gene> getListSorted()//by the main criteria
    {
        ArrayList<Gene> newList = new ArrayList<>();
        repo.stream().sorted().forEach(newList::add);
        return newList;
    }

    public ArrayList<String> getComboBoxOptions()
    {
        ArrayList<String> newList = new ArrayList<>();
        newList.add("All");
        Iterator<Gene> it = repo.iterator();
        for(;it.hasNext();)
        {
            Gene elem = (Gene)it.next();
            if(!(newList.contains(elem.getOrganism())))
                newList.add(elem.getOrganism());
        }
        //System.out.println(newList);
        return newList;
    }

    public ArrayList<Gene> getFilteredListForComboBox(String currentText, String selectedOption)
    {
        ArrayList<Gene> newList = new ArrayList<>();
        repo.stream().filter(s-> s.isGood(currentText, selectedOption)).sorted().forEach(newList::add);
        return newList;
    }
}
