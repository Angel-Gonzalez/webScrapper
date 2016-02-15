import sys
import xml.etree.ElementTree
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 50, 500, 700)
        self.setWindowTitle("Scrapper")
        self.setWindowIcon(QIcon("./res/img/turpial.png"))

        # Dock Widget
        self.main_dock = QDockWidget(self)
        self.main_dock.setObjectName("main_dock")
        self.main_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        # Inspect Url Group
        self.inspect_url_cpg = QGroupBox()
        self.inspect_url_cpg.setObjectName("inspect_url_cpg")
        self.inspect_url_cpg.setTitle("Root Url")
        self.inspect_url_vbl = QVBoxLayout()
        self.inspect_url_vbl.expandingDirections()
        self.inspect_url_hbl = QHBoxLayout()
        self.inspect_url_hbl.expandingDirections()
        self.inspect_url_lbl = QLabel("Inspect Url")
        self.inspect_url_tli = QLineEdit()
        self.inspect_url_btn = QPushButton("inspect")
        self.root_url_tmv = QTreeView()
        self.inspect_group = QWidget()

        # adding widget
        self.inspect_group.setLayout(self.inspect_url_hbl)
        self.inspect_url_hbl.addWidget(self.inspect_url_lbl)
        self.inspect_url_hbl.addWidget(self.inspect_url_tli)
        self.inspect_url_hbl.addWidget(self.inspect_url_btn)
        self.inspect_url_vbl.addWidget(self.inspect_group)
        self.inspect_url_vbl.addWidget(self.root_url_tmv)
        self.inspect_url_cpg.setLayout(self.inspect_url_vbl)
        self.setCentralWidget(self.inspect_url_cpg)

        self.show()


class DOMTree(QAbstractListModel):
    def __init__(self, element=None, qobject_parent=None):
        super().__init__(qobject_parent)
        self.__dom = element

    def parse(self, dom):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
