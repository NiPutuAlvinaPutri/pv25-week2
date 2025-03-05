import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFormLayout, QGroupBox, QRadioButton, QComboBox, QTextEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("User Registration Form - Alternative Version")
        self.setGeometry(100, 100, 500, 400)

        main_layout = QVBoxLayout()

        # Title
        title = QLabel("User Registration Form")
        title.setFont(QFont("Arial", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
        
        # User Information Section
        user_info_group = QGroupBox("User Information")
        user_info_layout = QVBoxLayout()
        user_info_layout.addWidget(QLabel("Name: John Doe"))
        user_info_layout.addWidget(QLabel("NIM: 12345678"))
        user_info_group.setLayout(user_info_layout)
        main_layout.addWidget(user_info_group)
        
        # Form Section
        form_group = QGroupBox("Registration Details")
        form_layout = QFormLayout()
        
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.address_input = QTextEdit()
        
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Select", "USA", "UK", "India", "Indonesia", "Canada", "Germany"])
        
        form_layout.addRow("Email:", self.email_input)
        form_layout.addRow("Phone:", self.phone_input)
        form_layout.addRow("Address:", self.address_input)
        form_layout.addRow("Gender:", gender_layout)
        form_layout.addRow("Country:", self.country_combo)
        
        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)
        
        # Actions Section
        action_group = QGroupBox("Actions")
        action_layout = QHBoxLayout()
        submit_btn = QPushButton("Register")
        cancel_btn = QPushButton("Clear")
        action_layout.addWidget(submit_btn)
        action_layout.addWidget(cancel_btn)
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)
        
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec_())