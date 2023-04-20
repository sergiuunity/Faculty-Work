package repository;

import java.util.HashMap;
import java.util.Map;


public class GenericRepo<ID, T> implements RepoInterface<ID, T>{

    Map<ID,T> repository;

    public GenericRepo(HashMap<ID, T> new_repository)
    {
        this.repository = new_repository;
    }

    public GenericRepo()
    {
        this.repository = new HashMap<ID,T>();
    }

    @Override
    public void add(ID id,T elem) {
        if(repository.put(id, elem) != null) throw new RuntimeException("Duplicate ID");
    }

    @Override
    public void delete(ID id) {
        if(!repository.containsKey(id)) throw new RuntimeException("Key does not exist");
        repository.remove(id);
    }

    @Override
    public void modify(ID id, T elem) {
        if(!repository.containsKey(id)) throw new RuntimeException("Key does not exist");
        repository.replace(id,elem);
    }

    @Override
    public T findById(ID id) {
        if (repository.containsKey(id))
            return repository.get(id);
        else
            throw new RuntimeException("No element with such key exists");
    }

    @Override
    public Iterable<T> getAll() {
        return repository.values();
    }

    public HashMap<ID, T> getHashMap()
    {
        return (HashMap<ID, T>) repository;
    }

    @Override
    public String toString() {
        return "["+ repository + "]";
    }

    public int size()
    {
        return repository.size();
    }
}
