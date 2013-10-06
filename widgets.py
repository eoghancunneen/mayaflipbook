#==============================================================================
#
#  Copyright (c) 2012-13 Eoghan Patrick Cunneen
#  All rights reserved.
#
#  This file contains confidential and proprietary source code, belonging to
#  Eoghan Patrick Cunneen. Its contents may not be disclosed to third parties,
#  copied or duplicated in any form, in whole or in part, without prior
#  permission.
#
#===============================================================================
""" This module contains the individual widgets that combine to make the
flipbook UI.
"""

# Import stdlib modules:

# Import third party modules:
from PyQt4 import QtCore
from PyQt4 import QtGui


class FrameRangeWidget(QtGui.QGroupBox):
	"""A simple widget to let the user set the frame range."""
	def __init__(self, parent=None):
		super(FrameRangeWidget, self).__init__(parent=None)
		self.lb_startframe = QtGui.QLabel('Start Frame')
		self.lb_endframe = QtGui.QLabel('End Frame')
		self.sb_startframe = QtGui.QSpinBox()
		self.sb_endrame = QtGui.QSpinBox()
		self.pb_setframerange = QtGui.QPushButton('Set Framerange')
		self._setup_ui()

	def _setup_ui(self):
		layout = QtGui.QVBoxLayout()
		separator = QtGui.QLabel('-')
		horizontal_layout = QtGui.QHBoxLayout()
		formlayout_start = QtGui.QFormLayout()
		formlayout_end = QtGui.QFormLayout()
		layout.addLayout(horizontal_layout)
		layout.addWidget(self.pb_setframerange)
		self.setLayout(layout)


class PencilControlWidget(QtGui.QGroupBox):
	""" A simple widget to let the user select/deselect the pencil tool
	"""
	def __init__(self, parent=None):
		super(PencilControlWidget, self).__init__(parent)
		self.pb_select_pencil = QtGui.QPushButton('Select Pencil Tool')
		self.pb_deselect_pencil = QtGui.QPushButton('Deelect Pencil Tool')
		self._setup_ui()

	def _setup_ui(self):
		layout = QtGui.QVBoxLayout()
		layout.addWidget(self.pb_select_pencil)
		layout.addWidget(self.pb_deselect_pencil)
		self.setLayout(layout)

