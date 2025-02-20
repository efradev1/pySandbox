from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_serial_dropdown.py_serial_dropdown import PySerialDropDown
from gui.widgets.py_toggle.py_toggle import PyToggle
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        self.themes = Themes().items
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        #Button 1 widget
        self.btn_1_widget = QWidget(self.menu_1)
        self.btn_1_widget.setObjectName(u"btn_1_widget")
        self.btn_1_widget.setMinimumSize(QSize(0, 40))
        self.btn_1_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_1_layout = QVBoxLayout(self.btn_1_widget)
        self.btn_1_layout.setSpacing(0)
        self.btn_1_layout.setObjectName(u"btn_1_layout")
        self.btn_1_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.btn_1_widget)

        # BOX2 for motor 1 label
        self.box02 = QHBoxLayout()
        self.box02.setObjectName(u"box_2_layout")

        # SERIAL PORT DROPDOWN 1
        self.serial_port_dropdown1 = PySerialDropDown(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )

        # Create refresh button for serial ports 1
        self.refresh_ports_btn1 = PyPushButton(
            text="Refresh Ports",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.refresh_ports_btn1.setMaximumHeight(40)

        # Connect the refresh button to the refresh_ports method
        self.refresh_ports_btn1.clicked.connect(self.serial_port_dropdown1.refresh_ports)

        # ADD WIDGETS TO BOX2
        self.box02.addWidget(self.serial_port_dropdown1)
        self.box02.addWidget(self.refresh_ports_btn1)
        self.box02.setAlignment(Qt.AlignTop)

        # Add box2 to vertical layout
        self.verticalLayout.addLayout(self.box02)

        # BOX3 for motor 2 label
        self.box03 = QHBoxLayout()
        self.box03.setObjectName(u"box_3_layout")

        # SERIAL PORT DROPDOWN 2
        self.serial_port_dropdown2 = PySerialDropDown(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )

        # Create refresh button for serial ports 2
        self.refresh_ports_btn2 = PyPushButton(
            text="Refresh Ports",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.refresh_ports_btn2.setMaximumHeight(40)

        # Connect the refresh button to the refresh_ports method
        self.refresh_ports_btn2.clicked.connect(self.serial_port_dropdown2.refresh_ports)  # Corregido de btn1 a btn2

        # ADD WIDGETS TO BOX3
        self.box03.addWidget(self.serial_port_dropdown2)
        self.box03.addWidget(self.refresh_ports_btn2)
        self.box03.setAlignment(Qt.AlignTop)

        # Add box3 to vertical layout
        self.verticalLayout.addLayout(self.box03)

        # Add label_1 after both boxes
        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label_1)

        #Label for menu1   
        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btn_2_widget = QWidget(self.menu_2)
        self.btn_2_widget.setObjectName(u"btn_2_widget")
        self.btn_2_widget.setMinimumSize(QSize(0, 40))
        self.btn_2_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_2_layout = QVBoxLayout(self.btn_2_widget)
        self.btn_2_layout.setSpacing(0)
        self.btn_2_layout.setObjectName(u"btn_2_layout")
        self.btn_2_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_2_widget)

        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.menu_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font-size: 9pt")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)

        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        #self.label_1.setText(QCoreApplication.translate("RightColumn", u"Menu 1 - Right Menu", None))
        self.label_2.setText(QCoreApplication.translate("RightColumn", u"Menu 2 - Right Menu", None))
        self.label_3.setText(QCoreApplication.translate("RightColumn", u"This is just an example menu.\n"
"Add Qt Widgets or your custom widgets here.", None))
    # retranslateUi