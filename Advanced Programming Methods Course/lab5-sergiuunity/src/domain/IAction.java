package domain;

public interface IAction<ID, T> {
    public void executeUndo();

    public void executeRedo();

}
