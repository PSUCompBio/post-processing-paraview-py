# trace generated using paraview version 5.7.0-RC4
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
brain0000pvtu = XMLPartitionedUnstructuredGridReader(FileName=['./brain.0000.pvtu'])
brain0000pvtu.CellArrayStatus = ['PartID', 'AvgStrain', 'ProcID']
brain0000pvtu.PointArrayStatus = ['Displacements', 'Accelerations', 'Boundary']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
renderView1.ViewSize = [2296, 1012]

# show data in view
brain0000pvtuDisplay = Show(brain0000pvtu, renderView1)

# get color transfer function/color map for 'PartID'
partIDLUT = GetColorTransferFunction('PartID')

# get opacity transfer function/opacity map for 'PartID'
partIDPWF = GetOpacityTransferFunction('PartID')

# trace defaults for the display properties.
brain0000pvtuDisplay.Representation = 'Surface'
brain0000pvtuDisplay.ColorArrayName = ['CELLS', 'PartID']
brain0000pvtuDisplay.LookupTable = partIDLUT
brain0000pvtuDisplay.OSPRayScaleArray = 'Accelerations'
brain0000pvtuDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
brain0000pvtuDisplay.SelectOrientationVectors = 'Accelerations'
brain0000pvtuDisplay.ScaleFactor = 0.0150744
brain0000pvtuDisplay.SelectScaleArray = 'PartID'
brain0000pvtuDisplay.GlyphType = 'Arrow'
brain0000pvtuDisplay.GlyphTableIndexArray = 'PartID'
brain0000pvtuDisplay.GaussianRadius = 0.0007537199999999999
brain0000pvtuDisplay.SetScaleArray = ['POINTS', 'Accelerations']
brain0000pvtuDisplay.ScaleTransferFunction = 'PiecewiseFunction'
brain0000pvtuDisplay.OpacityArray = ['POINTS', 'Accelerations']
brain0000pvtuDisplay.OpacityTransferFunction = 'PiecewiseFunction'
brain0000pvtuDisplay.DataAxesGrid = 'GridAxesRepresentation'
brain0000pvtuDisplay.PolarAxes = 'PolarAxesRepresentation'
brain0000pvtuDisplay.ScalarOpacityFunction = partIDPWF
brain0000pvtuDisplay.ScalarOpacityUnitDistance = 0.004822805191940828

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brain0000pvtuDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brain0000pvtuDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
brain0000pvtuDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

AssignViewToLayout(renderView1)

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# split cell
layout1.SplitHorizontal(2, 0.5)

# close an empty frame
layout1.Collapse(6)

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitVertical(1, 0.5)

# set active view
SetActiveView(None)

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
AssignViewToLayout(view=renderView2, layout=layout1, hint=4)

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
AssignViewToLayout(view=renderView3, layout=layout1, hint=6)

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
AssignViewToLayout(view=renderView4, layout=layout1, hint=5)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(brain0000pvtu)

# show data in view
brain0000pvtuDisplay_1 = Show(brain0000pvtu, renderView2)

# trace defaults for the display properties.
brain0000pvtuDisplay_1.Representation = 'Surface'
brain0000pvtuDisplay_1.ColorArrayName = ['CELLS', 'PartID']
brain0000pvtuDisplay_1.LookupTable = partIDLUT
brain0000pvtuDisplay_1.OSPRayScaleArray = 'Accelerations'
brain0000pvtuDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
brain0000pvtuDisplay_1.SelectOrientationVectors = 'Accelerations'
brain0000pvtuDisplay_1.ScaleFactor = 0.0150744
brain0000pvtuDisplay_1.SelectScaleArray = 'PartID'
brain0000pvtuDisplay_1.GlyphType = 'Arrow'
brain0000pvtuDisplay_1.GlyphTableIndexArray = 'PartID'
brain0000pvtuDisplay_1.GaussianRadius = 0.0007537199999999999
brain0000pvtuDisplay_1.SetScaleArray = ['POINTS', 'Accelerations']
brain0000pvtuDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
brain0000pvtuDisplay_1.OpacityArray = ['POINTS', 'Accelerations']
brain0000pvtuDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
brain0000pvtuDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
brain0000pvtuDisplay_1.PolarAxes = 'PolarAxesRepresentation'
brain0000pvtuDisplay_1.ScalarOpacityFunction = partIDPWF
brain0000pvtuDisplay_1.ScalarOpacityUnitDistance = 0.004822805191940828

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brain0000pvtuDisplay_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brain0000pvtuDisplay_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
brain0000pvtuDisplay_1.SetScalarBarVisibility(renderView2, True)

