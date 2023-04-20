package gui;

import domain.Appointment;
import domain.Patient;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import service.DentistService;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

import static javafx.collections.FXCollections.observableArrayList;

public class DentistGUI {

    @FXML
    private ComboBox<String> appointmentsReportsComboBox;

    @FXML
    private ComboBox<String> patientsReportsComboBox;

    @FXML
    private TextField appointmentsReportsTextField;

    @FXML
    private TextField patientsReportsTextField;


    private DentistService dentistService;
    @FXML
    private Label dentistName;

    @FXML
    private Label dentistID;



    @FXML
    private ListView<Patient> patientsListView;
    private ObservableList<Patient> patients = observableArrayList();
    @FXML
    private ListView<Appointment> appointmentsListView;
    private ObservableList<Appointment> appointments = observableArrayList();


    @FXML
    private TextField dentistNameField;


    @FXML
    private TextField patientIDField;

    @FXML
    private TextField patientNameField;

    @FXML
    private TextField patientPhoneNumberField;



    @FXML
    private TextField appointmentDayField;

    @FXML
    private TextField appointmentDurationField;

    @FXML
    private TextField appointmentHourField;

    @FXML
    private TextField appointmentIDField;

    @FXML
    private TextField appointmentMinuteField;

    @FXML
    private TextField appointmentMonthField;

    @FXML
    private TextField appointmentPatientIDField;

    @FXML
    private TextField appointmentYearField;


    public DentistGUI(DentistService dentistService) {
        this.dentistService = dentistService;
    }

    public void displayAlertForNotEnoughDataIntroduced()
    {
        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle("Not enough data introduced.");
        alert.setContentText("Fill all the necessary fields before pressing Add/Update.");
        alert.showAndWait();
    }

    private void displayAlertForNotSelectingItem()
    {
        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle("No item selected.");
        alert.setContentText("Select an item to remove/cancel.");
        alert.showAndWait();
    }

    private void displayAlertInvalidData()
    {
        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle("Invalid data introduced.");
        alert.setContentText("You either introduced wrong data types or the given items are already in there in the case of adding(or missing in the case of updating).");
        alert.showAndWait();
    }

    private void displayAlertWithGivenMessage(String givenMessage)
    {
        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle("Alert!");
        alert.setContentText(givenMessage);
        alert.showAndWait();
    }

    public void emptyAndFillLists()
    {
        patients.clear();
        appointments.clear();
        Iterable<Patient> patientsIt = dentistService.getDentist().getPatients().getAll();
        for(Patient patient:patientsIt)
        {
            patients.add(patient);
        }

        Iterable<Appointment> appointmentsIt = dentistService.getDentist().getAppointments().getAll();
        for(Appointment appointment:appointmentsIt)
        {
            appointments.add(appointment);
        }
    }

    public void initialize()
    {
        dentistName.setText(dentistService.getDentist().getName());
        dentistID.setText(Integer.valueOf(dentistService.getDentist().getId()).toString());

        emptyAndFillLists();
        patientsListView.setItems(patients);
        appointmentsListView.setItems(appointments);

        ObservableList<String> appointmentsReports = observableArrayList();
        appointmentsReports.add("all");
        appointmentsReports.add("all the appointments for a certain patient");
        appointmentsReports.add("all the appointments on a certain date");
        appointmentsReports.add("all the appointments ordered by date");
        appointmentsReportsComboBox.setItems(appointmentsReports);

        ObservableList<String> patientsReports = observableArrayList();
        patientsReports.add("all");
        patientsReports.add("the phone number of a certain patient");
        patientsReports.add("all the patients ordered alphabetically");
        patientsReportsComboBox.setItems(patientsReports);
    }

    @FXML
    void onAppointmentsAddClicked(ActionEvent event) {
        try {
            if (appointmentYearField.getText().equals("") || appointmentMonthField.getText().equals("") || appointmentDayField.getText().equals("")
                    || appointmentHourField.getText().equals("") || appointmentMinuteField.getText().equals("") || appointmentDurationField.getText().equals("")
                    || appointmentIDField.getText().equals("") || appointmentPatientIDField.getText().equals("")) {
                displayAlertForNotEnoughDataIntroduced();
            } else {
                dentistService.addAppointment(appointmentIDField.getText(),
                        appointmentPatientIDField.getText(),
                        Integer.parseInt(appointmentYearField.getText()),
                        Integer.parseInt(appointmentMonthField.getText()),
                        Integer.parseInt(appointmentDayField.getText()),
                        Integer.parseInt(appointmentHourField.getText()),
                        Integer.parseInt(appointmentMinuteField.getText()),
                        Integer.parseInt(appointmentDurationField.getText()));
                appointments.add(dentistService.getAppointmentAtID(appointmentIDField.getText()));
            }
        }
        catch (RuntimeException re)
        {
            displayAlertInvalidData();
        }
    }

