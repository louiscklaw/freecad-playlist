import FreeCAD as App
import FreeCADGui as Gui

# import Mesh

FreeCAD.open(u"/home/logic/_workspace/freecad-playlist/thick-samples/2mm_thick_samples.FCStd")

# App.setActiveDocument("test_cube")
# App.ActiveDocument=App.getDocument("test_cube")
# Gui.ActiveDocument=Gui.getDocument("test_cube")

# for i in range(0,3):
#   Gui.SendMsgToActiveView("ViewFit")
#   Gui.activeDocument().activeView().saveImage('/home/logic/_workspace/freecad-playlist/freecadcmd-tryout/take-screen-shot/screencapture/test-screenshot{}.jpg'.format(str(i)),1920,1080,'Black')

# __objs__=[]
# __objs__.append(FreeCAD.getDocument("_mm_thick_samples").getObject("Part"))
# Mesh.export(__objs__,u"/tmp/temp.stl")

FreeCADGui.getMainWindow().close()
App.Console.PrintMessage('done')
