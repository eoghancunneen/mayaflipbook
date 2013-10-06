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
        horizontal_layout.addWidget(self.lb_startframe)
        horizontal_layout.addWidget(self.sb_startframe)
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(separator)
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.sb_endrame)
        horizontal_layout.addWidget(self.lb_endframe)
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
        self.pb_display_next_page = QtGui.QPushButton('Display Next Page')
        self.pb_display_previous_page = QtGui.QPushButton('Display Previous Page')
        self.pb_os_future_pages = QtGui.QPushButton('Onionskin Future Pages')
        self.pb_os_past_pages = QtGui.QPushButton('Onionskin Past Pages')
        self.lb_page_picker = QtGui.QLabel('Go to Page')
        self.sb_page_picker = QtGui.QSpinBox()
        self.pb_page_picker = QtGui.QPushButton('Go')
        self._setup_ui()

    def _setup_ui(self):
        layout = QtGui.QVBoxLayout()
        picker_layout = QtGui.QHBoxLayout()
        picker_form_layout = QtGui.QFormLayout()
        line1 = line2 = QtGui.QFrame()
        line1.setFrameShape(QtGui.QFrame.HLine)
        line2.setFrameShape(QtGui.QFrame.HLine)
        picker_form_layout.addRow(self.lb_page_picker, self.sb_page_picker)
        picker_layout.addLayout(picker_form_layout)
        picker_layout.addWidget(self.pb_page_picker)
        layout.addWidget(self.pb_set_page)
        layout.addWidget(self.pb_add_to_page)
        layout.addWidget(self.pb_delete_page)
        layout.addWidget(line1)
        layout.addLayout(picker_layout)
        layout.addWidget(line2)
        layout.addWidget(self.pb_display_next_page)
        layout.addWidget(self.pb_display_previous_page)
        layout.addWidget(self.pb_os_future_pages)
        layout.addWidget(self.pb_os_past_pages)
        self.setLayout(layout)
        self.setTitle('Page Operations')


class LoopOperationsWidget(QtGui.QGroupBox):
    """ A widget to let the user create a loop over a number of pages"""
    def __init__(self, parent=None):
       super(LoopOperationsWidget, self).__init__(parent)
       self.lb_num_loops = QtGui.QLabel('# Loops')
       self.lb_steps = QtGui.QLabel('Step')
       self.sb_num_loops = QtGui.QSpinBox()
       self.sb_steps = QtGui.QSpinBox()
       self.pb_execute_loop = QtGui.QPushButton('Loop Selection')
       self._setup_ui()

    def _setup_ui(self):
        layout = QtGui.QVBoxLayout()
        horizontal_layout = QtGui.QHBoxLayout()
        horizontal_layout.addWidget(self.lb_num_loops)
        horizontal_layout.addWidget(self.sb_num_loops)
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.lb_steps)
        horizontal_layout.addWidget(self.sb_steps)
        layout.addLayout(horizontal_layout)
        layout.addWidget(self.pb_execute_loop)
        self.setLayout(layout)
        self.setTitle('Loop Options')


class AdditionaOptionsWidget(QtGui.QGroupBox):
    """ A widget that contains extra, miscellaneous features"""
    def __init__(self, parent=None):
        super(AdditionaOptionsWidget, self).__init__(parent)
        self.pb_playblast = QtGui.QPushButton('Playblast')
        self.pb_save_scene = QtGui.QPushButton('Save Scene')
        self._setup_ui()

    def _setup_ui(self):
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.pb_playblast)
        layout.addWidget(self.pb_save_scene)
        self.setLayout(layout)
