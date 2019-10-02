# trace generated using paraview version 5.7.0-RC4
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

# import the simple module from the paraview
from paraview.simple import *
# disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Partitioned Unstructured Grid Reader'
brain0000pvtu = XMLPartitionedUnstructuredGridReader(
    FileName=['brain.0000.pvtu'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1876, 1012]

# show data in view
brain0000pvtuDisplay = Show(brain0000pvtu, renderView1)

# trace defaults for the display properties.
brain0000pvtuDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
brain0000pvtuDisplay.SetScalarBarVisibility(renderView1, False)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'PartID'
partIDLUT = GetColorTransferFunction('PartID')

# get opacity transfer function/opacity map for 'PartID'
partIDPWF = GetOpacityTransferFunction('PartID')

# turn off scalar coloring
ColorBy(brain0000pvtuDisplay, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView1)

# Properties modified on brain0000pvtuDisplay
brain0000pvtuDisplay.Opacity = 0.04

# create a new 'Extract Location'
extractLocation1 = ExtractLocation(Input=brain0000pvtu)


# Get location

strainFile = open("maxstrain.dat","r")
contents = strainFile.read()
contents = contents.split(" ")

# Properties modified on extractLocation1
extractLocation1.Location = [contents[-3], contents[-2], contents[-1]]

# show data in view
extractLocation1Display = Show(extractLocation1, renderView1)

# trace defaults for the display properties.
extractLocation1Display.Representation = 'Surface'

# show color bar/color legend
extractLocation1Display.SetScalarBarVisibility(renderView1, False)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Glyph'
glyph1 = Glyph(Input=extractLocation1,
               GlyphType='Arrow')

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleFactor = 0.01

# show data in view
glyph1Display = Show(glyph1, renderView1)

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, False)

# update the view to ensure updated data information
renderView1.Update()

# turn off scalar coloring
ColorBy(glyph1Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(partIDLUT, renderView1)

# change solid color
glyph1Display.AmbientColor = [1.0, 0.23921568627450981, 0.09019607843137255]
glyph1Display.DiffuseColor = [1.0, 0.23921568627450981, 0.09019607843137255]

# saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.40911776934797245, -
                              0.23228589444879838, -0.03873929063592235]
renderView1.CameraFocalPoint = [-4.6995944660221975e-17, -0.362302, -0.027605]
renderView1.CameraViewUp = [-0.27638048841926344, -
                            0.8278794363880928, 0.48808755815618116]
renderView1.CameraParallelScale = 0.11114327161821357

# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

SaveScreenshot('/Users/eralpsahin/Downloads/test1.png', renderView1, ImageResolution=[1876, 1012],
               FontScaling='Scale fonts proportionally',
               OverrideColorPalette='',
               StereoMode='No change',
               TransparentBackground=1,
               # PNG options
               CompressionLevel='1')
