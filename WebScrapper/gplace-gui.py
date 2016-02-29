#!/bin/python3

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Gplace.NodeObject import *
import Gplace.icons_rc


class GPlacesDownloader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 50, 700, 700)
        self.setWindowTitle("GPlaces Downloader")

        # Menu
        self.main_menu = self.menuBar()

        # File Menu
        self.menu_file = self.main_menu.addMenu("&File")
        self.action_new = self.create_action("&New...", QKeySequence.New, tip="New a project")
        self.action_open = self.create_action("&Open..", QKeySequence.Open, tip="Open a project")
        self.action_close = self.create_action("&Close", QKeySequence.Close, tip="Close the current project")
        self.action_quit = self.create_action("&Quit", QKeySequence.Quit, activate=self.action_quit,
                                              tip="Close the application")

        # Adding actions
        self.add_actions(self.menu_file, [self.action_new, self.action_open, self.action_close, None, self.action_quit])

        # Toolbar
        self.main_tool = QToolBar()
        self.new_tbn = QPushButton(self.main_tool)
        self.new_tbn.setText("+")
        self.toolBarArea(self.main_tool)

        # project structure
        self.project_tree = QTreeView()
        self.filter_line = QLineEdit()
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.expandingDirections()
        self.vertical_layout.addWidget(self.filter_line)
        self.vertical_layout.addWidget(self.project_tree)
        self.data_widget = QWidget()
        self.data_widget.setLayout(self.vertical_layout)
        # Assign widgets
        self.setCentralWidget(self.data_widget)

        # tem data object
        self.root_node = NodeObject("root")
        self.ch1 = CountryNode("Spain", self.root_node)
        self.ch2 = CountryNode("United Kingdom", self.root_node)
        self.ch3 = CountryNode("Belgium", self.root_node)
        self.ch4 = StateNode("Flandes", self.ch3)

        # Model
        self.project_model = ScrapModel(self.root_node)
        self.project_tree.setModel(self.project_model)

    @staticmethod
    def action_quit():
        """
        Quit the Application
        :return:
        """
        app.quit()

    def create_action(self, text, shortcut=None, activate=None, icon=None, tip=None, check=None):
        """
        Helper function for create QAction and set common params
        :param text: string
        :param shortcut: QKeySequence
        :param activate: function
        :param icon: QIcon
        :param tip: string
        :param check: bool
        :return: QAction
        """
        action = QAction(text, self)
        if icon is not None:
            pass
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
        if check is not None:
            action.setCheckable(check)
        if activate is not None:
            action.triggered.connect(activate)
        return action

    @staticmethod
    def add_actions(target: QMenu, actions: [QAction, ]):
        """
        Helper method for adding QActions to QWindowApplication Menu
        :param target: QMenuBar
        :param actions: list of QActions
        :return: None
        """
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)


class ScrapModel(QAbstractItemModel):
    def __init__(self, root, parent=None):
        super(ScrapModel, self).__init__(parent)
        self._rootNode = root

    def rowCount(self, parent: QModelIndex = None, *args, **kwargs):
        """
        Get child count for the current row
        :param parent: QModelIndex
        :param args:
        :param kwargs:
        :return: int
        """
        if not parent.isValid():
            parent_node = self._rootNode
        else:
            parent_node = parent.internalPointer()
        return parent_node.count()

    def columnCount(self, parent: QModelIndex = None, *args, **kwargs):
        """
        Get number of columns to display in the model
        :param parent: QModelIndex
        :param args:
        :param kwargs:
        :return: int
        """
        return 1

    def data(self, index: QModelIndex, role: int = None):
        """
        Get the object data by its role
        :param index: QModelIndex
        :param role: int
        :return: object
        """
        if not index.isValid():
            return None
        node = index.internalPointer()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if index.column() == 0:
                return node.name
            if index.column() == 1:
                return node.type_info()

        if role == Qt.DecorationRole:
            if index.column() == 0:
                type_info = node.type_info()
                if type_info == "COUNTRY":
                    return QIcon(QPixmap(":/country.png"))
                elif type_info == "STATE":
                    return QIcon(QPixmap(":/state.png"))
                elif type_info == "CITY":
                    return QIcon(QPixmap(":/city.png"))
                elif type_info == "ZIPCODE":
                    return QIcon(QPixmap(":/zip.png"))
                elif type_info == "CATEGORY":
                    pass
                elif type_info == "BUSINESS":
                    return QIcon(QPixmap(":/store.png"))

    def setData(self, index: QModelIndex, value: QVariant, role: int = Qt.EditRole):
        """
        Set name value to the current node
        :param index: QModelIndex
        :param value: QVariant
        :param role: int
        :return: bool
        """
        if index.isValid():
            if role == Qt.EditRole:
                node = index.internalPointer()
                node.name = value
                return True
        return False

    def headerData(self, section: int, orientation: int, role: int = None):
        """
        Get the Header information for the model
        :param section: int
        :param orientation:int
        :param role: int
        :return:
        """
        if section == 0:
            return "Project"

    def flags(self, index: QModelIndex):
        """
        Get the flags for the model data
        :param index: QModelIndex
        :return: int
        """
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def index(self, row, column, parent: QModelIndex = None, *args, **kwargs):
        """
        Get the node given a position
        :param row: int
        :param column: int
        :param parent: QModelIndex
        :param args:
        :param kwargs:
        :return: QModelIndex
        """
        parent_node = self.get_node(parent)
        child = parent_node.child(row)
        if child:
            return self.createIndex(row, column, child)
        else:
            return QModelIndex()

    def parent(self, index: QModelIndex = None):
        """
        Get the parent node
        :param index: QModelIndex
        :return: QModelIndex
        """
        node = self.get_node(index)
        parent_node = node.parent()
        if parent_node == self._rootNode:
            return QModelIndex()
        else:
            return self.createIndex(parent_node.row(), 0, parent_node)

    def get_node(self, index: QModelIndex):
        """
        Helper to check valid node
        :param index: QModelIndex
        :return: NodeObject
        """
        if index.isValid():
            node = index.internalPointer()
            if node:
                return node
        return self._rootNode

    def removeRows(self, position: int, row: int, parent: QModelIndex = None, *args, **kwargs):
        pass

    def insertRows(self, position: int, rows: int, parent: QModelIndex = None, *args, **kwargs):
        """
        Insert a NodeObject in a given position
        :param position: int
        :param rows: int
        :param parent: 
        :param args:
        :param kwargs:
        :return:
        """
        success = False
        parent_node = self.get_node(parent)
        self.beginInsertRows(parent, position, position + rows)
        for row in range(rows):
            child_count = parent_node.count()
            child_node = NodeObject("Untitled", str(child_count))
            success = parent_node.insert(position, child_node)
        self.endInsertRows()
        return success


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = GPlacesDownloader()
    form.show()
    sys.exit(app.exec_())
