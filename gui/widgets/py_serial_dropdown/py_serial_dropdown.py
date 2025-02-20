from qt_core import *
import serial.tools.list_ports

class PySerialDropDown(QComboBox):
    def __init__(
        self,
        radius = 8,
        border_size = 2,
        color = "#FFF",
        selection_color = "#FFF", 
        bg_color = "#333",
        bg_color_active = "#222",
        context_color = "#00ABE8"
    ):
        super().__init__()
        
        # PARAMETERS
        self.radius = radius
        self.border_size = border_size
        self.color = color
        self.selection_color = selection_color
        self.bg_color = bg_color
        self.bg_color_active = bg_color_active
        self.context_color = context_color

        # Apply style
        self.set_style()
        
        # Connect signal
        self.currentIndexChanged.connect(self.selection_changed)
        
        # Initialize ports
        self.initialize_ports()

    def refresh_ports(self):
        """Refresh the list of available ports"""
        self.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.addItem(port.device)

    def initialize_ports(self):
        """Initial port population"""
        self.refresh_ports()

    def selection_changed(self, index):
        if index >= 0:
            selected_port = self.currentText()
            print(f"Selected port: {selected_port}")

    def set_style(self):
        style = f"""
        QComboBox {{
            background-color: {self.bg_color};
            border-radius: {self.radius}px;
            border: {self.border_size}px solid {self.context_color};
            padding-left: 10px;
            color: {self.color};
            min-height: 40px;
        }}
        QComboBox:hover {{
            background-color: {self.bg_color_active};
        }}
        QComboBox::drop-down {{
            border: none;
            width: 20px;
            height: 20px;
            margin: 5px;
        }}
        QComboBox::down-arrow {{
            image: url(:/icons/images/icons/cil-arrow-bottom.png);
        }}
        QComboBox QAbstractItemView {{
            background-color: {self.bg_color};
            padding: 10px;
            selection-background-color: {self.bg_color_active};
            color: {self.selection_color};
        }}
        """
        self.setStyleSheet(style)