# reset view to fit data
renderView2.ResetCamera()

# set active view
SetActiveView(renderView4)

# show data in view
brain0000pvtuDisplay_2 = Show(brain0000pvtu, renderView4)

# trace defaults for the display properties.
brain0000pvtuDisplay_2.Representation = 'Surface'
brain0000pvtuDisplay_2.ColorArrayName = ['CELLS', 'PartID']
brain0000pvtuDisplay_2.LookupTable = partIDLUT
brain0000pvtuDisplay_2.OSPRayScaleArray = 'Accelerations'
brain0000pvtuDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
brain0000pvtuDisplay_2.SelectOrientationVectors = 'Accelerations'
brain0000pvtuDisplay_2.ScaleFactor = 0.0150744
brain0000pvtuDisplay_2.SelectScaleArray = 'PartID'
brain0000pvtuDisplay_2.GlyphType = 'Arrow'
brain0000pvtuDisplay_2.GlyphTableIndexArray = 'PartID'
brain0000pvtuDisplay_2.GaussianRadius = 0.0007537199999999999
brain0000pvtuDisplay_2.SetScaleArray = ['POINTS', 'Accelerations']
brain0000pvtuDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
brain0000pvtuDisplay_2.OpacityArray = ['POINTS', 'Accelerations']
brain0000pvtuDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
brain0000pvtuDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
brain0000pvtuDisplay_2.PolarAxes = 'PolarAxesRepresentation'
brain0000pvtuDisplay_2.ScalarOpacityFunction = partIDPWF
brain0000pvtuDisplay_2.ScalarOpacityUnitDistance = 0.004822805191940828

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brain0000pvtuDisplay_2.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brain0000pvtuDisplay_2.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
brain0000pvtuDisplay_2.SetScalarBarVisibility(renderView4, True)

# reset view to fit data
renderView4.ResetCamera()

# set active view
SetActiveView(renderView3)

# show data in view
brain0000pvtuDisplay_3 = Show(brain0000pvtu, renderView3)

# trace defaults for the display properties.
brain0000pvtuDisplay_3.Representation = 'Surface'
brain0000pvtuDisplay_3.ColorArrayName = ['CELLS', 'PartID']
brain0000pvtuDisplay_3.LookupTable = partIDLUT
brain0000pvtuDisplay_3.OSPRayScaleArray = 'Accelerations'
brain0000pvtuDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
brain0000pvtuDisplay_3.SelectOrientationVectors = 'Accelerations'
brain0000pvtuDisplay_3.ScaleFactor = 0.0150744
brain0000pvtuDisplay_3.SelectScaleArray = 'PartID'
brain0000pvtuDisplay_3.GlyphType = 'Arrow'
brain0000pvtuDisplay_3.GlyphTableIndexArray = 'PartID'
brain0000pvtuDisplay_3.GaussianRadius = 0.0007537199999999999
brain0000pvtuDisplay_3.SetScaleArray = ['POINTS', 'Accelerations']
brain0000pvtuDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
brain0000pvtuDisplay_3.OpacityArray = ['POINTS', 'Accelerations']
brain0000pvtuDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
brain0000pvtuDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
brain0000pvtuDisplay_3.PolarAxes = 'PolarAxesRepresentation'
brain0000pvtuDisplay_3.ScalarOpacityFunction = partIDPWF
brain0000pvtuDisplay_3.ScalarOpacityUnitDistance = 0.004822805191940828

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
brain0000pvtuDisplay_3.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
brain0000pvtuDisplay_3.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
brain0000pvtuDisplay_3.SetScalarBarVisibility(renderView3, True)

