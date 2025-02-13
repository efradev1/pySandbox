# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
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
        self.btn_1_widget = QWidget(self.menu_1)
        self.btn_1_widget.setObjectName(u"btn_1_widget")
        self.btn_1_widget.setMinimumSize(QSize(0, 40))
        self.btn_1_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_1_layout = QVBoxLayout(self.btn_1_widget)
        self.btn_1_layout.setSpacing(0)
        self.btn_1_layout.setObjectName(u"btn_1_layout")
        self.btn_1_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_1_widget)

        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        # /////////////////////////
        #Box1 for Toggle and label "Arm"
        self.box01 = QHBoxLayout()
        self.box01.setObjectName(u"box_1_layout")
        #Adding box 1 to vertical layout
        self.verticalLayout.addLayout(self.box01)

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )
        text_label = QLabel("Arm")
        text_label.setStyleSheet("color: white; font-size: 20px;")
        text_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Add widgets to Box1
        self.box01.addWidget(self.toggle_button)
        self.box01.addWidget(text_label)

        # /////////////////////////

        # /////////////////////////
        #BOX2 for motor 1 label
        self.box02 = QHBoxLayout()
        self.box02.setObjectName(u"box_2_layout")

        #Adding box 2 to vertical layout
        self.verticalLayout.addLayout(self.box02)

        #Label for Motor 1
        self.label_motor1 = QLabel("Motor 1:")
        self.label_motor1.setObjectName(u"label_motor1")
        font = QFont()
        font.setPointSize(16)
        self.label_motor1.setFont(font)
        self.label_motor1.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_motor1.setAlignment(Qt.AlignLeft)
        #Adding the label to box 2
        self.box02.addWidget(self.label_motor1)

        #Label for motor status
        self.label_motor_status = QLabel("Disconnected")
        self.label_motor_status.setObjectName(u"label_motor1")
        font = QFont()
        font.setPointSize(16)
        self.label_motor_status.setFont(font)
        self.label_motor_status.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_motor_status.setAlignment(Qt.AlignRight)
        #Adding the label to box 2
        self.box02.addWidget(self.label_motor_status)





        # /////////////////////////
        # Create frame 1
        self.frame_01 = QFrame()
        self.frame_01.setFrameShape(QFrame.StyledPanel)
        self.frame_01.setFrameShadow(QFrame.Raised)
        self.frame_01_layout = QVBoxLayout()  # You can choose QHBoxLayout or QVBoxLayout as needed
        self.frame_01.setLayout(self.frame_01_layout)
        self.frame_01.setStyleSheet("border: 1px solid white;")

        # # Modifying the frame's position
        # self.verticalLayout.insertWidget(1, self.frame_01)
        
        # Set fixed height if needed
        self.frame_01.setFixedHeight(230)

        # Add frame 1 to the layout
        self.verticalLayout.addWidget(self.frame_01)

        # Create frame 2
        self.frame_02 = QFrame()
        self.frame_02.setFrameShape(QFrame.StyledPanel)
        self.frame_02.setFrameShadow(QFrame.Raised)
        self.frame_02_layout = QVBoxLayout()  # You can choose QHBoxLayout or QVBoxLayout as needed
        self.frame_02.setLayout(self.frame_01_layout)
        self.frame_02.setStyleSheet("border: 1px solid white;")

        # Set fixed height if needed
        self.frame_02.setFixedHeight(230)

        # Add frame 1 to the layout
        self.verticalLayout.addWidget(self.frame_02)


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

