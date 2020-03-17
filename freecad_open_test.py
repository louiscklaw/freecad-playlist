#!/usr/bin/env python3

freecad_paths = ['/home/logic/.FreeCAD/Mod/ExplodedAssembly',
  '/home/logic/.FreeCAD/Mod/Glass',
  '/home/logic/.FreeCAD/Mod/Render',
  '/home/logic/.FreeCAD/Mod/kicadStepUpMod',
  '/home/logic/.FreeCAD/Mod/fasteners',
  '/home/logic/.FreeCAD/Mod/Assembly4',
  '/usr/share/freecad/Mod/Inspection',
  '/usr/share/freecad/Mod/Fem',
  '/usr/share/freecad/Mod/Test',
  '/usr/share/freecad/Mod/Measure',
  '/usr/share/freecad/Mod/MeshPart',
  '/usr/share/freecad/Mod/Spreadsheet',
  '/usr/share/freecad/Mod/Ship',
  '/usr/share/freecad/Mod/Points',
  '/usr/share/freecad/Mod/Raytracing',
  '/usr/share/freecad/Mod/Path',
  '/usr/share/freecad/Mod/PartDesign',
  '/usr/share/freecad/Mod/Arch',
  '/usr/share/freecad/Mod/Drawing',
  '/usr/share/freecad/Mod/Start',
  '/usr/share/freecad/Mod/TechDraw',
  '/usr/share/freecad/Mod/Complete',
  '/usr/share/freecad/Mod/AddonManager',
  '/usr/share/freecad/Mod/Import',
  '/usr/share/freecad/Mod/Surface',
  '/usr/share/freecad/Mod/Plot',
  '/usr/share/freecad/Mod/Show',
  '/usr/share/freecad/Mod/Draft',
  '/usr/share/freecad/Mod/Image',
  '/usr/share/freecad/Mod/Robot',
  '/usr/share/freecad/Mod/Idf',
  '/usr/share/freecad/Mod/Web',
  '/usr/share/freecad/Mod/Tux',
  '/usr/share/freecad/Mod/Material',
  '/usr/share/freecad/Mod/Mesh',
  '/usr/share/freecad/Mod/OpenSCAD',
  '/usr/share/freecad/Mod/Sketcher',
  '/usr/share/freecad/Mod/ReverseEngineering',
  '/usr/share/freecad/Mod/Part',
  '/usr/share/freecad/Mod',
  '/usr/lib/freecad/lib64',
  '/usr/lib/freecad-python3/lib',
  '/usr/share/freecad/Ext',
  '',
  '/usr/lib/python36.zip',
  '/usr/lib/python3.6',
  '/usr/lib/python3.6/lib-dynload',
  '/home/logic/.local/lib/python3.6/site-packages',
  '/usr/local/lib/python3.6/dist-packages',
  '/usr/lib/python3/dist-packages',
  '/home/logic/.FreeCAD/Macro',
  '/usr/lib/freecad/Macro'
]

import sys
from pprint import pprint

for freecad_path in freecad_paths:
  sys.path.append(freecad_path)

import FreeCAD as App
import Import


filename = '/home/logic/_workspace/freecad-playlist/common_parts.FCStd'
App.open(filename)
App.setActiveDocument('common_parts')
App.ActiveDocument.recompute()
App.setActiveDocument("")
App.ActiveDocument=None

print('done')