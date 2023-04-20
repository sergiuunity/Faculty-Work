package domain;

import repository.GenericRepo;

public class ActionRemove<ID, T> implements IAction<ID, T>{
    GenericRepo repo;
    ID elemId;
    T removedElem;

    public ActionRemove(GenericRepo repo, ID elemId, T removedElem) {
        this.repo = repo;
        this.elemId = elemId;
        this.removedElem = removedElem;
    }

    @Override
    public void executeUndo() {
        repo.add(elemId, removedElem);
    }

    @Override
    public void executeRedo() {
        repo.delete(elemId);
    }
}
