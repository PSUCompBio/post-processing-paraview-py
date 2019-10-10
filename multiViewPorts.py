import vtk
import os, sys

def main(argv):
    vtkFile = sys.argv[1]
    if os.path.exists(vtkFile):
        print("exists :",vtkFile)
    else:
        print("VTK file not found:")
        return
    datFile = sys.argv[2]
    isDatFile = False
    if os.path.exists(datFile):
        print("exists :",datFile)
        isDatFile = True
    else:
        print("dat file not found")

    reader = vtk.vtkUnstructuredGridReader()
    reader.SetFileName(vtkFile)
    reader.Update()

    surfaceFilter = vtk.vtkDataSetSurfaceFilter()
    surfaceFilter.SetInputConnection(reader.GetOutputPort())
    # surfaceFilter.Update()

    tris = vtk.vtkTriangleFilter()
    tris.SetInputConnection(surfaceFilter.GetOutputPort())
    tris.Update()

    maxSpheres = []
    minSpheres = []
    if(isDatFile):
        with open(datFile) as f:
            for line in f:
                chars = line.split()
                if chars[0] != "#":
                    MaxStrain,MaxX,MaxY,MaxZ,MaxT,MinStrain,MinX,MinY,MinZ,MinT = line.split()
                    # print(float(MaxX),float(MaxY),float(MaxZ))
                    # print(float(MinX),float(MinY),float(MinZ))
                    # print(MaxX,MaxY,MaxZ,MinX,MinY,MinZ)
                    # sphere
                    maxSource = vtk.vtkSphereSource()
                    maxSource.SetCenter(float(MaxX),float(MaxY),float(MaxZ))
                    maxSpheres.append(maxSource)
                    minSource = vtk.vtkSphereSource()
                    minSource.SetCenter(float(MinX),float(MinY),float(MinZ))
                    minSpheres.append(minSource)

    maxSpActors = []
    minSpActors = []
    for sp in maxSpheres:
        sp.SetThetaResolution(64)
        sp.SetPhiResolution(64)
        sp.SetRadius(0.005)
        sp.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(sp.GetOutput())
        sphereActor = vtk.vtkActor()
        sphereActor.GetProperty().SetColor(1.0,0.0,0.0)
        sphereActor.SetMapper(mapper)
        maxSpActors.append(sphereActor)

    for sp in minSpheres:
        sp.SetThetaResolution(64)
        sp.SetPhiResolution(64)
        sp.SetRadius(0.005)
        sp.Update()

        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(sp.GetOutput())
        sphereActor = vtk.vtkActor()
        sphereActor.GetProperty().SetColor(0.0,0.0,1.0)
        sphereActor.SetMapper(mapper)
        minSpActors.append(sphereActor)

    '''One render window, multiple viewports'''
    rw = vtk.vtkRenderWindow()
    #iren = vtk.vtkRenderWindowInteractor()
    #iren.SetRenderWindow(rw)
    renderers = []
    # Define viewport ranges
    xmins = [0, .5, 0, .5]
    xmaxs = [0.5, 1, 0.5, 1]
    ymins = [0, 0, .5, .5]
    ymaxs = [0.5, 0.5, 1, 1]
    camera_views = [[-1.0,0.0,0.0],[-1.0,-0.70,-0.7],[0.0,0.0,-1.0],[0.0,-1.0,0.0]]
    camera_viewUp = [[0.0,-1.0,0.0],[0.0,-1.0,0.0],[0.0,-1.0,0.0],[0.0,1.0,0.0]]
    for i in range(4):
        ren = vtk.vtkRenderer()
        ren.SetViewport(xmins[i], ymins[i], xmaxs[i], ymaxs[i])
        # Create a mapper and actor
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(tris.GetOutput())
        mapper.ScalarVisibilityOff()
        actor = vtk.vtkActor()
        actor.GetProperty().SetColor(1.0,0.7,0.7)
        actor.GetProperty().SetOpacity(0.25)
        actor.SetMapper(mapper)
        ren.AddActor(actor)
        for spActors in maxSpActors:
            ren.AddActor(spActors)
        for spActors in minSpActors:
            ren.AddActor(spActors)
        ren.SetBackground(1.0,1.0,1.0)

        camera = ren.GetActiveCamera()
        camera.SetPosition(camera_views[i])
        camera.SetViewUp(camera_viewUp[i])
        ren.ResetCamera()
        renderers.append(ren)

    # Create a renderwindowinteractor
    # iren = vtk.vtkRenderWindowInteractor()
    # style = vtk.vtkInteractorStyleTrackballCamera()
    # iren.SetInteractorStyle(style)
    # iren.SetRenderWindow(rw)

    # Enable user interface interactor
    #iren.Initialize()
    rw.SetWindowName('RW: Multiple ViewPorts')
    rw.SetSize(400,400)
    rw.SetOffScreenRendering(1)
    for ren in renderers:
        rw.AddRenderer(ren)
    rw.Render()
    # iren.Start()

    windowToImageFilter = vtk.vtkWindowToImageFilter()
    windowToImageFilter.SetInput(rw)
    windowToImageFilter.Update()

    writer = vtk.vtkPNGWriter()
    dirName = os.path.dirname(vtkFile)
    imageFile = os.path.join(dirName,"screenshot.png")
    writer.SetFileName(imageFile)
    writer.SetInputConnection(windowToImageFilter.GetOutputPort())
    writer.Write()
    print("Image Written at : ",imageFile)


if __name__ == '__main__':
    main(sys.argv[1:])
