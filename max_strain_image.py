# trace generated using paraview version 5.7.0-RC4
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PVD Reader'
brainpvd = PVDReader(FileName='./brain.pvd')
brainpvd.CellArrays = ['PartID', 'AvgStrain', 'ProcID']
brainpvd.PointArrays = ['Displacements', 'Accelerations', 'Boundary']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2296, 960]

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraFocalDisk = 1.0
renderView2.Background = [0.32, 0.34, 0.43]
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1
# uncomment following to set a specific view size
# renderView2.ViewSize = [400, 400]

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView2, layout=layout1, hint=2)

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitVertical(1, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraFocalDisk = 1.0
renderView3.Background = [0.32, 0.34, 0.43]
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1
# uncomment following to set a specific view size
# renderView3.ViewSize = [400, 400]

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView3, layout=layout1, hint=4)

# set active view
SetActiveView(renderView2)

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraFocalDisk = 1.0
renderView4.Background = [0.32, 0.34, 0.43]
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.OSPRayMaterialLibrary = materialLibrary1
# uncomment following to set a specific view size
# renderView4.ViewSize = [400, 400]

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView4, layout=layout1, hint=6)

# set active source
SetActiveSource(brainpvd)

# show data in view
brainpvdDisplay = Show(brainpvd, renderView4)

# get color transfer function/color map for 'PartID'
partIDLUT = GetColorTransferFunction('PartID')

# get opacity transfer function/opacity map for 'PartID'
partIDPWF = GetOpacityTransferFunction('PartID')

# trace defaults for the display properties.
brainpvdDisplay.Representation = 'Surface'
brainpvdDisplay.ColorArrayName = ['CELLS', 'PartID']
brainpvdDisplay.LookupTable = partIDLUT
brainpvdDisplay.OSPRayScaleArray = 'Accelerations'
brainpvdDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
brainpvdDisplay.SelectOrientationVectors = 'Accelerations'
brainpvdDisplay.ScaleFactor = 0.0150744
brainpvdDisplay.SelectScaleArray = 'PartID'
brainpvdDisplay.GlyphType = 'Arrow'
brainpvdDisplay.GlyphTableIndexArray = 'PartID'
brainpvdDisplay.GaussianRadius = 0.0007537199999999999
brainpvdDisplay.SetScaleArray = ['POINTS', 'Accelerations']
brainpvdDisplay.ScaleTransferFunction = 'PiecewiseFunction'
brainpvdDisplay.OpacityArray = ['POINTS', 'Accelerations']
brainpvdDisplay.OpacityTransferFunction = 'PiecewiseFunction'
brainpvdDisplay.DataAxesGrid = 'GridAxesRepresentation'
brainpvdDisplay.PolarAxes = 'PolarAxesRepresentation'
brainpvdDisplay.ScalarOpacityFunction = partIDPWF
brainpvdDisplay.ScalarOpacityUnitDistance = 0.004822805191940828

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brainpvdDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brainpvdDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
brainpvdDisplay.SetScalarBarVisibility(renderView4, False)

# reset view to fit data
renderView4.ResetCamera()

# show data in view
brainpvdDisplay = Show(brainpvd, renderView4)

# reset view to fit data
renderView4.ResetCamera()

# show color bar/color legend
brainpvdDisplay.SetScalarBarVisibility(renderView4, False)

# update the view to ensure updated data information
renderView4.Update()

# set active view
SetActiveView(renderView3)

# show data in view
brainpvdDisplay_1 = Show(brainpvd, renderView3)