# reset view to fit data
renderView3.ResetCamera()

# set active view
SetActiveView(renderView1)

# reset view to fit data
renderView1.ResetCamera()

# set active view
SetActiveView(renderView4)

# reset view to fit data
renderView4.ResetCamera()

# set active view
SetActiveView(renderView2)

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

# set active view
SetActiveView(renderView4)

# reset view to fit data
renderView4.ResetCamera()

# reset view to fit data
renderView4.ResetCamera()

# reset view to fit data
renderView4.ResetCamera()

# reset view to fit data
renderView4.ResetCamera()

# reset view to fit data
renderView4.ResetCamera()

# reset view to fit data
renderView4.ResetCamera()

# set active view
SetActiveView(renderView2)

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

# reset view to fit data
renderView2.ResetCamera()

# set active view
SetActiveView(renderView3)

# set active source
SetActiveSource(brain0000pvtu)

# create a new 'Extract Location'
extractLocation1 = ExtractLocation(Input=brain0000pvtu)

strainFile = open("maxstrain.dat","r")
contents = strainFile.read().strip()
contents = contents.split(" ")

# Read File and set location
extractLocation1.Location = [contents[0], contents[1], contents[2]]

# show data in view
extractLocation1Display = Show(extractLocation1, renderView3)

# trace defaults for the display properties.
extractLocation1Display.Representation = 'Surface'
extractLocation1Display.ColorArrayName = ['CELLS', 'PartID']
extractLocation1Display.LookupTable = partIDLUT
extractLocation1Display.OSPRayScaleArray = 'Accelerations'
extractLocation1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractLocation1Display.SelectOrientationVectors = 'Accelerations'
extractLocation1Display.ScaleFactor = 0.00040859999999999996
extractLocation1Display.SelectScaleArray = 'PartID'
extractLocation1Display.GlyphType = 'Arrow'
extractLocation1Display.GlyphTableIndexArray = 'PartID'
extractLocation1Display.GaussianRadius = 2.0429999999999996e-05
extractLocation1Display.SetScaleArray = ['POINTS', 'Accelerations']
extractLocation1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractLocation1Display.OpacityArray = ['POINTS', 'Accelerations']
extractLocation1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractLocation1Display.DataAxesGrid = 'GridAxesRepresentation'
extractLocation1Display.PolarAxes = 'PolarAxesRepresentation'
extractLocation1Display.ScalarOpacityFunction = partIDPWF
extractLocation1Display.ScalarOpacityUnitDistance = 0.005748640013081363

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractLocation1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractLocation1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# hide data in view
Hide(brain0000pvtu, renderView3)

# show color bar/color legend
extractLocation1Display.SetScalarBarVisibility(renderView3, True)

# update the view to ensure updated data information
renderView3.Update()

# set active source
SetActiveSource(brain0000pvtu)

# show data in view
brain0000pvtuDisplay_3 = Show(brain0000pvtu, renderView3)

# show color bar/color legend
brain0000pvtuDisplay_3.SetScalarBarVisibility(renderView3, True)

# set active source
SetActiveSource(brain0000pvtu)

# set active source
SetActiveSource(extractLocation1)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(extractLocation1)

# show data in view
extractLocation1Display_1 = Show(extractLocation1, renderView2)

