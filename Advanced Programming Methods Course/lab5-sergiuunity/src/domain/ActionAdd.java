package domain;

import repository.GenericRepo;

public class ActionAdd<ID, T> implements IAction<ID, T>{
    GenericRepo repo;
    ID elemId;
    T addedElem;

    public ActionAdd(GenericRepo repo, ID elemId, T addedElem) {
        this.repo = repo;
        this.elemId = elemId;
        this.addedElem = addedElem;
    }

    @Override
    public void executeUndo() {
        repo.delete(elemId);
    }

    @Override
    public void executeRedo() {
        repo.add(elemId, addedElem);
    }
}