    @FXML
    void onAppointmentsCancelClicked(ActionEvent event) {
        try {
            int selectedID = appointmentsListView.getSelectionModel().getSelectedIndex();
            dentistService.removeAppointment(appointmentsListView.getItems().get(selectedID));
            appointmentsListView.getItems().remove(selectedID);
        }
        catch (RuntimeException re)
        {
            displayAlertForNotSelectingItem();
        }
    }


    @FXML
    void onAppointmentsUpdateClicked(ActionEvent event) {
        try {
            if (appointmentYearField.getText().equals("") || appointmentMonthField.getText().equals("") || appointmentDayField.getText().equals("")
                    || appointmentHourField.getText().equals("") || appointmentMinuteField.getText().equals("") || appointmentDurationField.getText().equals("")
                    || appointmentIDField.getText().equals("") || appointmentPatientIDField.getText().equals("")) {
                displayAlertForNotEnoughDataIntroduced();
            } else {
                int index = appointments.indexOf(dentistService.getAppointmentAtID(appointmentIDField.getText()));
                dentistService.modifyAppointment(appointmentIDField.getText(),
                        appointmentPatientIDField.getText(),
                        Integer.parseInt(appointmentYearField.getText()),
                        Integer.parseInt(appointmentMonthField.getText()),
                        Integer.parseInt(appointmentDayField.getText()),
                        Integer.parseInt(appointmentHourField.getText()),
                        Integer.parseInt(appointmentMinuteField.getText()),
                        Integer.parseInt(appointmentDurationField.getText()));
                appointments.set(index, dentistService.getAppointmentAtID(appointmentIDField.getText()));
            }
        }
        catch (RuntimeException re)
        {
            displayAlertInvalidData();
        }
    }

    @FXML
    void onModifyDentistClicked(ActionEvent event) {
        try {
            if (dentistNameField.getText().equals("")) {
                displayAlertForNotEnoughDataIntroduced();
            } else {
                dentistService.modifyDentistDetails(dentistNameField.getText());
                dentistName.setText(dentistService.getDentist().getName());
            }
        }
        catch (RuntimeException re)
        {
            displayAlertWithGivenMessage(re.getMessage());
        }
    }

    @FXML
    void onPatientsAddClicked(ActionEvent event) {
        try {
            if (patientIDField.getText().equals("") || patientNameField.getText().equals("") || patientPhoneNumberField.getText().equals("")) {
                displayAlertForNotEnoughDataIntroduced();
            } else {
                dentistService.addPatient(patientIDField.getText(),
                        patientNameField.getText(),
                        patientPhoneNumberField.getText());
                patients.add(dentistService.getPatientAtID(patientIDField.getText()));
            }
        }
        catch (RuntimeException re)
        {
            displayAlertInvalidData();
        }
    }

    @FXML
    void onPatientsRemoveClicked(ActionEvent event) {
        try {
            int selectedID = patientsListView.getSelectionModel().getSelectedIndex();
            dentistService.removePatient(patientsListView.getItems().get(selectedID));
            patientsListView.getItems().remove(selectedID);
        }
        catch (RuntimeException re)
        {
            displayAlertForNotSelectingItem();
        }

    }

    @FXML
    void onPatientsUpdateClicked(ActionEvent event) {
        try {
            if (patientIDField.getText().equals("") || patientNameField.getText().equals("") || patientPhoneNumberField.getText().equals("")) {
                displayAlertForNotEnoughDataIntroduced();
            } else {
                int index = patients.indexOf(dentistService.getPatientAtID(patientIDField.getText()));
                dentistService.modifyPatient(patientIDField.getText(),
                        patientNameField.getText(),
                        patientPhoneNumberField.getText());
                patients.set(index, dentistService.getPatientAtID(patientIDField.getText()));
            }
        }
        catch (RuntimeException re)
        {
            displayAlertInvalidData();
        }
    }