# trace defaults for the display properties.
brainpvdDisplay_1.Representation = 'Surface'
brainpvdDisplay_1.ColorArrayName = ['CELLS', 'PartID']
brainpvdDisplay_1.LookupTable = partIDLUT
brainpvdDisplay_1.OSPRayScaleArray = 'Accelerations'
brainpvdDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
brainpvdDisplay_1.SelectOrientationVectors = 'Accelerations'
brainpvdDisplay_1.ScaleFactor = 0.0150744
brainpvdDisplay_1.SelectScaleArray = 'PartID'
brainpvdDisplay_1.GlyphType = 'Arrow'
brainpvdDisplay_1.GlyphTableIndexArray = 'PartID'
brainpvdDisplay_1.GaussianRadius = 0.0007537199999999999
brainpvdDisplay_1.SetScaleArray = ['POINTS', 'Accelerations']
brainpvdDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
brainpvdDisplay_1.OpacityArray = ['POINTS', 'Accelerations']
brainpvdDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
brainpvdDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
brainpvdDisplay_1.PolarAxes = 'PolarAxesRepresentation'
brainpvdDisplay_1.ScalarOpacityFunction = partIDPWF
brainpvdDisplay_1.ScalarOpacityUnitDistance = 0.004822805191940828

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brainpvdDisplay_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brainpvdDisplay_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
brainpvdDisplay_1.SetScalarBarVisibility(renderView3, False)

# reset view to fit data
renderView3.ResetCamera()

# set active view
SetActiveView(renderView1)

# show data in view
brainpvdDisplay_2 = Show(brainpvd, renderView1)

# trace defaults for the display properties.
brainpvdDisplay_2.Representation = 'Surface'
brainpvdDisplay_2.ColorArrayName = ['CELLS', 'PartID']
brainpvdDisplay_2.LookupTable = partIDLUT
brainpvdDisplay_2.OSPRayScaleArray = 'Accelerations'
brainpvdDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
brainpvdDisplay_2.SelectOrientationVectors = 'Accelerations'
brainpvdDisplay_2.ScaleFactor = 0.0150744
brainpvdDisplay_2.SelectScaleArray = 'PartID'
brainpvdDisplay_2.GlyphType = 'Arrow'
brainpvdDisplay_2.GlyphTableIndexArray = 'PartID'
brainpvdDisplay_2.GaussianRadius = 0.0007537199999999999
brainpvdDisplay_2.SetScaleArray = ['POINTS', 'Accelerations']
brainpvdDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
brainpvdDisplay_2.OpacityArray = ['POINTS', 'Accelerations']
brainpvdDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
brainpvdDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
brainpvdDisplay_2.PolarAxes = 'PolarAxesRepresentation'
brainpvdDisplay_2.ScalarOpacityFunction = partIDPWF
brainpvdDisplay_2.ScalarOpacityUnitDistance = 0.004822805191940828

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brainpvdDisplay_2.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brainpvdDisplay_2.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
brainpvdDisplay_2.SetScalarBarVisibility(renderView1, False)

# reset view to fit data
renderView1.ResetCamera()

# set active view
SetActiveView(renderView2)

# show data in view
brainpvdDisplay_3 = Show(brainpvd, renderView2)

# trace defaults for the display properties.
brainpvdDisplay_3.Representation = 'Surface'
brainpvdDisplay_3.ColorArrayName = ['CELLS', 'PartID']
brainpvdDisplay_3.LookupTable = partIDLUT
brainpvdDisplay_3.OSPRayScaleArray = 'Accelerations'
brainpvdDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
brainpvdDisplay_3.SelectOrientationVectors = 'Accelerations'
brainpvdDisplay_3.ScaleFactor = 0.0150744
brainpvdDisplay_3.SelectScaleArray = 'PartID'
brainpvdDisplay_3.GlyphType = 'Arrow'
brainpvdDisplay_3.GlyphTableIndexArray = 'PartID'
brainpvdDisplay_3.GaussianRadius = 0.0007537199999999999
brainpvdDisplay_3.SetScaleArray = ['POINTS', 'Accelerations']
brainpvdDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
brainpvdDisplay_3.OpacityArray = ['POINTS', 'Accelerations']
brainpvdDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
brainpvdDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
brainpvdDisplay_3.PolarAxes = 'PolarAxesRepresentation'
brainpvdDisplay_3.ScalarOpacityFunction = partIDPWF
brainpvdDisplay_3.ScalarOpacityUnitDistance = 0.004822805191940828

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brainpvdDisplay_3.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brainpvdDisplay_3.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
brainpvdDisplay_3.SetScalarBarVisibility(renderView2, False)

# reset view to fit data
renderView2.ResetCamera()

# set active view
SetActiveView(renderView1)

# turn off scalar coloring
ColorBy(brainpvdDisplay_2, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView1)

