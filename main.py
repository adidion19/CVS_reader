# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adidion <adidion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/03 15:41:24 by adidion           #+#    #+#              #
#    Updated: 2022/11/04 17:34:11 by adidion          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PyQt5.QtWidgets import QApplication
import sys
from chooseFile import ChooseFile
# from listOfIndex import ListOfIndex
from csvWindow import CSVWindow

def main():
	app = QApplication(sys.argv)
	a = ChooseFile()
	r = a.initUI()
	# a = ListOfIndex()
	# tab = a.getTab(r)
	# a.show()
	main = CSVWindow(r)
	main.show()
	main.setWindowTitle("CSV Viewer")
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()