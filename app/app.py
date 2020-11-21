import sys

from PyQt5 import sip
from PyQt5.QtWidgets import *
from runlogin import Login


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())
