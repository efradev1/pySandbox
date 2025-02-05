# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA (Original style)
# Modified for QComboBox
# ///////////////////////////////////////////////////////////////

from qt_core import *

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

class PyDropDownBox(QComboBox):
    def __init__(
        self,
        items = [],
        place_holder_text = "",
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
        if place_holder_text:
            self.setPlaceholderText(place_holder_text)
        
        # Add initial items
        self.addItems(items)

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

    # SET STYLESHEET
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

    # Add methods to manage items
    def add_item(self, item):
        """Add a single item to the dropdown"""
        self.addItem(str(item))

    def add_items(self, items):
        """Add multiple items to the dropdown"""
        self.addItems([str(item) for item in items])

    def clear_items(self):
        """Clear all items from the dropdown"""
        self.clear()

    def get_current_item(self):
        """Get the currently selected item"""
        return self.currentText()

    def set_current_item(self, text):
        """Set the current item by text"""
        index = self.findText(str(text))
        if index >= 0:
            self.setCurrentIndex(index)
