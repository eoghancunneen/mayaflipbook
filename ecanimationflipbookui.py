#! /usr/bin/python
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

# Primary module imports:
import re
import sys

# Third party module imports:
try:
    from PyQt4 import QtCore
    from PyQt4 import QtGui
    
    from ecanimationflipbookpyqt import Ui_Dialog
    _PYQT_AVAILABLE = True
except:
    _PYQT_AVAILABLE = False

try:
    from maya import cmds
    from maya import mel
except ImportError:
    pass

# Proprietary module imports:
import  ecanimationflipbook


# ------------------------------------------------------------------------------
#class GravityTechalyoutCharDialog(QtGui.QDialog, gravityTechlayoutExport_charDialogUI.Ui_Dialog):
#    
#    """
#    """
#    
#    def __init__(self, parent=None):
#        """
#        """
#        super(GravityTechalyoutCharDialog, self).__init__(parent)
#        self.setupUi(self)
#
#


class MayaFlipbookPyqt(QtGui.QDialog, Ui_Dialog):
    """
    """
    def __init__(self, parent=None):
        super(MayaFlipbookPyqt, self).__init__(parent)
        
        self.setupUi(self)
        self.setup_interface()
        
        
    def setup_interface(self):
        """ Connecting the slots and signals for each of the
        widgets in the UI.
        """
        self.connect(self.pb_set_framerange, QtCore.SIGNAL('clicked()'), self.set_framerange)
        self.connect(self.pb_select_pencil_tool, QtCore.SIGNAL('clicked()'), self.select_pencil_tool)
        self.connect(self.pb_deselect_pencil_tool, QtCore.SIGNAL('clicked()'), self.deselect_pencil_tool)
        self.connect(self.pb_set_page, QtCore.SIGNAL('clicked()'), self.set_page)
        self.connect(self.pb_add_to_page, QtCore.SIGNAL('clicked()'), self.add_to_page)
        self.connect(self.pb_delete_page, QtCore.SIGNAL('clicked()'), self.delete_page)
        self.connect(self.pb_go_to_page, QtCore.SIGNAL('clicked()'), self.go_to_page)
        self.connect(self.pb_display_next_page, QtCore.SIGNAL('clicked()'), self.display_next_page)
        self.connect(self.pb_display_previous_page, QtCore.SIGNAL('clicked()'), self.display_previous_page)
        self.connect(self.pb_onionskin_future_pages, QtCore.SIGNAL('clicked()'), self.onionskin_next_pages)
        self.connect(self.pb_onionskin_past_pages, QtCore.SIGNAL('clicked()'), self.onionskin_previous_pages)
        self.connect(self.pb_loop_selection, QtCore.SIGNAL('clicked()'), self.loop_selection)
        self.connect(self.pb_playblast, QtCore.SIGNAL('clicked()'), self.playblast)
        self.connect(self.pb_save, QtCore.SIGNAL('clicked()'), self.save_scene)
        
        
    def set_framerange(self):
        """ Set the scene's framerange.
        """
        # TODO: Add a check to make sure that the value that's been passed
        # is an integer value, rather than another character:
        start_frame = int(self.lb_start_frame.text())
        end_frame = int(self.lb_end_frame.text())
        ecanimationflipbook.set_framerange(start_frame, end_frame)
    
    
    def select_pencil_tool(self):
        """ Select the pencil tool.
        """
        ecanimationflipbook.select_pencil_tool(True)
    
    
    def deselect_pencil_tool(self):
        """ Deselect the pencil tool.
        """
        ecanimationflipbook.select_pencil_tool(False)
        
        
    def set_page(self):
        """ Add the selected or none-grouped curves to a new page.
        """
        ecanimationflipbook.set_page()
    
    
    def add_to_page(self):
        """ Add new curves to an existing page.
        """
        ecanimationflipbook.set_page()
        
        
    def insert_page(self):
        """ Set the current page.
        """
        ecanimationflipbook.add_selection_to_page(duplicate=True)
        
        
    def delete_page(self):
        """ Add new curves to an existing page.
        """       
        ecanimationflipbook.delete_page()
    
    
    def go_to_page(self):
        """ Set the current frame/page of the scene.
        """
        page_number = int(self.le_go_to_page.text())
        ecanimationflipbook.go_to_page(page_number)
    
    
    def display_next_page(self):
        """ Display the next available page.
        """
        ecanimationflipbook.display_next_page()
    
    
    def display_previous_page(self):
        """ Display the previous page.
        """
        ecanimationflipbook.display_previous_page()
    
    
    def onionskin_next_pages(self):
        """ Onionskin future pages.
        """
        ecanimationflipbook.display_next_pages()

    
    def onionskin_previous_pages(self):
        """ Onionskin the previous pages.
        """
        ecanimationflipbook.display_previous_pages()
    
    
    def loop_selection(self):
        """ Loop the 
        """
        # TODO: Need to make sure that the loop count and step are integer
        # values and not other characters:
        num_loops = int(self.le_num_loops.text())
        step = int(self.le_step.text())
        ecanimationflipbook.loop_selected(num_loops, step)
    
    
    def playblast(self):
        """ Set off a playblast of set framerage.
        """
        # This may live or die according to whichever platform we're
        # currently playing on:
        ecanimationflipbook.playblast_scene()
    
    
    def save_scene(self):
        """
        """
        ecanimationflipbook.save_scene()



