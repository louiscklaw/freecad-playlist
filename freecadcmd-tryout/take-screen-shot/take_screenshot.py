
import os,sys
from pprint import pprint

import FreeCAD as App
import FreeCADGui as Gui

HOME=os.environ['HOME']
TRAVIS_BUILD_DIR=os.getenv('TRAVIS_BUILD_DIR','/home/logic/_workspace')

FreeCAD.open(u"{}/freecad-playlist/freecadcmd-tryout/take-screen-shot/test-cube.FCStd".format(TRAVIS_BUILD_DIR))

App.setActiveDocument("test_cube")
App.ActiveDocument=App.getDocument("test_cube")

Gui.ActiveDocument=Gui.getDocument("test_cube")

for i in range(0,3):
  Gui.SendMsgToActiveView("ViewFit")

  directory_to_save_image = '{}/freecad-playlist/freecadcmd-tryout/take-screen-shot/screencapture/test-screenshot{}.jpg'.format(TRAVIS_BUILD_DIR, str(1))

  # pprint(directory_to_save_image)
  # sys.exit()

  Gui.activeDocument().activeView().saveImage('{}/freecad-playlist/freecadcmd-tryout/take-screen-shot/screencapture/test-screenshot{}.jpg'.format(TRAVIS_BUILD_DIR, str(i)),1920,1080,'Black')


FreeCADGui.getMainWindow().close()
App.Console.PrintMessage('done')