    @FXML
    void onRetrieveClicked(ActionEvent event) {
        //reading properties
        String propertiesRepository;
        String location;
        String propertiesPatients;
        String propertiesAppointments;
        Properties properties = new Properties();
        try {
            FileInputStream ip = new FileInputStream("src/text_files/settings.properties");
            properties.load(ip);
            propertiesRepository = properties.getProperty("Repository");
            location = properties.getProperty("Location");
            propertiesPatients = properties.getProperty("Patients");
            propertiesAppointments = properties.getProperty("Appointments");

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        try
        {
            dentistService.retrieveData(propertiesRepository, location, propertiesPatients, propertiesAppointments);
            emptyAndFillLists();
        }
        catch (RuntimeException re)
        {
            displayAlertWithGivenMessage(re.getMessage());
        }
    }

    @FXML
    void onStoreClicked(ActionEvent event) {

        //reading properties
        String propertiesRepository;
        String location;
        String propertiesPatients;
        String propertiesAppointments;
        Properties properties = new Properties();
        try {
            FileInputStream ip = new FileInputStream("src/text_files/settings.properties");
            properties.load(ip);
            propertiesRepository = properties.getProperty("Repository");
            location = properties.getProperty("Location");
            propertiesPatients = properties.getProperty("Patients");
            propertiesAppointments = properties.getProperty("Appointments");

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        try
        {
            dentistService.storeData(propertiesRepository, location, propertiesPatients, propertiesAppointments);
        }
        catch (RuntimeException re)
        {
            displayAlertWithGivenMessage(re.getMessage());
        }
    }

    @FXML
    void onUndoClicked(ActionEvent event) {
        try
        {
            dentistService.undo();
            emptyAndFillLists();
        }
        catch (RuntimeException re)
        {
            displayAlertWithGivenMessage(re.getMessage());
        }
    }


    @FXML
    void onRedoClicked(ActionEvent event) {
        try
        {
            dentistService.redo();
            emptyAndFillLists();
        }
        catch (RuntimeException re)
        {
            displayAlertWithGivenMessage(re.getMessage());
        }
    }





    //reports Work
    void setAppointmentsListView(ObservableList<Appointment> newAppointments)
    {
        appointmentsListView.setItems(newAppointments);
    }

    void setAppointmentsListView(ArrayList<Appointment> newAppointments)
    {
        ObservableList<Appointment> currentAppointments = observableArrayList();
        for(Appointment appointment:newAppointments)
        {
            currentAppointments.add(appointment);
        }

        appointmentsListView.setItems(currentAppointments);
    }

    void setPatientsListView(ObservableList<Patient> newPatients)
    {
        patientsListView.setItems(newPatients);
    }

    void setPatientsListView(ArrayList<Patient> newPatients)
    {
        ObservableList<Patient> currentPatients = observableArrayList();
        for(Patient patient:newPatients)
        {
            currentPatients.add(patient);
        }

        patientsListView.setItems(currentPatients);
    }




    @FXML
    void onAppointmentsReportsComboBoxChanged(ActionEvent event) {

        String selectedOption = appointmentsReportsComboBox.getSelectionModel().getSelectedItem();
        if(selectedOption.equals("all the appointments for a certain patient"))
            appointmentsReportsTextField.setPromptText("give patient id....");
        else if(selectedOption.equals("all the appointments on a certain date"))
            appointmentsReportsTextField.setPromptText("give date(yyyy-mm-dd)...");
        else if(selectedOption.equals("all the appointments ordered by date") || selectedOption.equals("all"))
            appointmentsReportsTextField.setPromptText("just press go...");
    }

    @FXML
    void onPatientsReportsComboBoxChanged(ActionEvent event) {

        String selectedOption = patientsReportsComboBox.getSelectionModel().getSelectedItem();
        if(selectedOption.equals("the phone number of a certain patient"))
            patientsReportsTextField.setPromptText("give patient id...");
        else if(selectedOption.equals("all the patients ordered alphabetically")|| selectedOption.equals("all"))
            patientsReportsTextField.setPromptText("just press go...");
    }


    @FXML
    void onGoAppointmentsReports(ActionEvent event) {
        String selectedOption = appointmentsReportsComboBox.getSelectionModel().getSelectedItem();
        if(selectedOption.equals("all the appointments for a certain patient"))
        {
            String wantedID = appointmentsReportsTextField.getText();
            setAppointmentsListView(dentistService.appointmentsOfPatient(wantedID));
        }
        else if(selectedOption.equals("all the appointments on a certain date"))
        {
            try
            {
                String wantedDate = appointmentsReportsTextField.getText();
                setAppointmentsListView(dentistService.appointmentsOnDate(wantedDate));
            }
            catch (RuntimeException re)
            {
                displayAlertWithGivenMessage(re.getMessage());
            }
        }
        else if(selectedOption.equals("all the appointments ordered by date"))
        {
            setAppointmentsListView(dentistService.appointmentsOrderedByDate());
        }
        else if(selectedOption.equals("all"))
        {
            setAppointmentsListView(appointments);
        }
    }

    @FXML
    void onGoPatientsReports(ActionEvent event) {
        String selectedOption = patientsReportsComboBox.getSelectionModel().getSelectedItem();
        if(selectedOption.equals("the phone number of a certain patient"))
        {
            String wantedID = patientsReportsTextField.getText();
            ArrayList<String> listOfStrings = dentistService.phoneNumberOfPatient(wantedID);
            ArrayList<Patient> listOfPatients = new ArrayList<Patient>();
            listOfPatients.add(0, new Patient("", "", listOfStrings.get(0)));
            setPatientsListView(listOfPatients);
        }
        else if(selectedOption.equals("all the patients ordered alphabetically"))
        {
            setPatientsListView(dentistService.patientsOrderedAlphabetically());
        }
        else if (selectedOption.equals("all"))
        {
            setPatientsListView(patients);
        }
    }


    //end of reports Work



}