# trace defaults for the display properties.
extractLocation1Display_1.Representation = 'Surface'
extractLocation1Display_1.ColorArrayName = ['CELLS', 'PartID']
extractLocation1Display_1.LookupTable = partIDLUT
extractLocation1Display_1.OSPRayScaleArray = 'Accelerations'
extractLocation1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
extractLocation1Display_1.SelectOrientationVectors = 'Accelerations'
extractLocation1Display_1.ScaleFactor = 0.00040859999999999996
extractLocation1Display_1.SelectScaleArray = 'PartID'
extractLocation1Display_1.GlyphType = 'Arrow'
extractLocation1Display_1.GlyphTableIndexArray = 'PartID'
extractLocation1Display_1.GaussianRadius = 2.0429999999999996e-05
extractLocation1Display_1.SetScaleArray = ['POINTS', 'Accelerations']
extractLocation1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
extractLocation1Display_1.OpacityArray = ['POINTS', 'Accelerations']
extractLocation1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
extractLocation1Display_1.DataAxesGrid = 'GridAxesRepresentation'
extractLocation1Display_1.PolarAxes = 'PolarAxesRepresentation'
extractLocation1Display_1.ScalarOpacityFunction = partIDPWF
extractLocation1Display_1.ScalarOpacityUnitDistance = 0.005748640013081363

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractLocation1Display_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractLocation1Display_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
extractLocation1Display_1.SetScalarBarVisibility(renderView2, True)

# set active view
SetActiveView(renderView1)

# show data in view
extractLocation1Display_2 = Show(extractLocation1, renderView1)

# trace defaults for the display properties.
extractLocation1Display_2.Representation = 'Surface'
extractLocation1Display_2.ColorArrayName = ['CELLS', 'PartID']
extractLocation1Display_2.LookupTable = partIDLUT
extractLocation1Display_2.OSPRayScaleArray = 'Accelerations'
extractLocation1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
extractLocation1Display_2.SelectOrientationVectors = 'Accelerations'
extractLocation1Display_2.ScaleFactor = 0.00040859999999999996
extractLocation1Display_2.SelectScaleArray = 'PartID'
extractLocation1Display_2.GlyphType = 'Arrow'
extractLocation1Display_2.GlyphTableIndexArray = 'PartID'
extractLocation1Display_2.GaussianRadius = 2.0429999999999996e-05
extractLocation1Display_2.SetScaleArray = ['POINTS', 'Accelerations']
extractLocation1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
extractLocation1Display_2.OpacityArray = ['POINTS', 'Accelerations']
extractLocation1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
extractLocation1Display_2.DataAxesGrid = 'GridAxesRepresentation'
extractLocation1Display_2.PolarAxes = 'PolarAxesRepresentation'
extractLocation1Display_2.ScalarOpacityFunction = partIDPWF
extractLocation1Display_2.ScalarOpacityUnitDistance = 0.005748640013081363

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractLocation1Display_2.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractLocation1Display_2.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
extractLocation1Display_2.SetScalarBarVisibility(renderView1, True)

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
extractLocation1Display_3.ScaleFactor = 0.00040859999999999996
extractLocation1Display_3.SelectScaleArray = 'PartID'
extractLocation1Display_3.GlyphType = 'Arrow'
extractLocation1Display_3.GlyphTableIndexArray = 'PartID'
extractLocation1Display_3.GaussianRadius = 2.0429999999999996e-05
extractLocation1Display_3.SetScaleArray = ['POINTS', 'Accelerations']
extractLocation1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
extractLocation1Display_3.OpacityArray = ['POINTS', 'Accelerations']
extractLocation1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
extractLocation1Display_3.DataAxesGrid = 'GridAxesRepresentation'
extractLocation1Display_3.PolarAxes = 'PolarAxesRepresentation'
extractLocation1Display_3.ScalarOpacityFunction = partIDPWF
extractLocation1Display_3.ScalarOpacityUnitDistance = 0.005748640013081363

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractLocation1Display_3.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractLocation1Display_3.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show color bar/color legend
extractLocation1Display_3.SetScalarBarVisibility(renderView4, True)

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(brain0000pvtu)

# turn off scalar coloring
ColorBy(brain0000pvtuDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView1)

# Properties modified on brain0000pvtuDisplay
brain0000pvtuDisplay.Opacity = 0.04

# set active view
SetActiveView(renderView2)

# turn off scalar coloring
ColorBy(brain0000pvtuDisplay_1, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView2)

# Properties modified on brain0000pvtuDisplay_1
brain0000pvtuDisplay_1.Opacity = 0.04

