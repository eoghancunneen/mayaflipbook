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
import os
import sys
import re

# Third party module imports:
try:
    from maya import cmds
    from maya import mel
except ImportError:
    pass
    
# Proprietary module imports:


# ------------------------------------------------------------------------------


def save_scene():
    """
    """
    os.listdir("~/")
    cmds.file(rename="fred.ma")
    cmds.file(save=True, type='mayaAscii')
    
    
def start_playblast():
    """
    """
    start_frame = cmds.playbackOptions(min=True, query=True)
    end_frame   = cmds.playbackOptions(max=True, query=True)
    location = "x"
    cmds.playblast(filename="/tmp/tmp.mov", fmt="qt", offScreen=True)


def set_framerange(start_time, end_time):
    """ Set the start and end range for playback and animation.
    """
    cmds.playbackOptions(ast=start_time, aet=end_time, min=start_time, max=end_time)


def select_pencil_tool(select=True):
    """ Select the pencil tool.
    """
    if select:
        cmds.setToolTo("pencilContext")
    else:
        cmds.setToolTo(t)