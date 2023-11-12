from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from LoginWindow import LoginScreen
import json
from DataBaseOperation import DBOperation

class InstallWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Install Vehicle Parking System")
        self.resize(400, 200)

        layout = QVBoxLayout()

        # Labels for database and admin setup
        label_db_name = QLabel("Database Name: ")
        label_db_name.setStyleSheet("color: black; padding: 8px 0px; font-size: 18px;")
        label_db_username = QLabel("Database Username: ")
        label_db_username.setStyleSheet("color: black; padding: 8px 0px; font-size: 18px;")
        label_db_password = QLabel("Database Password: ")
        label_db_password.setStyleSheet("color: black; padding: 8px 0px; font-size: 18px;")
        label_admin_username = QLabel("Admin Username: ")
        label_admin_username.setStyleSheet("color: black; padding: 8px 0px; font-size: 18px;")
        label_admin_password = QLabel("Admin Password: ")
        label_admin_password.setStyleSheet("color: black; padding: 8px 0px; font-size: 18px;")
        label_no_of_two_seater = QLabel("No of Two Wheeler Space: ")
        label_no_of_two_seater.setStyleSheet("color: black; padding: 8px 0px; font-size: 18px;")
        label_no_of_four_seater = QLabel("No. of Four Wheeler Space: ")
        label_no_of_four_seater.setStyleSheet("color: black; padding: 8px 0px; font-size: 18px;")

        # LineEdits for user inputs
        self.input_db_name = QLineEdit()
        self.input_db_name.setText("vehicle_parking")
        self.input_db_name.setStyleSheet("padding: 5px; font-size: 17px; color: black;")
        self.input_db_username = QLineEdit()
        self.input_db_username.setStyleSheet("padding: 5px; font-size: 17px; color: black;")
        self.input_db_password = QLineEdit()
        self.input_db_password.setStyleSheet("padding: 5px; font-size: 17px; color: black;")
        self.input_admin_username = QLineEdit()
        self.input_admin_username.setStyleSheet("padding: 5px; font-size: 17px; color: black;")
        self.input_admin_password = QLineEdit()
        self.input_admin_password.setStyleSheet("padding: 5px; font-size: 17px; color: black;")
        self.input_two_wheeler = QLineEdit()
        self.input_two_wheeler.setStyleSheet("padding: 5px; font-size: 17px; color: black;")
        self.input_four_wheeler = QLineEdit()
        self.input_four_wheeler.setStyleSheet("padding: 5px; font-size: 17px; color: black;")

        # Save button and error label
        button_save = QPushButton("Save config")
        button_save.setStyleSheet("padding: 5px; font-size: 17px; background: blue; color: #fff;")
        self.error_label = QLabel()
        self.error_label.setStyleSheet("color: red")

        # Adding widgets to the layout
        layout.addWidget(label_db_name)
        layout.addWidget(self.input_db_name)
        layout.addWidget(label_db_username)
        layout.addWidget(self.input_db_username)
        layout.addWidget(label_db_password)
        layout.addWidget(self.input_db_password)
        layout.addWidget(label_admin_username)
        layout.addWidget(self.input_admin_username)
        layout.addWidget(label_admin_password)
        layout.addWidget(self.input_admin_password)
        layout.addWidget(label_no_of_two_seater)
        layout.addWidget(self.input_two_wheeler)
        layout.addWidget(label_no_of_four_seater)
        layout.addWidget(self.input_four_wheeler)
        layout.addWidget(button_save)
        layout.addWidget(self.error_label)

        # Connecting button signal to the slot method
        button_save.clicked.connect(self.showStepInfo)

        # Set the layout for the InstallWindow
        self.setLayout(layout)

    def showStepInfo(self):
        # Validation for user input
        if self.input_db_name.text() == "":
            self.error_label.setText("Please Enter DB Name")
            return

        if self.input_db_username.text() == "":
            self.error_label.setText("Please Enter DB Username")
            return

        if self.input_db_password.text() == "":
            self.error_label.setText("Please Enter DB Password")
            return

        if self.input_admin_username.text() == "":
            self.error_label.setText("Please Enter Admin Username")
            return

        if self.input_admin_password.text() == "":
            self.error_label.setText("Please Enter Admin Password")
            return

        if self.input_two_wheeler.text() == "":
            self.error_label.setText("Please Enter Two Wheeler Space")
            return

        if self.input_four_wheeler.text() == "":
            self.error_label.setText("Please Enter Four Wheeler Space")
            return

        # Collect user data to save in a JSON file
        data = {
            "username": self.input_db_username.text(),
            "database": self.input_db_name.text(),
            "password": self.input_db_password.text()
        }
        file = open("./config.json", "w")
        file.write(json.dumps(data))
        file.close()

        # Database operations - creating tables and inserting data
        dbOperation = DBOperation()
        dbOperation.CreateTables()
        dbOperation.InsertAdmin(self.input_admin_username.text(), self.input_admin_password.text())
        dbOperation.InsertOneTimeData(int(self.input_two_wheeler.text()), int(self.input_four_wheeler.text()))

        # Close the Install window and open the Login window
        self.close()
        self.login = LoginScreen()
        self.login.showLoginScreen()
        print("Save")
