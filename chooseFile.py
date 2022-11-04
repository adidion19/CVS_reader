# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    chooseFile.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adidion <adidion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/03 15:41:46 by adidion           #+#    #+#              #
#    Updated: 2022/11/04 11:15:24 by adidion          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PyQt5.QtWidgets import QFileDialog, QWidget
import sys

class ChooseFile(QWidget):

	def __init__(self):
		super().__init__()
		self.title = 'Choose your CSV file.'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		try:
			r = self.openCvsFile()
		except FileExistsError:
			sys.exit()
		return r

	def openCvsFile(self):
		options = QFileDialog.Options()
		fileName = QFileDialog.getOpenFileName(self,"Choose a CSV file", "","CSV Files (.csv), *.csv", options=options)
		if fileName:
			return fileName[0]
		raise FileExistsError