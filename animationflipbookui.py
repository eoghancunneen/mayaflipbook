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
#===============================================================================
""" Module docstring to come...
"""

# Primary module imports:
import re
import sys

# Third party module imports:
try:
    from PyQt4 import QtCore
    from PyQt4 import QtGui    
    _PYQT_AVAILABLE = True
except:
    _PYQT_AVAILABLE = False

try:
    from maya import cmds
    from maya import mel
except ImportError:
    pass

# Proprietary module imports:
import animationflipbook
from animationflipbookpyqt import Ui_Dialog


class MayaFlipbookPyqt(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MayaFlipbookPyqt, self).__init__(parent)
        self.setupUi(self)
        self.setup_interface()
        self.setup_interface_values()
        
        
    def setup_interface(self):
        """ Connecting the slots and signals for each of the
        widgets in the UI.
        """
        self.pb_set_framerange.clicked.connect(self.set_framerange)
        self.pb_select_pencil_tool.clicked.connect(self.select_pencil_tool)        
        self.pb_deselect_pencil_tool.clicked.connect(self.deselect_pencil_tool)
        self.pb_set_page.clicked.connect(self.set_page)        
        self.pb_add_to_page.clicked.connect(self.add_to_page)        
        self.pb_delete_page.clicked.connect(self.delete_page)        
        self.pb_go_to_page.clicked.connect(self.go_to_page)
        self.pb_display_next_page.clicked.connect(self.display_next_page)        
        self.pb_display_previous_page.clicked.connect(self.display_previous_page)        
        self.pb_onionskin_future_pages.clicked.connect(self.onionskin_next_pages)        
        self.pb_onionskin_past_pages.clicked.connect(self.onionskin_previous_pages)        
        self.pb_loop_selection.clicked.connect(self.loop_selection)        
        self.pb_playblast.clicked.connect(self.playblast)        
        self.pb_save.clicked.connect(self.save_scene)
        
        # Callbacks to fully implement and test. This will allow us
        # to remove buttons altogether and save on some screen real
        # estate:
        self.sb_start_frame.valueChanged.connect(self.update_start_frame)
        self.sb_end_frame.valueChanged.connect(self.update_start_frame)
        self.sb_go_to_page.valueChanged.connect(self.go_to_page)
        
        
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
        animationflipbook.set_framerange(self.sb_start_frame.value(),
                                           self.sb_end_frame.value())
    
    
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
        animationflipbook.go_to_page(self.sb_go_to_page.value())
    
    
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
        animationflipbook.loop_selected(self.sb_num_loops.value(),
                                          self.sb_step.value())
    
    
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



def launch_flipbook():
    """ This launches the UI and sets up the flipbook node.
    """
    # Create the flipbook node:
    setup_flipbook()
    
    # Show the UI:
    show_ui()


def setup_flipbook():
    """ Creates the flipbook node if one doesn't exist already.
    """
    animationflipbook.setup_animation_flipbook()


def set_framerange(*args):
    """ Set the scene's framerange.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    start_frame = cmds.floatFieldGrp("set_framerange_field", query=True, v1=True)
    end_frame = cmds.floatFieldGrp("set_framerange_field", query=True, v2=True)
    animationflipbook.set_framerange(start_frame, end_frame)
    

def loop_selected(*args):
    """ Loop the selected page.
        
    Loop over the selected pages N times with a gap of M frames
    between eack loop. N and M are values taken from the UI.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    num_loops = cmds.floatFieldGrp("set_loop_field", query=True, v1=True)
    step = cmds.floatFieldGrp("set_loop_field", query=True, v2=True)
    animationflipbook.loop_selection(int(num_loops), int(step))
    
    
def select_pencil_tool(*args):
    """ Select the pencil tool.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.select_pencil_tool(True)
    
    
def deselect_pencil_tool(*args):
    """ Deselect the pencil tool.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.select_pencil_tool(False)
   
   
def go_to_page(*args):
    """ Change the frame to the one specified.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    page_number = cmds.floatFieldGrp("go_to_page_field", v1=True, query=True)
    animationflipbook.go_to_page(page_number)


def set_page(*args):
    """ Add the selected or none-grouped curves to a new page.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.set_page()
    

def insert_page(*args):
    """ Set the current page.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.add_selection_to_page(duplicate=True)
    
    
def delete_page(*args):
    """ Delete the current page.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.delete_page()
    
    
def save_scene(*args):
    """ Set the current page.
    
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.save_scene()
    
    
def playblast_scene(*args):
    """ Playblast the current scene.
    
    Playblast the current scene, saving the output in the selected
    format and location designated in a JSON configuration file.
    
    :todo: Set up the JSON file to configure playblasts.
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.playblast_scene()


def display_next_page(*args):
    """ Display the next available page..
    
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.display_next_page()
    

def display_previous_page(*args):
    """ Display previous page.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.display_previous_page()
    
    
def display_next_pages(*args):
    """ Onionskin future pages.
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.display_next_pages()
    

def display_previous_pages(*args):
    """ Onionskin the previous pages
    
    :noindex:
    .. note::
        This is utilised by the native MEL UI.
    """
    animationflipbook.display_previous_pages()    


def show_ui():
    """ Show the appropriate UI to the user.
    
    Using the variable set upon creation of t
    """
    show_pyqt_ui() if _PYQT_AVAILABLE else show_native_ui()
        

def show_native_ui():
    """ This builds the actual native Maya Inteface and displays it.
    
    .. note::
        This is utilised by the native MEL UI.
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
    

def show_pyqt_ui():
    """ Display the PyQt4 UI as the user has QT installed.
    
    :raises: IOError
    """
    try:
        app = QtGui.QApplication(sys.argv)
        flipbook_dialog = MayaFlipbookPyqt()
        flipbook_dialog.show()
        sys.exit(app.exec_())

    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)
        _show_native_ui()


if __name__ == "__main__":
    show_pyqt_ui()
