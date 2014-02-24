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
from PyQt4 import QtGui
from maya import cmds

# Proprietary module imports:
import animationflipbook
reload(animationflipbook)


class MayaFlipBookFacade(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MayaFlipBookFacade, self).__init__(parent)
        self.framerange_widget = FrameRangeWidget()
        self.pencil_control_widget = PencilControlWidget()
        self.page_operation_widget = PageOperationsWidget()
        self.loop_operations_widget = LoopOperationsWidget()
        self.extra_options = AdditionaOptionsWidget()
        self._setup_ui()
        self._setup_connections()

    def _setup_ui(self):
        """ Construct the UI."""
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.framerange_widget)
        layout.addWidget(self.pencil_control_widget)
        layout.addWidget(self.page_operation_widget)
        layout.addWidget(self.loop_operations_widget)
        layout.addWidget(self.extra_options)
        self.setLayout(layout)

    def _setup_connections(self):
        """ Connecting the slots and signals for each of the widgets
        in the UI.
        """
        self.framerange_widget.pb_set_framerange.clicked.connect(
            self.set_framerange)
        self.pencil_control_widget.pb_select_pencil.clicked.connect(
            self.select_pencil_tool)
        self.pencil_control_widget.pb_deselect_pencil.clicked.connect(
            self.deselect_pencil_tool)
        self.page_operation_widget.pb_set_page.clicked.connect(
            self.set_page)
        self.page_operation_widget.pb_add_to_page.clicked.connect(
            self.add_to_page)
        self.page_operation_widget.pb_delete_page.clicked.connect(
            self.delete_page)
        self.page_operation_widget.pb_page_picker.clicked.connect(
            self.go_to_page)
        self.page_operation_widget.pb_display_next_page.clicked.connect(
            self.display_next_page)
        self.page_operation_widget.pb_display_previous_page.clicked.connect(
            self.display_previous_page)
        self.page_operation_widget.pb_os_future_pages.clicked.connect(
            self.onionskin_next_pages)
        self.page_operation_widget.pb_os_past_pages.clicked.connect(
            self.onionskin_previous_pages)
        self.loop_operations_widget.pb_execute_loop.clicked.connect(
            self.loop_selection)
        self.extra_options.pb_playblast.clicked.connect(self.playblast)
        self.extra_options.pb_save_scene.clicked.connect(self.save_scene)

        # :TODO:
        # Callbacks to fully implement and test. This will allow us
        # to remove buttons altogether and save on some screen real
        # estate:
        #self.framerange_widget.sb_startframe.valueChanged.connect(
        #    self.update_start_frame)
        #self.framerange_widget.sb_endframe.valueChanged.connect(
        #    self.update_start_frame)
        #self.framerange_widget.sb_go_to_page.valueChanged.connect(
        #    self.go_to_page)

    def setup_interface_values(self):
        """ Setting the default values for the widgets.

        Querying the maya scene to get the get basic default values and
        setting other values to their default values.
        """

        # Set the start and end frame values to the current maya
        # start and end frames:
        self.sb_start_frame.setText(cmds.playbackOptions(query=True, min=True))
        self.sb_end_frame.setText(cmds.playbackOptions(query=True, max=True))

        # Set the
        self.le_go_to_page.setText()

    def set_framerange(self):
        """ Set the scene's framerange.
        :deprecated: Widget call backs will resolve this.
        """
        animationflipbook.set_framerange(
            self.framerange_widget.sb_start_frame.value(),
            self.framerange_widget.sb_end_frame.value())

    def select_pencil_tool(self):
        """ Select the pencil tool.
        """
        animationflipbook.select_pencil_tool(True)

    def deselect_pencil_tool(self):
        """ Deselect the pencil tool.
        """
        animationflipbook.select_pencil_tool(False)

    def set_page(self):
        """ Add the selected or none-grouped curves to a new page.
        """
        animationflipbook.set_page()

    def add_to_page(self):
        """ Add new curves to an existing page.
        """
        animationflipbook.set_page()

    def insert_page(self):
        """ Set the current page.
        """
        animationflipbook.add_selection_to_page(duplicate=True)

    def delete_page(self):
        """ Delete the current page.
        """
        animationflipbook.delete_page()

    def go_to_page(self):
        """ Set the current frame/page of the scene.
        """
        animationflipbook.go_to_page(
            self.page_operation_widget.sb_page_picker.value())

    def display_next_page(self):
        """ Display the next available page.
        """
        animationflipbook.display_next_page()

    def display_previous_page(self):
        """ Display the previous page.
        """
        animationflipbook.display_previous_page()

    def onionskin_next_pages(self):
        """ Onionskin future pages.
        """
        animationflipbook.display_next_pages()

    def onionskin_previous_pages(self):
        """ Onionskin the previous pages.
        """
        animationflipbook.display_previous_pages()

    def loop_selection(self):
        """ Loop the selected page.

        Loop over the selected pages N times with a gap of M frames
        between eack loop. N and M are values taken from the UI.
        """
        animationflipbook.loop_selection(
            self.loop_operations_widget.sb_num_loops.value(),
            self.loop_operations_widget.sb_steps.value())

    def playblast(self):
        """ Playblast the current scene.

        Playblast the current scene, saving the output in the selected
        format and location designated in a JSON configuration file.

        :todo: Set up the JSON file to configure playblasts.
        :deprecated: Create a new playblast module for maya.
        """
        # This may live or die according to whichever platform we're
        # currently playing on:
        animationflipbook.playblast_scene()

    def save_scene(self):
        """ Save the current scene.

        :deprecated: Create a new Maya save/load module.
        """
        animationflipbook.save_scene()


