# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adidion <adidion@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/03 15:41:24 by adidion           #+#    #+#              #
#    Updated: 2022/11/08 14:32:23 by adidion          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from PyQt5.QtWidgets import QApplication
import sys
from chooseFile import ChooseFile
from csvWindow import CSVWindow

def main():
	app = QApplication(sys.argv)
	a = ChooseFile()
	r = a.initUI()
	main = CSVWindow(r)
	main.show()
	main.setWindowTitle("CSV Viewer")
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()