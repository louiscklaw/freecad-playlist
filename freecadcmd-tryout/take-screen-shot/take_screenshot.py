import FreeCAD as App
import FreeCADGui as Gui

FreeCAD.open(u"/home/logic/_workspace/freecad-playlist/freecadcmd-tryout/take-screen-shot/test-cube.FCStd")

App.setActiveDocument("test_cube")
App.ActiveDocument=App.getDocument("test_cube")

Gui.ActiveDocument=Gui.getDocument("test_cube")

for i in range(0,3):
  Gui.activeDocument().activeView().saveImage('/home/logic/_workspace/freecad-playlist/freecadcmd-tryout/take-screen-shot/screencapture/test-screenshot{}.jpg'.format(str(i)),1440,102,'White')


FreeCADGui.getMainWindow().close()
App.Console.PrintMessage('done')