# Properties modified on brainpvdDisplay_2
brainpvdDisplay_2.Opacity = 0.04

# set active view
SetActiveView(renderView3)

# turn off scalar coloring
ColorBy(brainpvdDisplay_1, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView3)

# Properties modified on brainpvdDisplay_1
brainpvdDisplay_1.Opacity = 0.04

# set active view
SetActiveView(renderView4)

# Properties modified on brainpvdDisplay
brainpvdDisplay.Opacity = 0.04

# turn off scalar coloring
ColorBy(brainpvdDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView4)

# set active view
SetActiveView(renderView2)

# Properties modified on brainpvdDisplay_3
brainpvdDisplay_3.Opacity = 0.04

# turn off scalar coloring
ColorBy(brainpvdDisplay_3, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView2)

# set active view
SetActiveView(renderView1)

# reset view to fit data
renderView1.ResetCamera()

# set active view
SetActiveView(renderView2)

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

# set active view
SetActiveView(renderView3)

# reset view to fit data
renderView3.ResetCamera()

# reset view to fit data
renderView3.ResetCamera()

# set active view
SetActiveView(renderView4)

# create a new 'Extract Location'
extractLocation1 = ExtractLocation(Input=brainpvd)

strainFile = open("maxstrain.dat","r")
contents = strainFile.read().strip()
contents = contents.split(" ")

# Read File and set location
extractLocation1.Location = [contents[0], contents[1], contents[2]]

# set active view
SetActiveView(renderView3)

# Properties modified on extractLocation1

# show data in view
extractLocation1Display = Show(extractLocation1, renderView3)

# trace defaults for the display properties.
extractLocation1Display.Representation = 'Surface'
extractLocation1Display.ColorArrayName = ['CELLS', 'PartID']
extractLocation1Display.LookupTable = partIDLUT
extractLocation1Display.OSPRayScaleArray = 'Accelerations'
extractLocation1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractLocation1Display.SelectOrientationVectors = 'Accelerations'
extractLocation1Display.ScaleFactor = 0.0002446
extractLocation1Display.SelectScaleArray = 'PartID'
extractLocation1Display.GlyphType = 'Arrow'
extractLocation1Display.GlyphTableIndexArray = 'PartID'
extractLocation1Display.GaussianRadius = 1.223e-05
extractLocation1Display.SetScaleArray = ['POINTS', 'Accelerations']
extractLocation1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractLocation1Display.OpacityArray = ['POINTS', 'Accelerations']
extractLocation1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractLocation1Display.DataAxesGrid = 'GridAxesRepresentation'
extractLocation1Display.PolarAxes = 'PolarAxesRepresentation'
extractLocation1Display.ScalarOpacityFunction = partIDPWF
extractLocation1Display.ScalarOpacityUnitDistance = 0.0036211270345018337

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractLocation1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractLocation1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
extractLocation1Display.SetScalarBarVisibility(renderView3, False)

# update the view to ensure updated data information
renderView3.Update()

# update the view to ensure updated data information
renderView4.Update()

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView4)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView3)

# Properties modified on renderView3
renderView3.OrientationAxesVisibility = 0

# Properties modified on renderView3
renderView3.OrientationAxesVisibility = 1

# Properties modified on renderView3
renderView3.OrientationAxesVisibility = 0

# set active view
SetActiveView(renderView1)

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# set active view
SetActiveView(renderView2)

# Properties modified on renderView2
renderView2.OrientationAxesVisibility = 0

# set active view
SetActiveView(renderView4)

# Properties modified on renderView4
renderView4.OrientationAxesVisibility = 0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractLocation1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractLocation1)

# set active view
SetActiveView(renderView3)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractLocation1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractLocation1)

# hide color bar/color legend
extractLocation1Display.SetScalarBarVisibility(renderView3, False)

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(extractLocation1)

# show data in view
extractLocation1Display_1 = Show(extractLocation1, renderView1)

