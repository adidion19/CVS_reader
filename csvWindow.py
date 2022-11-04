# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvWindow.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adidion <adidion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/03 15:41:41 by adidion           #+#    #+#              #
#    Updated: 2022/11/04 18:15:10 by adidion          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QComboBox, QVBoxLayout, QWidget, QPushButton
import pyqtgraph as pg
import pandas as pd
import numpy as np


class CSVWindow(QtWidgets.QMainWindow):

	def __init__(self, r):
		super().__init__()
		self.data = pd.read_csv(r)
		self.d = dict()
		for col in self.data.columns:
			self.d[col] = np.array(self.data[col])
		self.graphWidget = pg.PlotWidget()
		self.button1 = QPushButton(self.graphWidget)
		self.button1.setText("Change Y comparator")
		self.setCentralWidget(self.graphWidget)

		self.button1.clicked.connect(self.button1_clicked)
		self.x = self.d[list(self.d.keys())[1]]
		self.x.sort()
		self.x_name = list(self.d.keys())[1]
		self.y = self.d[list(self.d.keys())[2]]
		self.y_name = list(self.d.keys())[2]

		# plot data: x, y values
		self.graphWidget.plot(self.x, self.y)

	def Y_changed(self, s):
		self.y = self.d[s]
		self.redraw()

	def redraw(self):
		self.graphWidget = pg.PlotWidget()
		self.setCentralWidget(self.graphWidget)
		self.button1 = QPushButton(self.graphWidget)
		self.button1.setText("Change Y comparator")
		self.setCentralWidget(self.graphWidget)
		self.button1.clicked.connect(self.button1_clicked)
		self.graphWidget.plot(self.x, self.y)
	
	def button1_clicked(self, s):
		box1 = QComboBox()
		box1.addItem(self.y_name)
		for i in self.d.keys():
			if i != self.y_name:
				box1.addItem(i)
		# container = QWidget()
		layout = QVBoxLayout()
		layout.addWidget(box1)
		self.graphWidget.setLayout(layout)
		# self.setCentralWidget(container)
		box1.currentTextChanged.connect(self.Y_changed)