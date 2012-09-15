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
import os
import time

# Third party module imports:
from maya import cmds
from maya import mel

# Proprietary module imports:


# ------------------------------------------------------------------------------
# Private functions:

def _display_page(page_number):
    """
    """
    current_frame = cmds.currentTime(query=True)
    cmds.setAttr("page_%04d.visibilityOverride"%(page_number), 1)
    
    
def _display_pages(page_numbers):
    """
    """
    current_frame = cmds.currentTime(query=True)
    for number in page_numbers:
        cmds.setAttr("page_%04d.visibilityOverride"%(number), 1)
    

def _internally_sort_page_numbers():
    """ When inserting page numbers between set pages, this will sort the page
    numbers in the currentPage enum attribute.
    
    Comments to come...
    """
    # Get the pages in the format "page_xxxx:page_xxxy:page_xxxz:etc":
    pages = cmds.addAttr("flipbook_LOC.currentPage", query=True, enumName=True)
    
    # Arrange into a list for sorting:
    page_list = pages.split(':')
    page_list.sort()
    sorted_pages = ':'.join(page_list)
    
    # Return the sorted enum list:
    return sorted_pages


def _update_flipbook_node(new_page, current_frame):
    """ Updates the flipbook node with a new page in the enumerator and sets the
    key for that frame.
    
    @param new_page: Page name
    @type new_page: String
    """
    # ...:
    cmds.expression(object=new_page,
                    name="%s_visbility_EXP"%(new_page), 
                    string="int $page = %d;\nint $current_keyed_frame = flipbook_LOC.pagesToDisplay;\n%s.visibility = ($page==$current_keyed_frame)||(visibilityOverride);"%(current_frame, new_page),
                    alwaysEvaluate=True)
    
    # We will also be adding another attribute with just integer values. This 
    # will be set here at this point as well.
    cmds.setKeyframe("flipbook_LOC.pagesToDisplay",
                     value=current_frame,
                     time=current_frame,
                     outTangentType="step")
    
    # Return:
    return

def _get_project_path():
    """ Returns the current maya project workspace.
    """
    return cmds.workspace(query=True, rootDirectory=True)
    

def _get_scenes_directory():
    """ Returns the path to where the scenes are saved to.
    """
    return os.path.join(_get_project_path(), "scenes")


def _get_images_directory():
    """ Returns the path to where the scenes are saved to.
    """
    return os.path.join(_get_project_path(), "images")


# ------------------------------------------------------------------------------
# Public-er functions:

def setup_animation_flipbook():
    """ Set the rig for the animation flipbook.
    
    Comments to come...
    """
    if not cmds.objExists("flipbook_LOC"):
        cmds.spaceLocator(name="flipbook_LOC")
        cmds.addAttr("flipbook_LOC",
                     longName="pagesToDisplay",
                     attributeType="long")
    return


def set_page():
    """ Sets the current frame as a page.
    
    Comments to come...
    """
    
    # ...
    selected_objects = list()
    
    # Get all of the selected objects in the scene:
    #if cmds.ls(selection=True):
    #    selected_objects = cmds.ls(selection=True)
    #else:
    # If nothing is selected, then get everything that isn't already in a page
    # of its own:
    cmds.select(clear=True)
    cmds.select(allDagObjects=True)
        
    for object in cmds.ls(selection=True):
        print "Object: ", object
        if cmds.listRelatives(object, shapes=True):
            object_shape = cmds.listRelatives(object, shapes=True)[0]
            if cmds.objectType(object_shape) == "nurbsCurve":
                selected_objects.append(object)
                    
    # Then group the objects into their own page. The page number is dictated
    # by the current frame:
    current_frame = cmds.currentTime(query=True)
    page_name = "page_%04d"%(current_frame)

    if not cmds.objExists(page_name):
        cmds.group(selected_objects, name=page_name)
        
        # Add the visibility override attribute to the group name:
        cmds.addAttr(page_name, longName="visibilityOverride", attributeType="bool")
        cmds.setKeyframe(page_name+".visibilityOverride", time=1, value=0)
    
        # Set the key for this page and insert the page number into the attribute
        # on the flipbook node:
        _update_flipbook_node(page_name, current_frame)
    else:
        cmds.parent(selected_objects, page_name)
        
    

    # Return
    return


def go_to_page(page_number):
    """ Go to a particular page in the animation regardless of it being keyed or
    not.
    
    Comments to come...
    """
    # Update the timeline to the specific frame number passed as a parameter:
    cmds.currentTime(page_number, edit=True, update=True)

 