# trace defaults for the display properties.
extractLocation1Display_1.Representation = 'Surface'
extractLocation1Display_1.ColorArrayName = ['CELLS', 'PartID']
extractLocation1Display_1.LookupTable = partIDLUT
extractLocation1Display_1.OSPRayScaleArray = 'Accelerations'
extractLocation1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
extractLocation1Display_1.SelectOrientationVectors = 'Accelerations'
extractLocation1Display_1.ScaleFactor = 0.0002446
extractLocation1Display_1.SelectScaleArray = 'PartID'
extractLocation1Display_1.GlyphType = 'Arrow'
extractLocation1Display_1.GlyphTableIndexArray = 'PartID'
extractLocation1Display_1.GaussianRadius = 1.223e-05
extractLocation1Display_1.SetScaleArray = ['POINTS', 'Accelerations']
extractLocation1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
extractLocation1Display_1.OpacityArray = ['POINTS', 'Accelerations']
extractLocation1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
extractLocation1Display_1.DataAxesGrid = 'GridAxesRepresentation'
extractLocation1Display_1.PolarAxes = 'PolarAxesRepresentation'
extractLocation1Display_1.ScalarOpacityFunction = partIDPWF
extractLocation1Display_1.ScalarOpacityUnitDistance = 0.0036211270345018337

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractLocation1Display_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractLocation1Display_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide color bar/color legend
extractLocation1Display_1.SetScalarBarVisibility(renderView1, False)

# set active view
SetActiveView(renderView2)

# show data in view
extractLocation1Display_2 = Show(extractLocation1, renderView2)

# trace defaults for the display properties.
extractLocation1Display_2.Representation = 'Surface'
extractLocation1Display_2.ColorArrayName = ['CELLS', 'PartID']
extractLocation1Display_2.LookupTable = partIDLUT
extractLocation1Display_2.OSPRayScaleArray = 'Accelerations'
extractLocation1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
extractLocation1Display_2.SelectOrientationVectors = 'Accelerations'
extractLocation1Display_2.ScaleFactor = 0.0002446
extractLocation1Display_2.SelectScaleArray = 'PartID'
extractLocation1Display_2.GlyphType = 'Arrow'
extractLocation1Display_2.GlyphTableIndexArray = 'PartID'
extractLocation1Display_2.GaussianRadius = 1.223e-05
extractLocation1Display_2.SetScaleArray = ['POINTS', 'Accelerations']
extractLocation1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
extractLocation1Display_2.OpacityArray = ['POINTS', 'Accelerations']
extractLocation1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
extractLocation1Display_2.DataAxesGrid = 'GridAxesRepresentation'
extractLocation1Display_2.PolarAxes = 'PolarAxesRepresentation'
extractLocation1Display_2.ScalarOpacityFunction = partIDPWF
extractLocation1Display_2.ScalarOpacityUnitDistance = 0.0036211270345018337

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractLocation1Display_2.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractLocation1Display_2.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide color bar/color legend
extractLocation1Display_2.SetScalarBarVisibility(renderView2, False)

# set active view
SetActiveView(renderView3)

# set active view
SetActiveView(renderView4)

# show data in view
extractLocation1Display_3 = Show(extractLocation1, renderView4)

# trace defaults for the display properties.
extractLocation1Display_3.Representation = 'Surface'
extractLocation1Display_3.ColorArrayName = ['CELLS', 'PartID']
extractLocation1Display_3.LookupTable = partIDLUT
extractLocation1Display_3.OSPRayScaleArray = 'Accelerations'
extractLocation1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
extractLocation1Display_3.SelectOrientationVectors = 'Accelerations'
extractLocation1Display_3.ScaleFactor = 0.0002446
extractLocation1Display_3.SelectScaleArray = 'PartID'
extractLocation1Display_3.GlyphType = 'Arrow'
extractLocation1Display_3.GlyphTableIndexArray = 'PartID'
extractLocation1Display_3.GaussianRadius = 1.223e-05
extractLocation1Display_3.SetScaleArray = ['POINTS', 'Accelerations']
extractLocation1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
extractLocation1Display_3.OpacityArray = ['POINTS', 'Accelerations']
extractLocation1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
extractLocation1Display_3.DataAxesGrid = 'GridAxesRepresentation'
extractLocation1Display_3.PolarAxes = 'PolarAxesRepresentation'
extractLocation1Display_3.ScalarOpacityFunction = partIDPWF
extractLocation1Display_3.ScalarOpacityUnitDistance = 0.0036211270345018337

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractLocation1Display_3.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractLocation1Display_3.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide color bar/color legend
extractLocation1Display_3.SetScalarBarVisibility(renderView4, False)

