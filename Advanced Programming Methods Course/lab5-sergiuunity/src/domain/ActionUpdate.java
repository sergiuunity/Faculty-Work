package domain;

import repository.GenericRepo;

public class ActionUpdate<ID, T> implements IAction<ID, T>{
    GenericRepo repo;
    ID elemId;
    T oldElem;
    T newElem;

    public ActionUpdate(GenericRepo repo, ID elemId, T oldElem, T newElem) {
        this.repo = repo;
        this.elemId = elemId;
        this.oldElem = oldElem;
        this.newElem = newElem;
    }

    @Override
    public void executeUndo() {
        repo.modify(elemId, oldElem);
    }

    @Override
    public void executeRedo() {
        repo.modify(elemId, newElem);
    }
}
