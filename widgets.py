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
    """ A simple widget to let the user set the frame range."""
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
        self.setTitle('Set Scene Framerange')


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
        self.setTitle('Pencil Controls')


class PageOperationsWidget(QtGui.QGroupBox):
    """ A widget to allow the user to control the main features of this
    tool. Setting pages, adding pages, deleting pages, jumping to particular
    pages, page visibility features and onion skinning are all controlled
    from this widget."""
    def __init__(self, parent=None):
        super(PageOperationsWidget, self).__init__(parent)
        self.pb_set_page = QtGui.QPushButton('Set Page')
        self.pb_add_to_page = QtGui.QPushButton('Add to Page')
        self.pb_delete_page = QtGui.QPushButton('Delete Page')
        self.pb_go_to_page = QtGui.QPushButton('Go to Page')
        self.pb_display_next_page = QtGui.QPushButton('Display Next Page')
        self.pb_display_previous_page = QtGui.QPushButton('Display Previous Page')
        self.pb_os_future_pages = QtGui.QPushButton('Onionskin Future Pages')
        self.pb_os_past_pages = QtGui.QPushButton('Onionskin Past Pages')


        
        self._setup_ui()

    def _setup_ui(self):
        pass












