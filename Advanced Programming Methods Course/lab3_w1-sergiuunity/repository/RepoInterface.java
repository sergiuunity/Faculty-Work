package repository;


public interface RepoInterface<ID, T>{

    public void add(ID id, T elem);
    public void delete(ID id);
    public void modify(ID id, T elem);
    public T findById(ID id);
    public Iterable<T> getAll();

    public int size();
}
