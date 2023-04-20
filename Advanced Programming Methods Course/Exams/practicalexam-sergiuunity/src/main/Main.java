package main;

import gui.Controller;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

import repository.Repository;
import service.*;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("/gui/ui.fxml"));

        Repository repo = new Repository();
        Service service = new Service(repo);
        service.importDataFromDB();
        Controller controller = new Controller(service);
        fxmlLoader.setController(controller);
        Scene scene = new Scene(fxmlLoader.load(), 1280, 800);
        stage.setTitle("Genes App");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}