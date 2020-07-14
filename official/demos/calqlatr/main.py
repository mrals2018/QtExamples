from Qt.QtCore import QCoreApplication, Qt, QUrl
from Qt.QtGui import QGuiApplication
from Qt.QtQuick import QQuickView

import calqlatr_rc  # noqa: F401


def main():
    import sys

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QCoreApplication.setOrganizationName("QtExamples")

    app = QGuiApplication(sys.argv)

    view = QQuickView()
    view.engine().quit.connect(app.quit)
    view.setSource(QUrl("qrc:/demos/calqlatr/calqlatr.qml"))
    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
