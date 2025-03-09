import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QRadioButton, QComboBox, 
                             QButtonGroup, QGroupBox, QFormLayout, QSpacerItem, 
                             QSizePolicy)
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

class UserRegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Week 2 : Layout - User Registration Form')
        self.setFixedSize(400, 500)
        
        # Set overall background
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QGroupBox {
                background-color: #e0e0e0;
                border: 1px solid #c0c0c0;
                border-radius: 5px;
                margin-top: 10px;
                font-weight: bold;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
            }
            QPushButton {
                border-radius: 10px;
                padding: 6px;
                background-color: #f0f0f0;
                border: 1px solid gray;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
        """)
        
        main_layout = QVBoxLayout()
        
        # Identitas
        identitas_box = QGroupBox("Identitas (vertical box layout)")
        identitas_layout = QVBoxLayout()
        for text in ['Nama  : Ni_Putu_Alvina_Putri', 'Nim     : F1D022017', 'Kelas  : C']:
            label = QLabel(text)
            label.setStyleSheet("color: #333;")
            identitas_layout.addWidget(label)
        identitas_box.setLayout(identitas_layout)
        main_layout.addWidget(identitas_box)
        
        # Navigasi
        nav_box = QGroupBox("Navigation (horizontal box layout)")
        nav_layout = QHBoxLayout()
        for btn_text in ['Home', 'About', 'Contact']:
            btn = QPushButton(btn_text)
            nav_layout.addWidget(btn)
        nav_box.setLayout(nav_layout)
        main_layout.addWidget(nav_box)
        
        # Form User Registration
        form_box = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()
        
        # Adjust label alignment and add spacing
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setFormAlignment(Qt.AlignRight | Qt.AlignVCenter)
        form_layout.setHorizontalSpacing(20)  # Increased horizontal spacing
        
        # Full Name
        full_name_label = QLabel('Full Name')
        full_name_input = QLineEdit()
        form_layout.addRow(full_name_label, full_name_input)
        
        # Email
        email_label = QLabel('Email')
        email_input = QLineEdit()
        form_layout.addRow(email_label, email_input)
        
        # Phone
        phone_label = QLabel('Phone')
        phone_input = QLineEdit()
        form_layout.addRow(phone_label, phone_input)
        
        # Gender
        gender_label = QLabel('Gender')
        gender_layout = QHBoxLayout()
        male_radio = QRadioButton('Male')
        female_radio = QRadioButton('Female')
        female_radio.setChecked(True)
        
        gender_layout.addWidget(male_radio)
        gender_layout.addWidget(female_radio)
        
        # Add spacer to push gender selection to the right
        gender_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        
        form_layout.addRow(gender_label, gender_layout)
        
        # Country
        country_label = QLabel('Country')
        country_dropdown = QComboBox()
        country_dropdown.addItems(['Select Country', 'Indonesia', 'USA', 'UK'])
        form_layout.addRow(country_label, country_dropdown)
        
        form_box.setLayout(form_layout)
        main_layout.addWidget(form_box)
        
        # Action Buttons
        action_box = QGroupBox("Actions (horizontal box layout)")
        btn_layout = QHBoxLayout()
        for text in ['Submit', 'Cancel']:
            btn = QPushButton(text)
            btn_layout.addWidget(btn)
        action_box.setLayout(btn_layout)
        main_layout.addWidget(action_box)
        
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserRegistrationForm()
    window.show()
    sys.exit(app.exec_())
