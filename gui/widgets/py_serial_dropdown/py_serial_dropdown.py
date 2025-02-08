# ///////////////////////////////////////////////////////////////
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts.
#
# ///////////////////////////////////////////////////////////////

from qt_core import *
import serial.tools.list_ports

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QComboBox {{
    background-color: {_bg_color};
    border-radius: {_radius}px;
    border: {_border_size}px solid transparent;
    padding-left: 10px;
    padding-right: 10px;
    color: {_color};
    min-height: 28px;
}}

QComboBox:hover {{
    border: {_border_size}px solid {_context_color};
}}

QComboBox:focus {{
    border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}

QComboBox::drop-down {{
    border: none;
    width: 20px;
    height: 20px;
    margin-right: 5px;
}}

QComboBox::down-arrow {{
    image: url(images/down_arrow.png);
    width: 12px;
    height: 12px;
}}

QComboBox QAbstractItemView {{
    background-color: {_bg_color};
    padding: 10px;
    selection-background-color: {_context_color};
    selection-color: {_selection_color};
    border-radius: {_radius}px;
}}
'''

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

        # Set placeholder text
        self.setPlaceholderText("Select COM Port")
        
        # Load available ports
        self.refresh_ports()

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            border_size,
            color,
            selection_color,
            bg_color,
            bg_color_active,
            context_color
        )

    def refresh_ports(self):
        """Refresh the list of available serial ports"""
        self.clear()  # Clear existing items
        ports = serial.tools.list_ports.comports()
        
        if not ports:
            self.addItem("No COM ports available")
            self.setEnabled(False)
        else:
            self.setEnabled(True)
            for port in ports:
                # Add port with description as tooltip
                port_info = f"{port.device} - {port.description}"
                self.addItem(port_info)
                tooltip = f"Device: {port.device}\nDescription: {port.description}"
                if port.manufacturer:
                    tooltip += f"\nManufacturer: {port.manufacturer}"
                if port.product:
                    tooltip += f"\nProduct: {port.product}"
                self.setItemData(self.count() - 1, tooltip, Qt.ToolTipRole)

    def get_current_port(self):
        """Get the currently selected port name only"""
        if self.currentText() != "No COM ports available":
            return self.currentText().split(" - ")[0]
        return None

    def set_stylesheet(
        self,
        radius,
        border_size,
        color,
        selection_color,
        bg_color,
        bg_color_active,
        context_color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,
            _border_size = border_size,           
            _color = color,
            _selection_color = selection_color,
            _bg_color = bg_color,
            _bg_color_active = bg_color_active,
            _context_color = context_color
        )
        self.setStyleSheet(style_format)