# set active source
SetActiveSource(extractLocation1)

# create a new 'Glyph'
glyph1 = Glyph(Input=extractLocation1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'Accelerations']
glyph1.ScaleArray = ['CELLS', 'PartID']
glyph1.ScaleFactor = 0.0002446
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleFactor = 0.01

# show data in view
glyph1Display = Show(glyph1, renderView4)

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'PartID']
glyph1Display.LookupTable = partIDLUT
glyph1Display.OSPRayScaleArray = 'PartID'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'AvgStrain'
glyph1Display.ScaleFactor = 0.0009999999776482583
glyph1Display.SelectScaleArray = 'PartID'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'PartID'
glyph1Display.GaussianRadius = 4.9999998882412914e-05
glyph1Display.SetScaleArray = ['POINTS', 'PartID']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'PartID']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView4, False)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# update the view to ensure updated data information
renderView3.Update()

# update the view to ensure updated data information
renderView4.Update()

# turn off scalar coloring
ColorBy(glyph1Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView4)

# change solid color
glyph1Display.AmbientColor = [1.0, 0.23137254901960785, 0.0784313725490196]
glyph1Display.DiffuseColor = [1.0, 0.23137254901960785, 0.0784313725490196]

# set active view
SetActiveView(renderView3)

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display_1 = Show(glyph1, renderView3)

# trace defaults for the display properties.
glyph1Display_1.Representation = 'Surface'
glyph1Display_1.ColorArrayName = ['POINTS', 'PartID']
glyph1Display_1.LookupTable = partIDLUT
glyph1Display_1.OSPRayScaleArray = 'PartID'
glyph1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display_1.SelectOrientationVectors = 'AvgStrain'
glyph1Display_1.ScaleFactor = 0.0009999999776482583
glyph1Display_1.SelectScaleArray = 'PartID'
glyph1Display_1.GlyphType = 'Arrow'
glyph1Display_1.GlyphTableIndexArray = 'PartID'
glyph1Display_1.GaussianRadius = 4.9999998882412914e-05
glyph1Display_1.SetScaleArray = ['POINTS', 'PartID']
glyph1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display_1.OpacityArray = ['POINTS', 'PartID']
glyph1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display_1.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display_1.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display_1.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display_1.SetScalarBarVisibility(renderView3, False)

# turn off scalar coloring
ColorBy(glyph1Display_1, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView3)

# change solid color
glyph1Display_1.AmbientColor = [1.0, 0.23137254901960785, 0.0784313725490196]
glyph1Display_1.DiffuseColor = [1.0, 0.23137254901960785, 0.0784313725490196]

# set active view
SetActiveView(renderView1)

# show data in view
glyph1Display_2 = Show(glyph1, renderView1)

# trace defaults for the display properties.
glyph1Display_2.Representation = 'Surface'
glyph1Display_2.ColorArrayName = ['POINTS', 'PartID']
glyph1Display_2.LookupTable = partIDLUT
glyph1Display_2.OSPRayScaleArray = 'PartID'
glyph1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display_2.SelectOrientationVectors = 'AvgStrain'
glyph1Display_2.ScaleFactor = 0.0009999999776482583
glyph1Display_2.SelectScaleArray = 'PartID'
glyph1Display_2.GlyphType = 'Arrow'
glyph1Display_2.GlyphTableIndexArray = 'PartID'
glyph1Display_2.GaussianRadius = 4.9999998882412914e-05
glyph1Display_2.SetScaleArray = ['POINTS', 'PartID']
glyph1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display_2.OpacityArray = ['POINTS', 'PartID']
glyph1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display_2.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display_2.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display_2.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display_2.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display_2.SetScalarBarVisibility(renderView1, False)

# turn off scalar coloring
ColorBy(glyph1Display_2, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView1)