def add_selection_to_page(duplicate=False):
    """ Takes the current selection of objects and moves them to a new or
    existing page.
    
    Comments to come
    """
    # Get the current selected objects:
    selected_objects = cmds.ls(selection=True)
    
    # Are they under a page already?
    if cmds.listRelatives(selected_objects, parent=True):
        
        # Should they be duplicated? Or moved entirely?
        if duplicate:
            selected_objects = cmds.duplicate(selected_objects)
            cmds.parent(selected_objects, world=True)
        else:
            cmds.parent(selected_objects, world=True)

    # Select the objects we want to turn into a page:
    cmds.select(clear=True)
    cmds.select(selected_objects)
    
    # Go to the page?
    page_number = cmds.currentTime(query=True)
    go_to_page(page_number)

    # Create the page:
    set_page()
    

def display_previous_page():
    """ Sets the visibility attribute of the previous page to 1.
    
    This just sets the attribute, but doesn't key it. This means that the 
    animator can view the illustration, without worrying about the visibility of
    it moving forward. It will be reset as soon as the frame is updated.
    """
    # Get the current frame:
    current_frame = cmds.currentTime(query=True)
    
    # Get the current keys on the node:
    keys = cmds.keyframe( 'flipbook_LOC',
                          at='pagesToDisplay',
                          query=True,
                          valueChange=True)
    
    # If your key isn't in the keys, add it:
    if current_frame not in keys:
        keys.append(current_frame)
        
    # Sort the keys:
    keys.sort()
    
    # Get the index of the current frame:
    key_index = keys.index(current_frame)
    previous_key = keys[key_index-1]
    
    # Display that frame:
    _display_page(previous_key)
    

def display_next_page():
    """Sets the visibility attribute of the next page to 1.
    
    This just sets the attribute, but doesn't key it. This means that the 
    animator can view the illustration, without worrying about the visibility of
    it moving forward. It will be reset as soon as the frame is updated.
    """
    # Get the current frame:
    current_frame = cmds.currentTime(query=True)
    
    # Get the current keys on the node:
    keys = cmds.keyframe( 'flipbook_LOC',
                          at='pagesToDisplay',
                          query=True,
                          valueChange=True)
        
    # If your key isn't in the keys, add it:
    if current_frame not in keys:
        keys.append(current_frame)
        
    # Sort the keys:
    keys.sort()
    
    # Get the index of the current frame:
    key_index = keys.index(current_frame)
    next_key = keys[key_index+1]
    
    # Display that frame:
    print "Next key: %d"%(next_key)
    print keys
    _display_page(next_key)
    
    
def display_previous_pages():
    """
    """
    # Get the current frame:
    current_frame = cmds.currentTime(query=True)
    
    # Get the current keys on the node:
    keys = cmds.keyframe( 'flipbook_LOC',
                          at='pagesToDisplay',
                          query=True,
                          valueChange=True)
    
    # If your key isn't in the keys, add it:
    if current_frame not in keys:
        keys.append(current_frame)
        
    # Sort the keys:
    keys.sort()
    
    # Get the index of the current frame:
    key_index = keys.index(current_frame)
    previous_key = keys[key_index-1]
    
    # Display that frame:
    _display_pages(keys[:key_index])
    

def display_next_pages():
    """
    """
    # Get the current frame:
    current_frame = cmds.currentTime(query=True)
    
    # Get the current keys on the node:
    keys = cmds.keyframe( 'flipbook_LOC',
                          at='pagesToDisplay',
                          query=True,
                          valueChange=True)
        
    # If your key isn't in the keys, add it:
    if current_frame not in keys:
        keys.append(current_frame)
        
    # Sort the keys:
    keys.sort()
    
    # Get the index of the current frame:
    key_index = keys.index(current_frame)
    
    # Display that frame:
    _display_pages(keys[key_index+1:])


def set_framerange(start_time, end_time):
    """ Set the start and end range for playback and animation.
    """
    # Set the animation and the min/max playback values:
    cmds.playbackOptions(ast=start_time,
                         aet=end_time,
                         min=start_time,
                         max=end_time)


def save_scene():
    """
    """
    # Get the current saved scene files:
    saved_scene_files = os.listdir(_get_scenes_directory())

    time_code = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    filename = "flipbookanimation_"+time_code+".ma"
        
    cmds.file(rename=filename)
    cmds.file(save=True, type='mayaAscii')


