package gui;

import domain.Gene;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import org.w3c.dom.events.MouseEvent;
import service.Service;

import java.util.ArrayList;

import static javafx.collections.FXCollections.observableArrayList;

public class Controller {
    private Service service;
    @FXML
    private ListView<Gene> mainList;
    @FXML
    private ObservableList<Gene> observableMainList = FXCollections.observableArrayList();

    public Controller(Service service) {
        this.service = service;
    }

    public void setMainList(ArrayList<Gene> newList)
    {
        observableMainList.clear();
        observableMainList.addAll(newList);
        mainList.setItems(observableMainList);
    }

    public void initialize()
    {
        setMainList(service.getListSorted());
        setUpComboBox();
    }


    @FXML
    private ComboBox<String> comboBox;

    public void setUpComboBox()
    {
        ObservableList<String> comboBoxOptions = observableArrayList();
        //addAll list containing all options created somewhere else using iterator

        comboBoxOptions.addAll(service.getComboBoxOptions());
        comboBox.setItems(comboBoxOptions);

    }

    @FXML
    void onComboBoxAct(ActionEvent event)
    {
        //setMainList(service.getFilteredListForComboBox());
    }

    @FXML
    private TextField firstTextField;
    @FXML
    void onFirstTextFieldAct(ActionEvent event)
    {
        String currentText = firstTextField.getText();
        String selectedOption = comboBox.getSelectionModel().getSelectedItem();
        setMainList(service.getFilteredListForComboBox(currentText, selectedOption));
    }

    @FXML
    private Button myButton;
    @FXML
    void onButtonClicked(ActionEvent event)
    {
//        Stage secondStage = new Stage();
//        popUp popUp = new popUp();
//        FXMLLoader loader = new FXMLLoader(getClass().getResource("/gui/popUp.fxml"));
//        loader.setController(popUp);
//        Parent root = null;
//        try {
//            root = (Parent)loader.load();
//            Scene scene = new Scene(root, 1280, 720);
//            secondStage.setTitle("Dentist GUI");
//            secondStage.setScene(scene);
//            secondStage.show();
//        } catch (IOException e) {
//            throw new RuntimeException(e);
//        }

    }


    @FXML
    private TextField secondTextField;
    @FXML
    private TextArea textArea;


    @FXML
    void onGeneClicked(ActionEvent event)
    {
        Gene currentGene = mainList.getSelectionModel().getSelectedItem();
        secondTextField.setPromptText(currentGene.getFunction());
        textArea.setText(currentGene.getSequence());

    }

    @FXML
    void onSecondTextFieldAct(ActionEvent event) {
        String secondText = secondTextField.getText();
        Gene currentGene = mainList.getSelectionModel().getSelectedItem();
        currentGene.setFunction(secondText);
        service.exportDataToDB();
    }
}