# change solid color
glyph1Display_2.AmbientColor = [1.0, 0.23137254901960785, 0.0784313725490196]
glyph1Display_2.DiffuseColor = [1.0, 0.23137254901960785, 0.0784313725490196]

# set active view
SetActiveView(renderView2)

# show data in view
glyph1Display_3 = Show(glyph1, renderView2)

# trace defaults for the display properties.
glyph1Display_3.Representation = 'Surface'
glyph1Display_3.ColorArrayName = ['POINTS', 'PartID']
glyph1Display_3.LookupTable = partIDLUT
glyph1Display_3.OSPRayScaleArray = 'PartID'
glyph1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display_3.SelectOrientationVectors = 'AvgStrain'
glyph1Display_3.ScaleFactor = 0.0009999999776482583
glyph1Display_3.SelectScaleArray = 'PartID'
glyph1Display_3.GlyphType = 'Arrow'
glyph1Display_3.GlyphTableIndexArray = 'PartID'
glyph1Display_3.GaussianRadius = 4.9999998882412914e-05
glyph1Display_3.SetScaleArray = ['POINTS', 'PartID']
glyph1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display_3.OpacityArray = ['POINTS', 'PartID']
glyph1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display_3.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display_3.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display_3.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display_3.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display_3.SetScalarBarVisibility(renderView2, False)

# turn off scalar coloring
ColorBy(glyph1Display_3, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView2)

# change solid color
glyph1Display_3.AmbientColor = [1.0, 0.23137254901960785, 0.0784313725490196]
glyph1Display_3.DiffuseColor = [1.0, 0.23137254901960785, 0.0784313725490196]

# set active view
SetActiveView(renderView1)

# current camera placement for renderView3
renderView3.CameraPosition = [0.0, -0.362302, -0.45702962589717316]
renderView3.CameraFocalPoint = [0.0, -0.362302, -0.027605]
renderView3.CameraParallelScale = 0.11114327161821357

# current camera placement for renderView4
renderView4.CameraPosition = [-0.3873184034732583, -0.18667824094683463, -0.08715547366637026]
renderView4.CameraFocalPoint = [-1.4969885532432072e-16, -0.3623020000000002, -0.027604999999999998]
renderView4.CameraViewUp = [-0.4265386999648609, -0.8938708971587104, 0.13805635314960568]
renderView4.CameraParallelScale = 0.11114327161821357

# current camera placement for renderView1
renderView1.CameraPosition = [-0.4294246258971732, -0.362302, -0.027605]
renderView1.CameraFocalPoint = [0.0, -0.362302, -0.027605]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.11114327161821357

# current camera placement for renderView2
renderView2.CameraPosition = [0.0, -0.7917266258971731, -0.027605]
renderView2.CameraFocalPoint = [0.0, -0.362302, -0.027605]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 0.11114327161821357

# save screenshot
SaveScreenshot('./maxstrain_brain.png', layout1, SaveAllViews=1,
    ImageResolution=[2277, 895],
    TransparentBackground=1)

#### saving camera placements for all active views

# current camera placement for renderView3
renderView3.CameraPosition = [0.0, -0.362302, -0.45702962589717316]
renderView3.CameraFocalPoint = [0.0, -0.362302, -0.027605]
renderView3.CameraParallelScale = 0.11114327161821357

# current camera placement for renderView4
renderView4.CameraPosition = [-0.3873184034732583, -0.18667824094683463, -0.08715547366637026]
renderView4.CameraFocalPoint = [-1.4969885532432072e-16, -0.3623020000000002, -0.027604999999999998]
renderView4.CameraViewUp = [-0.4265386999648609, -0.8938708971587104, 0.13805635314960568]
renderView4.CameraParallelScale = 0.11114327161821357

# current camera placement for renderView1
renderView1.CameraPosition = [-0.4294246258971732, -0.362302, -0.027605]
renderView1.CameraFocalPoint = [0.0, -0.362302, -0.027605]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.11114327161821357

# current camera placement for renderView2
renderView2.CameraPosition = [0.0, -0.7917266258971731, -0.027605]
renderView2.CameraFocalPoint = [0.0, -0.362302, -0.027605]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraParallelScale = 0.11114327161821357

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).