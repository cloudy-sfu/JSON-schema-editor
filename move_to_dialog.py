from PyQt6.QtWidgets import *

from is_type import is_type


class MoveToDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Destination selector")
        layout = QVBoxLayout()
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Node", ""])
        self.path = []  # identical location to selected node
        self.tree.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        layout.addWidget(self.tree)

        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def refresh_tree(self, schema):
        self.tree.clear()
        root_item = QTreeWidgetItem(["root", ""])
        self.tree.addTopLevelItem(root_item)
        for field, property_ in schema.get("properties", {}).items():
            json_object_to_tree(
                root_item,
                field,
                property_,
            )
        self.tree.expandAll()
        self.tree.resizeColumnToContents(0)


def json_object_to_tree(parent, field_name, property_, is_array_item=False):
    assert isinstance(parent, QTreeWidgetItem), "Parent node is not a tree item."

    if not (is_type(property_.get("type"), "object") or
            is_type(property_.get("type"), "array")
    ):
        return

    if is_array_item:
        col_0 = "<element>"
        col_1 = "E"
    else:
        col_0 = field_name
        col_1 = ""
    self_ = QTreeWidgetItem([col_0, col_1])
    parent.addChild(self_)
    if "properties" in property_.keys():
        for sub_field, sub_property in property_["properties"].items():
            json_object_to_tree(
                self_,
                sub_field,
                sub_property,
            )
    elif "items" in property_.keys():
        json_object_to_tree(
            self_,
            None,
            property_["items"],
            is_array_item=True
        )