def launch_flipbook():
    """ This launches the UI and sets up the flipbook node.
    """
    # Create the flipbook node:
    _setup_flipbook()
    
    # Show the UI:
    _show_ui()


def _setup_flipbook():
    """ Creates the flipbook node if one doesn't exist already.
    """
    ecanimationflipbook.setup_animation_flipbook()


def set_framerange(*args):
    """ Pass the values through to set the framerange for the scene.
    """
    start_frame = cmds.floatFieldGrp("set_framerange_field", query=True, v1=True)
    end_frame = cmds.floatFieldGrp("set_framerange_field", query=True, v2=True)
    ecanimationflipbook.set_framerange(start_frame, end_frame)
    

def loop_selected(*args):
    """ Pass the values through to set the framerange for the scene.
    """
    num_loops = cmds.floatFieldGrp("set_loop_field", query=True, v1=True)
    step = cmds.floatFieldGrp("set_loop_field", query=True, v2=True)
    ecanimationflipbook.loop_selection(int(num_loops), int(step))
    
    
def select_pencil_tool(*args):
    """ Select the pencil tool.
    """
    ecanimationflipbook.select_pencil_tool(True)
    
    
def deselect_pencil_tool(*args):
    """ Select the pencil tool.
    """
    ecanimationflipbook.select_pencil_tool(False)
   
   
def go_to_page(*args):
    """ Change the frame to the one specified.
    """
    page_number = cmds.floatFieldGrp("go_to_page_field", v1=True, query=True)
    ecanimationflipbook.go_to_page(page_number)


def set_page(*args):
    """ Set the current page.
    """
    ecanimationflipbook.set_page()
    

def insert_page(*args):
    """ Set the current page.
    """
    ecanimationflipbook.add_selection_to_page(duplicate=True)
    
    
def delete_page(*args):
    """ Set the current page.
    """
    ecanimationflipbook.delete_page()
    
    
def save_scene(*args):
    """ Set the current page.
    """
    ecanimationflipbook.save_scene()
    
    
def playblast_scene(*args):
    """ Set the current page.
    """
    ecanimationflipbook.playblast_scene()


def display_next_page(*args):
    """ Set the current page.
    """
    ecanimationflipbook.display_next_page()
    

def display_previous_page(*args):
    """ Set the current page.
    """
    ecanimationflipbook.display_previous_page()
    
    
