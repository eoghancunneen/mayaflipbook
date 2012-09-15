#==============================================================================
#
#  Copyright (c) 2012 Eoghan Patrick Cunneen
#  All rights reserved.
#
#  This file contains confidential and proprietary source code, belonging to
#  Eoghan Patrick Cunneen. Its contents may not be disclosed to third parties,
#  copied or duplicated in any form, in whole or in part, without prior
#  permission.
#
#  Summary: 
#           
#
#===============================================================================

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ecanimationflipbook.ui'
#
# Created: Sat Sep 15 23:11:47 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(330, 790)
        Dialog.setMinimumSize(QtCore.QSize(330, 790))
        self.gridLayout_6 = QtGui.QGridLayout(Dialog)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.grp_framerange = QtGui.QGroupBox(Dialog)
        self.grp_framerange.setObjectName(_fromUtf8("grp_framerange"))
        self.gridLayout = QtGui.QGridLayout(self.grp_framerange)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lb_start_frame = QtGui.QLabel(self.grp_framerange)
        self.lb_start_frame.setObjectName(_fromUtf8("lb_start_frame"))
        self.horizontalLayout.addWidget(self.lb_start_frame)
        self.le_start_frame = QtGui.QLineEdit(self.grp_framerange)
        self.le_start_frame.setObjectName(_fromUtf8("le_start_frame"))
        self.horizontalLayout.addWidget(self.le_start_frame)
        self.label_3 = QtGui.QLabel(self.grp_framerange)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.le_end_frame = QtGui.QLineEdit(self.grp_framerange)
        self.le_end_frame.setObjectName(_fromUtf8("le_end_frame"))
        self.horizontalLayout.addWidget(self.le_end_frame)
        self.lb_end_frame = QtGui.QLabel(self.grp_framerange)
        self.lb_end_frame.setObjectName(_fromUtf8("lb_end_frame"))
        self.horizontalLayout.addWidget(self.lb_end_frame)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pb_set_framerange = QtGui.QPushButton(self.grp_framerange)
        self.pb_set_framerange.setObjectName(_fromUtf8("pb_set_framerange"))
        self.verticalLayout.addWidget(self.pb_set_framerange)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.grp_framerange, 0, 0, 1, 1)
        self.grp_pencil_options = QtGui.QGroupBox(Dialog)
        self.grp_pencil_options.setObjectName(_fromUtf8("grp_pencil_options"))
        self.gridLayout_2 = QtGui.QGridLayout(self.grp_pencil_options)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pb_select_pencil_tool = QtGui.QPushButton(self.grp_pencil_options)
        self.pb_select_pencil_tool.setObjectName(_fromUtf8("pb_select_pencil_tool"))
        self.gridLayout_2.addWidget(self.pb_select_pencil_tool, 0, 0, 1, 1)
        self.pb_deselect_pencil_tool = QtGui.QPushButton(self.grp_pencil_options)
        self.pb_deselect_pencil_tool.setObjectName(_fromUtf8("pb_deselect_pencil_tool"))
        self.gridLayout_2.addWidget(self.pb_deselect_pencil_tool, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.grp_pencil_options, 1, 0, 1, 1)
        self.grp_page_operations = QtGui.QGroupBox(Dialog)
        self.grp_page_operations.setObjectName(_fromUtf8("grp_page_operations"))
        self.gridLayout_5 = QtGui.QGridLayout(self.grp_page_operations)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.pb_set_page = QtGui.QPushButton(self.grp_page_operations)
        self.pb_set_page.setObjectName(_fromUtf8("pb_set_page"))
        self.verticalLayout_5.addWidget(self.pb_set_page)
        self.pb_add_to_page = QtGui.QPushButton(self.grp_page_operations)
        self.pb_add_to_page.setObjectName(_fromUtf8("pb_add_to_page"))
        self.verticalLayout_5.addWidget(self.pb_add_to_page)
        self.pb_delete_page = QtGui.QPushButton(self.grp_page_operations)
        self.pb_delete_page.setObjectName(_fromUtf8("pb_delete_page"))
        self.verticalLayout_5.addWidget(self.pb_delete_page)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.line_2 = QtGui.QFrame(self.grp_page_operations)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_7.addWidget(self.line_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lb_go_to_page = QtGui.QLabel(self.grp_page_operations)
        self.lb_go_to_page.setObjectName(_fromUtf8("lb_go_to_page"))
        self.horizontalLayout_2.addWidget(self.lb_go_to_page)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.le_go_to_page = QtGui.QLineEdit(self.grp_page_operations)
        self.le_go_to_page.setObjectName(_fromUtf8("le_go_to_page"))
        self.horizontalLayout_2.addWidget(self.le_go_to_page)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pb_go_to_page = QtGui.QPushButton(self.grp_page_operations)
        self.pb_go_to_page.setObjectName(_fromUtf8("pb_go_to_page"))
        self.verticalLayout_2.addWidget(self.pb_go_to_page)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        self.line_3 = QtGui.QFrame(self.grp_page_operations)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_7.addWidget(self.line_3)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.pb_display_next_page = QtGui.QPushButton(self.grp_page_operations)
        self.pb_display_next_page.setObjectName(_fromUtf8("pb_display_next_page"))
        self.verticalLayout_6.addWidget(self.pb_display_next_page)
        self.pb_display_previous_page = QtGui.QPushButton(self.grp_page_operations)
        self.pb_display_previous_page.setObjectName(_fromUtf8("pb_display_previous_page"))
        self.verticalLayout_6.addWidget(self.pb_display_previous_page)
        self.pb_onionskin_future_pages = QtGui.QPushButton(self.grp_page_operations)
        self.pb_onionskin_future_pages.setObjectName(_fromUtf8("pb_onionskin_future_pages"))
        self.verticalLayout_6.addWidget(self.pb_onionskin_future_pages)
        self.pb_onionskin_past_pages = QtGui.QPushButton(self.grp_page_operations)
        self.pb_onionskin_past_pages.setObjectName(_fromUtf8("pb_onionskin_past_pages"))
        self.verticalLayout_6.addWidget(self.pb_onionskin_past_pages)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 2, 2)
        self.line = QtGui.QFrame(self.grp_page_operations)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_5.addWidget(self.line, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.grp_page_operations, 2, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.lb_num_loops = QtGui.QLabel(self.groupBox_4)
        self.lb_num_loops.setObjectName(_fromUtf8("lb_num_loops"))
        self.horizontalLayout_3.addWidget(self.lb_num_loops)
        self.le_num_loops = QtGui.QLineEdit(self.groupBox_4)
        self.le_num_loops.setObjectName(_fromUtf8("le_num_loops"))
        self.horizontalLayout_3.addWidget(self.le_num_loops)
        self.lb_step = QtGui.QLabel(self.groupBox_4)
        self.lb_step.setObjectName(_fromUtf8("lb_step"))
        self.horizontalLayout_3.addWidget(self.lb_step)
        self.le_step = QtGui.QLineEdit(self.groupBox_4)
        self.le_step.setObjectName(_fromUtf8("le_step"))
        self.horizontalLayout_3.addWidget(self.le_step)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.pb_loop_selection = QtGui.QPushButton(self.groupBox_4)
        self.pb_loop_selection.setObjectName(_fromUtf8("pb_loop_selection"))
        self.verticalLayout_3.addWidget(self.pb_loop_selection)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(Dialog)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pb_playblast = QtGui.QPushButton(self.groupBox_5)
        self.pb_playblast.setObjectName(_fromUtf8("pb_playblast"))
        self.verticalLayout_4.addWidget(self.pb_playblast)
        self.pb_save = QtGui.QPushButton(self.groupBox_5)
        self.pb_save.setObjectName(_fromUtf8("pb_save"))
        self.verticalLayout_4.addWidget(self.pb_save)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_5, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.le_start_frame, self.le_end_frame)
        Dialog.setTabOrder(self.le_end_frame, self.pb_set_framerange)
        Dialog.setTabOrder(self.pb_set_framerange, self.pb_select_pencil_tool)
        Dialog.setTabOrder(self.pb_select_pencil_tool, self.pb_deselect_pencil_tool)
        Dialog.setTabOrder(self.pb_deselect_pencil_tool, self.pb_set_page)
        Dialog.setTabOrder(self.pb_set_page, self.pb_add_to_page)
        Dialog.setTabOrder(self.pb_add_to_page, self.pb_delete_page)
        Dialog.setTabOrder(self.pb_delete_page, self.le_go_to_page)
        Dialog.setTabOrder(self.le_go_to_page, self.pb_go_to_page)
        Dialog.setTabOrder(self.pb_go_to_page, self.pb_display_next_page)
        Dialog.setTabOrder(self.pb_display_next_page, self.pb_display_previous_page)
        Dialog.setTabOrder(self.pb_display_previous_page, self.pb_onionskin_future_pages)
        Dialog.setTabOrder(self.pb_onionskin_future_pages, self.pb_onionskin_past_pages)
        Dialog.setTabOrder(self.pb_onionskin_past_pages, self.le_num_loops)
        Dialog.setTabOrder(self.le_num_loops, self.le_step)
        Dialog.setTabOrder(self.le_step, self.pb_loop_selection)
        Dialog.setTabOrder(self.pb_loop_selection, self.pb_playblast)
        Dialog.setTabOrder(self.pb_playblast, self.pb_save)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_framerange.setTitle(QtGui.QApplication.translate("Dialog", "Set Scene Framerange", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_start_frame.setText(QtGui.QApplication.translate("Dialog", "Start Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_end_frame.setText(QtGui.QApplication.translate("Dialog", "End Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_set_framerange.setText(QtGui.QApplication.translate("Dialog", "Set Framerange", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_pencil_options.setTitle(QtGui.QApplication.translate("Dialog", "Pencil Tool Options", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_select_pencil_tool.setText(QtGui.QApplication.translate("Dialog", "Select Pencil Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_deselect_pencil_tool.setText(QtGui.QApplication.translate("Dialog", "Deselect Pencil Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_page_operations.setTitle(QtGui.QApplication.translate("Dialog", "Page Operations", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_set_page.setText(QtGui.QApplication.translate("Dialog", "Set Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_add_to_page.setText(QtGui.QApplication.translate("Dialog", "Add to Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_delete_page.setText(QtGui.QApplication.translate("Dialog", "Delete Page", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_go_to_page.setText(QtGui.QApplication.translate("Dialog", "Go to Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_go_to_page.setText(QtGui.QApplication.translate("Dialog", "Go to Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_display_next_page.setText(QtGui.QApplication.translate("Dialog", "Display Next Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_display_previous_page.setText(QtGui.QApplication.translate("Dialog", "Display Previous Page", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_onionskin_future_pages.setText(QtGui.QApplication.translate("Dialog", "Onionskin Future Pages", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_onionskin_past_pages.setText(QtGui.QApplication.translate("Dialog", "Onionskin Past Pages", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Dialog", "Loop Options", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_num_loops.setText(QtGui.QApplication.translate("Dialog", "# Loops", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_step.setText(QtGui.QApplication.translate("Dialog", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_loop_selection.setText(QtGui.QApplication.translate("Dialog", "Loop Selection", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Dialog", "Other Options", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_playblast.setText(QtGui.QApplication.translate("Dialog", "Playblast", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_save.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))