class FrameRangeWidget(QtGui.QGroupBox):
    """ A simple widget to let the user set the frame range."""
    def __init__(self, parent=None):
        print parent
        print type(parent)
        super(FrameRangeWidget, self).__init__(parent)
        self.lb_start_frame = QtGui.QLabel('Start Frame')
        self.lb_end_frame = QtGui.QLabel('End Frame')
        self.sb_start_frame = QtGui.QSpinBox()
        self.sb_end_frame = QtGui.QSpinBox()
        self.pb_set_framerange = QtGui.QPushButton('Set Framerange')
        self._setup_ui()
        self._set_connections()

    def _setup_ui(self):
        layout = QtGui.QVBoxLayout()
        separator = QtGui.QLabel('-')
        horizontal_layout = QtGui.QHBoxLayout()
        horizontal_layout.addWidget(self.lb_start_frame)
        horizontal_layout.addWidget(self.sb_start_frame)
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(separator)
        horizontal_layout.addStretch()
        horizontal_layout.addWidget(self.sb_end_frame)
        horizontal_layout.addWidget(self.lb_end_frame)
        layout.addLayout(horizontal_layout)
        layout.addWidget(self.pb_set_framerange)
        self.setLayout(layout)
        self.setTitle('Set Scene Framerange')
        self.sb_start_frame.setMinimum(0)
        self.sb_end_frame.setMaximum(999999)
        self.sb_start_frame.setValue(1)
        self.sb_end_frame.setValue(24)

    def _set_connections(self):
        self.sb_start_frame.valueChanged.connect(
            self._resolve_frame_range)
        self.sb_end_frame.valueChanged.connect(
            self._resolve_frame_range)

    def _resolve_frame_range(self):
        # The end frame can never be larger than the start frame:
        if self.sb_end_frame.value() <= self.sb_start_frame.value():
            self.sb_end_frame.setValue(self.sb_start_frame.value() + 1)


class PencilControlWidget(QtGui.QGroupBox):
    """ A simple widget to let the user select/deselect the pencil tool
    """
    def __init__(self, parent=None):
        super(PencilControlWidget, self).__init__(parent)
        self.pb_select_pencil = QtGui.QPushButton('Select Pencil Tool')
        self.pb_deselect_pencil = QtGui.QPushButton('Deselect Pencil Tool')
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
