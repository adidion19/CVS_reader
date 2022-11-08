# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    chooseFile.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adidion <adidion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/03 15:41:46 by adidion           #+#    #+#              #
#    Updated: 2022/11/08 17:08:56 by adidion          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PyQt5.QtWidgets import QFileDialog, QWidget
import sys

class ChooseFile(QWidget):

#class constructor
	def __init__(self):
		super().__init__()
		self.title = 'Choose your CSV file.'

#init UI
	def initUI(self):
		self.setWindowTitle(self.title)
	#try to open
		try:
			r = self.openCsvFile()
		except FileExistsError:
			sys.exit()
		return r

#open CSV
	def openCsvFile(self):
		#set display options
		options = QFileDialog.Options()
		#filtering the accepted files
		fileName = QFileDialog.getOpenFileName(self,"Choose a CSV file", "","CSV Files (.csv), *.csv", options=options)
		if fileName:
			return fileName[0]
		raise FileExistsError