#! /usr/bin/env python
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
""" This is the construction of the UI that the user will use within maya.
...
"""

# Primary module imports:
import logging

# Third party module imports:
try:
    import widgets
    reload(widgets)
    _PYQT_AVAILABLE = True
except ImportError:
    _PYQT_AVAILABLE = False
    print "No PyQt"

try:
    from maya import cmds
except ImportError as e:
    logging.info(
        'Running outside of Maya mode. Full feature set will '
        'not work. Use this for testing front end.\n'
        '{0}'.format(e))

# Proprietary module imports:
import animationflipbook
reload(animationflipbook)


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


def show_native_ui():
    """ This builds the actual native Maya Inteface and displays it.

    .. note::
        This is utilised by the native MEL UI.
    """
    # Set up the flipbook:
    setup_flipbook()

    # Set the window name:
    window_name = "animation_flipbook"

    # If it already exists, kill it:
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)

    if cmds.windowPref(window_name, exists=True):
        cmds.windowPref(window_name, remove=True)

    # Set up the window and the layout:
    cmds.window(window_name, title="Flipbook Animation Tool")
    cmds.columnLayout(adjustableColumn=True)
    cmds.rowColumnLayout(columnAlign=(1, "left"), nc=1, cw=[(1, 480)])

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
        columnWidth=(10, 10),
        columnAlign2=("left", "left"),
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
                       columnAlign2=("left", "left"),
                       label="Number of loops",
                       el="Step",
                       cw2=(10, 10),
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


def show():
    """ Display the PyQt4 UI as the user has QT installed.

    :raises: Exception
    """
    # Setup the flipbook locator which will hold all of the information:
    setup_flipbook()

    if _PYQT_AVAILABLE:
        try:
            global flipbook_dialog
            flipbook_dialog = widgets.MayaFlipBookFacade()
            flipbook_dialog.show()
        except Exception:
            show_native_ui()
    else:
        show_native_ui()


if __name__ == "__main__":
    show()
