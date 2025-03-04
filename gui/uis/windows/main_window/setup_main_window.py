from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from main import MainWindow
from . functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

from gui.widgets.py_serial_dropdown.py_serial_dropdown import PySerialDropDown

# IMPORT MAIN WINDOW CLASS

# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "SandBox",
            "btn_tooltip" : "SandBox",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_widgets.svg",
            "btn_id" : "btn_widgets",
            "btn_text" : "Show Custom Widgets",
            "btn_tooltip" : "Show custom widgets",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_add_user.svg",
            "btn_id" : "btn_add_user",
            "btn_text" : "Add Users",
            "btn_tooltip" : "Add users",
            "show_top" : True,
            "is_active" : False
        },
        # {
        #     "btn_icon" : "icon_file.svg",
        #     "btn_id" : "btn_new_file",
        #     "btn_text" : "New File",
        #     "btn_tooltip" : "Create new file",
        #     "show_top" : True,
        #     "is_active" : False
        # },
        # {
        #     "btn_icon" : "icon_emoticons.svg",
        #     "btn_id" : "btn_new_file",
        #     "btn_text" : "Test Button",
        #     "btn_tooltip" : "Efraín's Test Button",
        #     "show_top" : True,
        #     "is_active" : False
        # },
        # {
        #     "btn_icon" : "icon_folder_open.svg",
        #     "btn_id" : "btn_open_file",
        #     "btn_text" : "Open File",
        #     "btn_tooltip" : "Open file",
        #     "show_top" : True,
        #     "is_active" : False
        # },
        # {
        #     "btn_icon" : "icon_save.svg",
        #     "btn_id" : "btn_save",
        #     "btn_text" : "Save File",
        #     "btn_tooltip" : "Save file",
        #     "show_top" : True,
        #     "is_active" : False
        # },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_info",
            "btn_text" : "Information",
            "btn_tooltip" : "Open informations",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "Settings",
            "btn_tooltip" : "Open settings",
            "show_top" : False,
            "is_active" : False
        }
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # SETTINGS LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.left_btn_1 = PyPushButton(
            text="Btn 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        # BTN 2
        self.left_btn_2 = PyPushButton(
            text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        # BTN 3 - Default QPushButton
        self.left_btn_3 = QPushButton("Default QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        # BTN 4 - Default QPushButton
        self.left_btn_4 = PyPushButton(
        text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_4.setIcon(self.icon)
        self.left_btn_4.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_4)

        # PAGES
        # ///////////////////////////////////////////////////////////////

        # PAGE 1 - ADD LOGO TO MAIN PAGE

        # Create a horizontal layout for the top controls
        self.top_layout = QHBoxLayout()

        # Add the horizontal layout to the page layout
        self.ui.load_pages.page_1_layout.addLayout(self.top_layout)

        ############ PAGE 1 LEFT FRAME ############

        # Create the left frame
        self.left_frame = QFrame()
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.left_frame_layout = QVBoxLayout()  # You can choose QHBoxLayout or QVBoxLayout as needed
        self.left_frame.setLayout(self.left_frame_layout)
        self.left_frame.setStyleSheet("border: 1px solid white;")

        # Add the frames to the top layout
        self.top_layout.addWidget(self.left_frame)

        #CREATING TOP ROW01
        self.top_row01 = QHBoxLayout()
        self.top_row01.setObjectName(u"row_1_layout")
        #ADDING THE TOP ROW TO THE LEFT FRAME LAYOUT
        self.left_frame_layout.addLayout(self.top_row01)

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )
        text_label = QLabel("Arm")
        text_label.setStyleSheet("color: white;")
        text_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Add widgets to the right frame (example widget)
        self.top_row01.addWidget(self.toggle_button)
        self.top_row01.addWidget(text_label)

        #Connecting the toggle with a function
        self.toggle_button.clicked.connect(self.packman)

        #CREATING TOP ROW02
        self.top_row02 = QHBoxLayout()
        self.top_row02.setObjectName(u"row_2_layout")

        #ADDING THE TOP ROW TO THE LEFT FRAME LAYOUT
        self.left_frame_layout.addLayout(self.top_row02)

        #Label for Motor 1
        self.label_motor1 = QLabel("Motor 1:")
        self.label_motor1.setObjectName(u"label_motor1")
        font = QFont()
        font.setPointSize(16)
        self.label_motor1.setFont(font)
        self.label_motor1.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_motor1.setAlignment(Qt.AlignLeft)
        #Adding the label to box 2
        self.top_row02.addWidget(self.label_motor1)

        #Label for motor status
        self.label_motor_status = QLabel("Disconnected")
        self.label_motor_status.setObjectName(u"label_motor1")
        font = QFont()
        font.setPointSize(16)
        self.label_motor_status.setFont(font)
        self.label_motor_status.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_motor_status.setAlignment(Qt.AlignRight)
        #Adding the label to box 2
        self.top_row02.addWidget(self.label_motor_status)

        # /////////////////////////
        # Create frame 1 for error and encoder box and labels
        self.frame_01 = QFrame()
        self.frame_01.setFrameShape(QFrame.StyledPanel)
        self.frame_01.setFrameShadow(QFrame.Raised)
        self.frame_01_layout = QVBoxLayout()  # Changed to QVBoxLayout for vertical arrangement
        self.frame_01.setLayout(self.frame_01_layout)
        #self.frame_01.setStyleSheet("border: 1px solid white;")

        # Set fixed height if needed
        self.frame_01.setFixedHeight(100)

        # Create labels for Error and Encoder 1
        self.label_error1 = QLabel("Error: ")
        self.label_error1.setObjectName(u"label_error1")
        self.label_error1.setFont(font)
        self.label_error1.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_error1.setAlignment(Qt.AlignLeft)
        self.label_error1.setFixedHeight(30)

        self.label_encoder1 = QLabel("Encoder: ")
        self.label_encoder1.setObjectName(u"label_encoder1")
        self.label_encoder1.setFont(font)
        self.label_encoder1.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_encoder1.setAlignment(Qt.AlignLeft)
        self.label_encoder1.setFixedHeight(30)

        # Add labels to frame_01
        self.frame_01_layout.addWidget(self.label_error1)
        self.frame_01_layout.addWidget(self.label_encoder1)

        # Add frame 1 to the layout
        self.left_frame_layout.addWidget(self.frame_01)

        # Set alignment for the widgets in the horizontal layout
        self.left_frame_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        #CREATING TOP ROW03
        self.top_row03 = QHBoxLayout()
        self.top_row03.setObjectName(u"row_2_layout")

        #ADDING THE TOP ROW TO THE LEFT FRAME LAYOUT
        self.left_frame_layout.addLayout(self.top_row03)

        #Label for Motor 2
        self.label_motor2 = QLabel("Motor 2:")
        self.label_motor2.setObjectName(u"label_motor2")
        font = QFont()
        font.setPointSize(16)
        self.label_motor2.setFont(font)
        self.label_motor2.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_motor2.setAlignment(Qt.AlignLeft)

        #Adding the label to box 3
        self.top_row03.addWidget(self.label_motor2)

        #Label for motor status
        self.label_motor_status = QLabel("Disconnected")
        self.label_motor_status.setObjectName(u"label_motor2")
        font = QFont()
        font.setPointSize(16)
        self.label_motor_status.setFont(font)
        self.label_motor_status.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_motor_status.setAlignment(Qt.AlignRight)
        #Adding the label to box 3
        self.top_row03.addWidget(self.label_motor_status)

        # Create frame 2 for error and encoder box and labels
        self.frame_02 = QFrame()
        self.frame_02.setFrameShape(QFrame.StyledPanel)
        self.frame_02.setFrameShadow(QFrame.Raised)
        self.frame_02_layout = QVBoxLayout()  # Changed to QVBoxLayout for vertical arrangement
        self.frame_02.setLayout(self.frame_02_layout)
        #self.frame_02.setStyleSheet("border: 1px solid white;")

        # Set fixed height if needed
        self.frame_02.setFixedHeight(100)

        # Create labels for Error and Encoder 2
        self.label_error2 = QLabel("Error: ")
        self.label_error2.setObjectName(u"label_error2")
        self.label_error2.setFont(font)
        self.label_error2.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_error2.setAlignment(Qt.AlignLeft)
        self.label_error2.setFixedHeight(30)

        self.label_encoder2 = QLabel("Encoder:")
        self.label_encoder2.setObjectName(u"label_encoder2")
        self.label_encoder2.setFont(font)
        self.label_encoder2.setStyleSheet(u"color: white; font-size: 20px;")
        self.label_encoder2.setAlignment(Qt.AlignLeft)
        self.label_encoder2.setFixedHeight(30)

        # Add labels to frame_01
        self.frame_02_layout.addWidget(self.label_error2)
        self.frame_02_layout.addWidget(self.label_encoder2)

        # Add frame 2 to the layout
        self.left_frame_layout.addWidget(self.frame_02)

        ############ PAGE 1 RIGHT FRAME ############

        # Create the right frame
        self.right_frame = QFrame()
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.right_frame_layout = QVBoxLayout()  # You can choose QHBoxLayout or QVBoxLayout as needed
        self.right_frame.setLayout(self.right_frame_layout)
        self.right_frame.setStyleSheet("border: 1px solid white;")

        # Add the frames to the top layout
        self.top_layout.addWidget(self.right_frame)

        # CIRCULAR PROGRESS 3 PAGE 1 RIGHT
        self.circular_progress_3 = PyCircularProgress(
            value = 75,
            progress_width = 2,
            progress_color = self.themes["app_color"]["pink"],
            text_color = self.themes["app_color"]["white"],
            font_size = 14,
            bg_color = self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_3.setFixedSize(140,140)

        # Add widgets to the right frame (example widget)
        self.right_frame_layout.addWidget(self.circular_progress_3)

        # Set alignment for the widgets in the frame
        self.right_frame_layout.setAlignment(Qt.AlignTop | Qt.AlignRight)

        # PAGE 2
        # CIRCULAR PROGRESS 1
        self.circular_progress_1 = PyCircularProgress(
            value = 80,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["text_title"],
            font_size = 14,
            bg_color = self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_1.setFixedSize(200,200)

        # CIRCULAR PROGRESS 2
        self.circular_progress_2 = PyCircularProgress(
            value = 45,
            progress_width = 4,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["context_color"],
            font_size = 14,
            bg_color = self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_2.setFixedSize(160,160)

        # CIRCULAR PROGRESS 3
        self.circular_progress_3 = PyCircularProgress(
            value = 75,
            progress_width = 2,
            progress_color = self.themes["app_color"]["pink"],
            text_color = self.themes["app_color"]["white"],
            font_size = 14,
            bg_color = self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_3.setFixedSize(140,140)

        # PY SLIDER 1
        self.vertical_slider_1 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_four"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_1.setMinimumHeight(100)

        # PY SLIDER 2
        self.vertical_slider_2 = PySlider(
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_2.setMinimumHeight(100)

        # PY SLIDER 3
        self.vertical_slider_3 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_four"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_3.setOrientation(Qt.Horizontal)
        self.vertical_slider_3.setMaximumWidth(200)

        # PY SLIDER 4
        self.vertical_slider_4 = PySlider(
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_4.setOrientation(Qt.Horizontal)
        self.vertical_slider_4.setMaximumWidth(200)

        # ICON BUTTON 1
        self.icon_button_1 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_heart.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "Icon button - Heart",
            width = 40,
            height = 40,
            radius = 20,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )

        # ICON BUTTON 2
        self.icon_button_2 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN with tooltip",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["green"],
        )

        # ICON BUTTON 3
        self.icon_button_3 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN actived! (is_actived = True)",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["context_color"],
            is_active = True
        )

        # ICON BUTTON 4
        self.icon_button_4 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN actived! (is_actived = True)",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["context_color"],
            is_active = True
        )

        # PUSH BUTTON 1
        self.push_button_1 = PyPushButton(
            text = "Button Without Icon",
            radius  =8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.push_button_1.setMinimumHeight(40)

        # PUSH BUTTON 2
        self.push_button_2 = PyPushButton(
            text = "Button With Icon",
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.icon_2 = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.push_button_2.setMinimumHeight(40)
        self.push_button_2.setIcon(self.icon_2)

        # PY LINE EDIT
        self.line_edit = PyLineEdit(
            text = "",
            place_holder_text = "Place holder text",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit.setMinimumHeight(30)

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )

        # TABLE WIDGETS
        self.table_widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("NAME")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("NICK")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("PASS")

        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)

        for x in range(10):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number) # Insert row
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str("Wanderson"))) # Add name
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str("vfx_on_fire_" + str(x)))) # Add nick
            self.pass_text = QTableWidgetItem()
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            self.pass_text.setText("12345" + str(x))
            self.table_widget.setItem(row_number, 2, self.pass_text) # Add pass
            self.table_widget.setRowHeight(row_number, 22)

        # ADD WIDGETS
        self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_1)
        self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_2)
        self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_3)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_1)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_2)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_3)
        self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_4)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_1)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_2)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_3)

        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_4)

        self.ui.load_pages.row_3_layout.addWidget(self.push_button_1)
        self.ui.load_pages.row_3_layout.addWidget(self.push_button_2)
        self.ui.load_pages.row_3_layout.addWidget(self.toggle_button)
        self.ui.load_pages.row_4_layout.addWidget(self.line_edit)
        self.ui.load_pages.row_5_layout.addWidget(self.table_widget)

        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1", 
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)

        

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)