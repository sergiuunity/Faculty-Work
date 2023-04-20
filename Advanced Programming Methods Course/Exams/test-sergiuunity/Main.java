import domain.ControlSoftware;
import domain.Instrument;
import repository.Repo;
import service.RepoService;
import ui.UI;

public class Main {
    public static void main(String[] args)
    {
        Repo repo = new Repo();

        ControlSoftware c1 = new ControlSoftware("1", true, 12);
        ControlSoftware c2 = new ControlSoftware("2", false, 7);
        Instrument c3 = new Instrument("3", true, "direction");
        Instrument c4 = new Instrument("4", false, "engine_state");

        repo.addControl(c1);
        repo.addControl(c2);
        repo.addControl(c3);
        repo.addControl(c4);

        RepoService repoService = new RepoService(repo);
        UI ui = new UI(repoService);

        ui.start();

    }
}
