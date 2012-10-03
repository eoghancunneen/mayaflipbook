Documentation for the mayaflipbook UI module
*********************************************

In this module we check to see if the user has the PyQt4 module loaded and 
available. If it is available, we create a PyQt derived UI which is far nicer
to use both aesthetically, but also in terms of maintainability. If the user
does not have the PyQt module loaded, the script falls back on a default native
Maya/MEL user interface. The user interface allows the user to operate each of
the commands necessary to run the Flipbook tool and to control its engine.

Some details to add here...
===========================


.. automodule:: mayaflipbook.ecanimationflipbookui
   :members:
   
   
    .. autoclass:: mayaflipbook.ecanimationflipbookui.MayaFlipbookPyqt
        :members: