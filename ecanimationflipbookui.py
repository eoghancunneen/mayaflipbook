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

# Third party module imports:
try:
    import PyQt4
    _PYQT_AVAILABLE = True
except:
    _PYQT_AVAILABLE = False

from maya import cmds
from maya import mel

# Proprietary module imports:
import ecanimationflipbook


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
    # floatFieldGrp -numberOfFields 2 -w 500 -columnAlign3 "left" "left" "left" -label "Start Frame" -el "End Frame" -cw2 40 40 -pre 1 -v1 $Min -v2 $Max ShotUpFrameRangeGroup;
    # button -w 20 -label "Set Frame Range" -c "SetRange(\"ShotUpFrameRangeGroup\",\"RampFrameRangeGroup\")";
    
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
    
    # Set the framerange:
    #cmds.floatFieldGrp("set_framerange_field",
    #                   numberOfFields=2,
    #                   cw2=(10,10),
    #                   columnAlign2=("left","left"),
    #                   label="Start Frame",
    #                   el="End Frame",
    #                   pre=1,
    #                   v1=1.0,
    #                   v2=24.0)
    
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
    print "Going to load the PyQt4 User Interface...BOOM!"
    