# set active view
SetActiveView(renderView3)

# turn off scalar coloring
ColorBy(brain0000pvtuDisplay_3, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView3)

# Properties modified on brain0000pvtuDisplay_3
brain0000pvtuDisplay_3.Opacity = 0.04

# set active view
SetActiveView(renderView4)

# turn off scalar coloring
ColorBy(brain0000pvtuDisplay_2, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView4)

# Properties modified on brain0000pvtuDisplay_2
brain0000pvtuDisplay_2.Opacity = 0.04

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(extractLocation1)

# set active view
SetActiveView(renderView1)

# create a new 'Glyph'
glyph1 = Glyph(Input=extractLocation1,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'Accelerations']
glyph1.ScaleArray = ['CELLS', 'PartID']
glyph1.ScaleFactor = 0.00040859999999999996
glyph1.GlyphTransform = 'Transform2'

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleFactor = 0.01

# show data in view
glyph1Display = Show(glyph1, renderView1)

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'PartID']
glyph1Display.LookupTable = partIDLUT
glyph1Display.OSPRayScaleArray = 'PartID'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'AvgStrain'
glyph1Display.ScaleFactor = 0.0009999997913837434
glyph1Display.SelectScaleArray = 'PartID'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'PartID'
glyph1Display.GaussianRadius = 4.9999989569187166e-05
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
glyph1Display.SetScalarBarVisibility(renderView1, True)

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
HideScalarBarIfNotNeeded(partIDLUT, renderView1)

# change solid color
glyph1Display.AmbientColor = [1.0, 0.3215686274509804, 0.054901960784313725]
glyph1Display.DiffuseColor = [1.0, 0.3215686274509804, 0.054901960784313725]

# set active view
SetActiveView(renderView4)

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display_1 = Show(glyph1, renderView4)

# trace defaults for the display properties.
glyph1Display_1.Representation = 'Surface'
glyph1Display_1.ColorArrayName = ['POINTS', 'PartID']
glyph1Display_1.LookupTable = partIDLUT
glyph1Display_1.OSPRayScaleArray = 'PartID'
glyph1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display_1.SelectOrientationVectors = 'AvgStrain'
glyph1Display_1.ScaleFactor = 0.0009999997913837434
glyph1Display_1.SelectScaleArray = 'PartID'
glyph1Display_1.GlyphType = 'Arrow'
glyph1Display_1.GlyphTableIndexArray = 'PartID'
glyph1Display_1.GaussianRadius = 4.9999989569187166e-05
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
glyph1Display_1.SetScalarBarVisibility(renderView4, True)

# turn off scalar coloring
ColorBy(glyph1Display_1, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView4)

# change solid color
glyph1Display_1.AmbientColor = [1.0, 0.3215686274509804, 0.054901960784313725]
glyph1Display_1.DiffuseColor = [1.0, 0.3215686274509804, 0.054901960784313725]

# set active view
SetActiveView(renderView2)

# show data in view
glyph1Display_2 = Show(glyph1, renderView2)

# trace defaults for the display properties.
glyph1Display_2.Representation = 'Surface'
glyph1Display_2.ColorArrayName = ['POINTS', 'PartID']
glyph1Display_2.LookupTable = partIDLUT
glyph1Display_2.OSPRayScaleArray = 'PartID'
glyph1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display_2.SelectOrientationVectors = 'AvgStrain'
glyph1Display_2.ScaleFactor = 0.0009999997913837434
glyph1Display_2.SelectScaleArray = 'PartID'
glyph1Display_2.GlyphType = 'Arrow'
glyph1Display_2.GlyphTableIndexArray = 'PartID'
glyph1Display_2.GaussianRadius = 4.9999989569187166e-05
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
glyph1Display_2.SetScalarBarVisibility(renderView2, True)

# turn off scalar coloring
ColorBy(glyph1Display_2, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView2)

# change solid color
glyph1Display_2.AmbientColor = [1.0, 0.3215686274509804, 0.054901960784313725]
glyph1Display_2.DiffuseColor = [1.0, 0.3215686274509804, 0.054901960784313725]

