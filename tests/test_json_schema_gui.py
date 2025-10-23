import json
import sys

from PyQt6.QtWidgets import QApplication

from main import SchemaEditor

app = QApplication([])
app.setStyleSheet(
    f'QWidget {{'
    f'    font-family: "Microsoft YaHei", Calibri, Ubuntu; '
    f'    font-size: 12pt;'
    f'}}'
)
myw = SchemaEditor()
with open("tests/json_schema/user_profile.json", "r", encoding="utf-8") as f:
    schema = json.load(f)
myw.schema = schema
myw.filepath = "tests/json_schema/user_profile.json"
myw.refresh_tree()
myw.show()
sys.exit(app.exec())
