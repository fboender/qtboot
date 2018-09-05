import sys
import signal
from PyQt5.Qt import *


class QTBoot(QMainWindow):
    def __init__(self, app_vendor, app_name, args, icon=None, toolbar_items=None):
        self.app_vendor = app_vendor
        self.app_name = app_name
        self.args = args
        self.icon = icon
        self.toolbar_items = toolbar_items

        # Make sure ctrl-c on the commandline stops the application
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        self.app = QApplication(args)
        self.settings = QSettings(self.app_vendor, self.app_name)
        self.central_widget = QWidget()

        QMainWindow.__init__(self)
        self.setWindowTitle(self.app_name)
        if self.icon is not None:
            self.setWindowIcon(QIcon(self.icon))
        geometry = self.settings.value("geometry")
        if geometry is not None:
            self.restoreGeometry(geometry);
        self.setCentralWidget(self.central_widget)

        # Create toolbar
        if self.toolbar_items is not None:
            self.toolbar = self.addToolBar('toolbar')
            for toolbar_item in self.toolbar_items:
                action = QAction(QIcon.fromTheme(toolbar_item["icon"]),
                                 toolbar_item["label"],
                                 self)
                action.setData(toolbar_item["id"])
                if toolbar_item["type"] == "check":
                    action.setCheckable(True)
                if toolbar_item["shortcut"] is not None:
                    action.setShortcut(toolbar_item["shortcut"])
                event_cb = getattr(self, "_ev_{}".format(toolbar_item["event"]))
                action.triggered.connect(event_cb)
                self.toolbar.addAction(action)

    def run(self):
        self.show()
        self.app.exec_()

    def closeEvent(self, event):
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.sync()
        QCoreApplication.quit()
