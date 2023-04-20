module gui {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires java.sql;
    requires json.simple;

    opens gui to javafx.fxml;
    exports gui;
    exports main;
}