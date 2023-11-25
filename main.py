import io
import sys

import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
import sys
from random import randint
from PyQt5 import uic

template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>170</y>
      <width>421</width>
      <height>231</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class MyWidget(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)  # Загружаем дизайн
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        a, b, c, d = randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255)
        # QColor(255, 0, 0, 127)
        qp.setPen(QPen(QColor(a, b, c, d),  8, Qt.SolidLine))
        n = randint(1, 400)
        qp.drawEllipse(randint(1, 600), randint(1, 600), n, n)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())