# set active view
SetActiveView(renderView3)

# show data in view
glyph1Display_3 = Show(glyph1, renderView3)

# trace defaults for the display properties.
glyph1Display_3.Representation = 'Surface'
glyph1Display_3.ColorArrayName = ['POINTS', 'PartID']
glyph1Display_3.LookupTable = partIDLUT
glyph1Display_3.OSPRayScaleArray = 'PartID'
glyph1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display_3.SelectOrientationVectors = 'AvgStrain'
glyph1Display_3.ScaleFactor = 0.0009999997913837434
glyph1Display_3.SelectScaleArray = 'PartID'
glyph1Display_3.GlyphType = 'Arrow'
glyph1Display_3.GlyphTableIndexArray = 'PartID'
glyph1Display_3.GaussianRadius = 4.9999989569187166e-05
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
glyph1Display_3.SetScalarBarVisibility(renderView3, True)

# turn off scalar coloring
ColorBy(glyph1Display_3, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView3)

# change solid color
glyph1Display_3.AmbientColor = [1.0, 0.3215686274509804, 0.054901960784313725]
glyph1Display_3.DiffuseColor = [1.0, 0.3215686274509804, 0.054901960784313725]

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(extractLocation1)

# hide color bar/color legend
extractLocation1Display_2.SetScalarBarVisibility(renderView1, False)

# set active view
SetActiveView(renderView4)

# hide color bar/color legend
extractLocation1Display_3.SetScalarBarVisibility(renderView4, False)

# set active view
SetActiveView(renderView2)

# hide color bar/color legend
extractLocation1Display_1.SetScalarBarVisibility(renderView2, False)

# set active view
SetActiveView(renderView3)

# hide color bar/color legend
extractLocation1Display.SetScalarBarVisibility(renderView3, False)

# set active view
SetActiveView(renderView1)

# Properties modified on renderView1
renderView1.OrientationAxesVisibility = 0

# set active view
SetActiveView(renderView4)

# Properties modified on renderView4
renderView4.OrientationAxesVisibility = 0

# set active view
SetActiveView(renderView2)

# Properties modified on renderView2
renderView2.OrientationAxesVisibility = 0

# set active view
SetActiveView(renderView3)

# Properties modified on renderView3
renderView3.OrientationAxesVisibility = 0

# set active view
SetActiveView(renderView1)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# set active view
SetActiveView(renderView4)

# reset view to fit data
renderView4.ResetCamera()

# set active view
SetActiveView(renderView1)

# current camera placement for renderView2
renderView2.CameraPosition = [0.0, -0.362302, -0.45702962589717316]
renderView2.CameraFocalPoint = [0.0, -0.362302, -0.027605]
renderView2.CameraParallelScale = 0.11114327161821357

# current camera placement for renderView4
renderView4.CameraPosition = [0.0, 0.06866384170091183, -0.027605]
renderView4.CameraFocalPoint = [0.0, -0.3637582446472588, -0.027605]
renderView4.CameraViewUp = [0.0, 0.0, 1.0]
renderView4.CameraParallelScale = 0.1119190714698733

# current camera placement for renderView1
renderView1.CameraPosition = [-0.43242208634817064, -0.3637582446472588, -0.027605]
renderView1.CameraFocalPoint = [0.0, -0.3637582446472588, -0.027605]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.1119190714698733

# current camera placement for renderView3
renderView3.CameraPosition = [-0.42183551419825904, -0.28848410626485527, -0.05940479327795262]
renderView3.CameraFocalPoint = [2.583493778741474e-16, -0.3623019999999991, -0.027605000000000157]
renderView3.CameraViewUp = [-0.17572548533082535, -0.983236788701942, 0.04864124945289468]
renderView3.CameraParallelScale = 0.11114327161821357

# save screenshot
SaveScreenshot('./brainstrain.png', layout1, SaveAllViews=1,
    ImageResolution=[2277, 947],
    TransparentBackground=1)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