def display_next_pages(*args):
    """ Set the current page.
    """
    ecanimationflipbook.display_next_pages()
    

def display_previous_pages(*args):
    """ Set the current page.
    """
    ecanimationflipbook.display_previous_pages()    


def _show_ui():
    """ Show the appropriate UI to the user.
    
    Using the variable set upon creation of t
    """
    if _PYQT_AVAILABLE:
        _show_pyqt_ui()
    else:
        _show_native_ui()

def _show_native_ui():
    """
    """
    # Set the window name:
    window_name = "ecanimation_flipbook"
    
    # If it already exists, kill it:
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
        
    if cmds.windowPref(window_name, exists=True):
        cmds.windowPref(window_name, remove=True)

    # Set up the window and the layout:
    cmds.window(window_name, title="Flipbook Animation Tool")
    cmds.columnLayout(adjustableColumn=True)
    cmds.rowColumnLayout(columnAlign=(1,"left"), nc=1, cw=[(1,480)])

    cmds.floatFieldGrp("set_framerange_field",
                       numberOfFields=2,
                       label="Start Frame",
                       el="End Frame",
                       pre=1,
                       v1=1.0,
                       v2=24.0)
               
               
    cmds.button(w=10, label="Set Framerange", command=set_framerange)
    cmds.text(label="")
    
    # Select/deselect the pencil tool:
    cmds.button(w=20, label="Select Pencil Tool", command=select_pencil_tool)
    cmds.button(w=20, label="Deselect Pencil Tool", command=deselect_pencil_tool)
    cmds.text(label="")
    
    # Set the page:
    cmds.button(w=20, label="Set page", command=set_page)
    cmds.button(w=20, label="Add to page", command=insert_page)
    cmds.button(w=20, label="Delete page", command=delete_page)
    cmds.text(label="")
    
    # Go to page:
    go_to_page_field = cmds.floatFieldGrp("go_to_page_field",
                                          numberOfFields=1,
                                          columnWidth=(10,10),
                                          columnAlign2=("left","left"),
                                          label="Go to frame",
                                          pre=1,
                                          v1=1.0)
    
    cmds.button(w=20, label="Go to page", command=lambda *args: go_to_page(go_to_page_field))
    cmds.text(label="")
    
    cmds.button(w=20, label="Display Next Page", command=display_next_page)
    cmds.button(w=20, label="Display Previous Page", command=display_previous_page)
    cmds.text(label="")
    
    cmds.button(w=20, label="Onion skin future frames", command=display_next_pages)
    cmds.button(w=20, label="Onion skin past frames", command=display_previous_pages)
    cmds.text(label="")
    
        # Set the framerange:
    cmds.floatFieldGrp("set_loop_field",
                       numberOfFields=2,
                       w=2,
                       columnAlign2=("left","left"),
                       label="Number of loops",
                       el="Step",
                       cw2=(10,10),
                       pre=1,
                       v1=0.0,
                       v2=0.0)
    cmds.button(w=20, label="Loop Selection", command=loop_selected)
    cmds.text(label="")
    
    # Playblast:
    cmds.button(w=20, label="Playblast", command=playblast_scene)
    cmds.text(label="")
    
    # Save:
    cmds.button(w=20, label="Save", command=save_scene)
    cmds.text(label="")
    
    cmds.setParent("..")
    cmds.showWindow(window_name) 
    

def _show_pyqt_ui():
    """ Display the PyQt4 UI as the user has QT installed.
    
    Comments to come...
    """
    try:
        print "Going to load the PyQt4 User Interface...BOOM!"
        global flipbook_dialog
        print "0"
        flipbook_dialog = MayaFlipbookPyqt()
        print "1"
        flipbook_dialog.show()
        print "2"

    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        _show_native_ui()
    

  
    
# Entry point for launcher
if __name__ == "__main__":
    try:       
        _show_pyqt_ui()
    except:
        pass