def playblast_scene():
    """ Playblast the current scene using the min and max playback values as the
    start and end value for the playblast.
    """
    # Get the start and end frames of the animation scene:
    start_frame = cmds.playbackOptions(min=True, query=True)
    end_frame   = cmds.playbackOptions(max=True, query=True)
    
    # Create the filename of the playblast:
    time_code = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    
    filename = cmds.file(query=True, sceneName=True)
    filename += time_code
    filename += ".mov"
    
    location = os.path.join(_get_images_directory(), filename)
    
    # Playblast the scene:
    cmds.playblast(filename=location, fmt="qt", offScreen=True)
    
    
def select_pencil_tool(select=True):
    """ Select the pencil tool or revert to the selection tool based on the 
    parameter passed.
    """
    if select:
        mel.eval("PencilCurveTool")
        cmds.setToolTo("pencilContext")
    else:
        g_select = mel.eval("$tmp_value = $gSelect")
        cmds.setToolTo(g_select)
        
        
def delete_page():
    """ Delete an existing page.
    
    Comments to come...
    """
    # Get the current frame that we're on:
    current_frame = cmds.currentTime(query=True)
    
    # We're going to have to delete the group first and foremost:
    page_name = "page_%04d"%(current_frame)
    expression_name = "page_%04d_visibility_EXP"%(current_frame)
    if cmds.objExists(expression_name):
        cmds.delete(expression_name)
    if cmds.objExists(page_name):
        cmds.delete(page_name)

    # Then we need to delete the key from the master node:
    cmds.cutKey("flipbook_LOC", 
                attribute="pagesToDisplay",
                time=(current_frame, current_frame),
                option="keys",
                clear=True)
    
    # Now that that's done, we *could* set the current frame to the last keyed
    # page?...maybe.
    return


def loop_selection(num_loops, step=1):
    """ Loop over selected pages num_loop times.
    
    With the pages selected in the maya scene, loop over the pages num_loop
    times with step amount of frames between each loop. 
    """
    # If there are pages selected:
    pages = cmds.ls(selection=True)
    if pages:
        regex = re.compile(r"page_(\d{4})")
        page_vals = [int(regex.search(page).group(1)) for page in pages]
        inc_value = (page_vals[-1]+step)-page_vals[0]
        page_loop = [page_vals[i]+(j*inc_value) for j in xrange(num_loops) for i in xrange(len(page_vals))]
        
        #
        page_array = ""
        
        # Set the expression now:
        
        
        for index, page in enumerate(page_vals):
            page_name = "page_%04d"%(page)
            expr_name = "page_%04d_visbility_EXP"%(page)
            
            if cmds.objExists(expr_name):
                cmds.delete(expr_name)
                
            exp   = """
            
// This frame is in a loop...
int $visible_frames[] = {%(values)s}; 
int $end_frames[] = {%(end_values)s}; 
int $frame;
int $visible = 0;

int $index;                
for($index=0; $index<size($visible_frames); $index++)
{
    if((frame>=$visible_frames[$index])&&(frame<$end_frames[$index]))
    {
        $visible = 1;
    }
}                   

int $page = %(page)d;
int $current_keyed_frame = flipbook_LOC.pagesToDisplay;
%(page_name)s.visibility = ($page==$current_keyed_frame)||(visibilityOverride)||$visible;
"""  %{"values":','.join(map(str, page_loop[index::len(page_vals)])), "end_values":','.join(map(str, page_loop[index+1::len(page_vals)])),"page":page, "page_name":page_name}
                    
            print exp
                 
            cmds.expression(object=page_name,
                            name=expr_name, 
                            string= exp,
                            alwaysEvaluate=True)  
                
                
    go_to_page(page_vals[-1]+1)
    page_name = "page_%04d"%(page_vals[-1]+1)
    set_empty_page()
    
    return page_loop
  
  
def set_empty_page():
    """Sets the current frame as an empty page.
    
    Comments to come...
    """
    # Then group the objects into their own page. The page number is dictated
    # by the current frame:
    current_frame = cmds.currentTime(query=True)
    page_name = "page_%04d"%(current_frame)

    if not cmds.objExists(page_name):
    
        cmds.group(name=page_name, empty=True)
        
        # Add the visibility override attribute to the group name:
        cmds.addAttr(page_name, longName="visibilityOverride", attributeType="bool")
        cmds.setKeyframe(page_name+".visibilityOverride", time=1, value=0)
    
        # Set the key for this page and insert the page number into the attribute
        # on the flipbook node:
        _update_flipbook_node(page_name, current_frame)

