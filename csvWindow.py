# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvWindow.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adidion <adidion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/03 15:41:41 by adidion           #+#    #+#              #
#    Updated: 2022/11/08 17:01:14 by adidion          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout
import pyqtgraph as pg
import pandas as pd
import numpy as np


class CSVWindow(QtWidgets.QMainWindow):

#class constructor
	def __init__(self, r):
		super().__init__()
	#read CSV
		data = pd.read_csv(r)

	#dict to store CSV values
		self.d = dict()
		for col in data.columns:
			self.d[col] = np.array(data[col])

	# bool to know if we have to order depending on X axis values
		self.b2o = True

	# setting X values and name (copy to avoid the reference when sorting)
		self.x = self.d[list(self.d.keys())[0]].copy()
		self.x.sort()
		self.x_name = list(self.d.keys())[0]

	# setting Y values and name (copy to avoid the reference when sorting)
		self.y = self.d[list(self.d.keys())[1]].copy()
		self.y = [y for y, _ in sorted(zip(self.y, self.x), key=lambda pair: pair[0])]
		self.y_name = list(self.d.keys())[1]

	# draw window
		self.redraw()

#change Y values / name (copy to avoid the reference when sorting)
	def Y_changed(self, s):
		if self.b2o:
			self.y = self.d[s].copy()
			self.y = [y for y, _ in sorted(zip(self.y, self.x), key=lambda pair: pair[0])]
			self.y_name = s
		else:
			self.y = self.d[s]
		self.redraw()
	
#change X values / name (copy to avoid the reference when sorting)
	def X_changed(self, s):
		if self.b2o:
			self.x = self.d[s].copy()
			self.x.sort()
			self.y = [y for y, _ in sorted(zip(self.y, self.x), key=lambda pair: pair[0])]
		else:
			self.x = self.d[s]
		self.x_name = s
		self.redraw()

#redraw the window when an event as occured
	def redraw(self):
	#creation of widget
		self.graphWidget = pg.PlotWidget()
		
	#settings to sho the grid (not mandatory)
		self.graphWidget.showGrid(x = True, y = True, alpha=0.5)

	#making the self.graphWidget main widget
		self.setCentralWidget(self.graphWidget)

	#init the layout
		self.layout = QtWidgets.QVBoxLayout(self.graphWidget)
		self.layout.addStretch()
		self.layout.setContentsMargins(0,0,0,0)
		self.graphWidget.setLayout(self.layout)

	#creation of button to change Y axis' values
		button1 = QPushButton(self.graphWidget)
		button1.setText("Change Y comparator")
		button1.setGeometry(0, 0, 165, 25)

	#creation of button to change X axis' values
		button2 = QPushButton(self.graphWidget)
		self.layout.addWidget(button2, alignment=QtCore.Qt.AlignRight)
		button2.setText("Change X comparator")
		button2.setGeometry(0, 0, 165, 25)

	#adding legend
		self.graphWidget.addLegend()
 
	#set name for y axis
		self.graphWidget.setLabel('left', self.y_name, units ='y')

	#set name for x axis
		self.graphWidget.setLabel('bottom', self.x_name, units ='x')


	#button's event dealer
		button1.clicked.connect(self.button1_clicked)
		button2.clicked.connect(self.button2_clicked)

	#plot of x/y values
		self.graphWidget.plot(self.x, self.y)
	
#function when Y button is clicked
	def button1_clicked(self, s):
	#creation of choices of button
		box1 = QComboBox()

	#add current item at first
		box1.addItem(self.y_name)

	#add other choices depending of columns in CSV
		for i in self.d.keys():
			if i != self.y_name:
				box1.addItem(i)

	#layout for choices
		if self.layout.count() == 2:
			self.layout.addWidget(box1)
		self.graphWidget.setLayout(self.layout)
		
	#event dealer when clicking on a choice
		box1.currentTextChanged.connect(self.Y_changed)

#function when x button is clicked
	def button2_clicked(self, s):
	#creation of widget
		box1 = QComboBox()

	#add current item at first
		box1.addItem(self.x_name)

	#add other choices depending of columns in CSV
		for i in self.d.keys():
			if i != self.x_name:
				box1.addItem(i)

	#layout for choices
		if self.layout.count() == 2:
			self.layout.addWidget(box1)
		self.graphWidget.setLayout(self.layout)
		
	#event dealer when clicking on a choice
		box1.currentTextChanged.connect(self.X_changed)

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Space:
			self.order()
		
	def order(self):
		if not self.b2o:
			self.y = self.d[self.y_name].copy()
			self.y = [y for y, _ in sorted(zip(self.y, self.x), key=lambda pair: pair[0])]
			self.x = self.d[self.x_name].copy()
			self.x.sort()
			self.y = [y for y, _ in sorted(zip(self.y, self.x), key=lambda pair: pair[0])]
			self.b2o = True
		else:
			self.y = self.d[self.y_name]
			self.x = self.d[self.x_name]
			self.b2o = False
		self.redraw()