# state file generated using paraview version 4.3.1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
import time
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

f=open('/p/lscratchh/koneru2/shktb_AST17/timeSteps-test.dat',"r")
times = f.readlines()
basedir = "/p/lscratchh/koneru2/shktb_AST17/VIZALL"
#basedir = "/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_MM15IP"
filename = "/shktb_"
ext = ".pvtu"
extPcls = ".pcls.pvtu"
basedirWrite = "/p/lscratchh/koneru2/shktb_AST17/PNGMV-test"
#basedirWrite = "/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_MM15IP/PNGS"
filenameWrite = "/M1663D_"
#filenameWrite = "/MM15IP_"
extWrite = ".png"

for currTime in times:
        timeStamp = "%.5E" % float(currTime)
        tempPNG = float(timeStamp)
        timePNG = "%03d" % int(tempPNG*1E6)
        #timeStamp = "%.5E" % float(currTime)
        timeStamp = str(timeStamp)
        timePNG = str(timePNG)
        parts = [basedir, filename, timeStamp, ext]
        fileLoc = ''.join(parts)
        print fileLoc,
        parts = [basedir, filename, timeStamp, extPcls]
        fileLocPcls = ''.join(parts)
        print fileLocPcls,


        # Create a new 'Render View'
        renderView1 = CreateView('RenderView')
        renderView1.ViewSize = [1600, 383]
        renderView1.OrientationAxesVisibility = 0
        renderView1.CenterOfRotation = [0.139141411118526, 0.00248620830684373, 0.00499999988824129]
        renderView1.StereoType = 0
        renderView1.CameraPosition = [0.0799080965819302, 0.0540748649202405, 0.0636053958967809]
        renderView1.CameraFocalPoint = [0.154440872954601, -0.00556274772717295, -0.00650778746958239]
        renderView1.CameraViewUp = [0.28207746045249693, 0.8577599622706518, -0.42974428842059087]
        renderView1.CameraParallelScale = 0.175142795897187
        renderView1.Background = [0.32, 0.34, 0.43]
        
        aLayout = GetLayout()
        aLayout.SplitVertical(0, 0.5)

        # Create a new 'Render View'
        renderView2 = CreateView('RenderView')
        renderView2.ViewSize = [1600, 197]
        renderView2.InteractionMode = '2D'
        renderView2.OrientationAxesVisibility = 0
        renderView2.CenterOfRotation = [0.174999997019768, 0.00499999988824129, 9.99999974737875e-06]
        renderView2.StereoType = 0
        renderView2.CameraPosition = [0.174999997019768, 0.00499999988824129, 0.676433989388009]
        renderView2.CameraFocalPoint = [0.174999997019768, 0.00499999988824129, 9.99999974737875e-06]
        renderView2.CameraParallelScale = 0.00829180933043838
        renderView2.Background = [0.32, 0.34, 0.43]
        
        aLayout = GetLayout()
        aLayout.SplitVertical(2, 0.5)

        # Create a new 'Render View'
        renderView3 = CreateView('RenderView')
        renderView3.ViewSize = [1600, 197]
        renderView3.InteractionMode = '2D'
        renderView3.OrientationAxesVisibility = 0
        renderView3.CenterOfRotation = [0.174999997019768, 0.00989999994635582, 0.00499999988824129]
        renderView3.StereoType = 0
        renderView3.CameraPosition = [0.174999997019768, -0.666523989441906, 0.00499999988824129]
        renderView3.CameraFocalPoint = [0.174999997019768, 0.00989999994635582, 0.00499999988824129]
        renderView3.CameraViewUp = [0.0, 0.0, 1.0]
        renderView3.CameraParallelScale = 0.00829180933043838
        renderView3.Background = [0.32, 0.34, 0.43]
        
        # ----------------------------------------------------------------
        # setup the data processing pipelines
        # ----------------------------------------------------------------
        
        # create a new 'XML Partitioned Unstructured Grid Reader'
        shktb_00000E00pvtu = XMLPartitionedUnstructuredGridReader(FileName=fileLoc)
        shktb_00000E00pvtu.CellArrayStatus = ['Gas Density', 'Momentum', 'Pressure', 'Particle Volume Fraction']
        
        # create a new 'Slice'
        slice2 = Slice(Input=shktb_00000E00pvtu)
        slice2.SliceType = 'Plane'
        slice2.SliceOffsetValues = [0.0]
        
        # init the 'Plane' selected for 'SliceType'
        slice2.SliceType.Origin = [0.0, 1e-05, 0.0]
        slice2.SliceType.Normal = [0.0, 1.0, 0.0]
        
        # create a new 'XML Partitioned Unstructured Grid Reader'
        #shktb_00000E00pclspvtu = XMLPartitionedUnstructuredGridReader(FileName=['/p/lscratchh/koneru2/shktb_AST17/VIZT0/shktb_0.00000E+00.pcls.pvtu'])
        shktb_00000E00pclspvtu = XMLPartitionedUnstructuredGridReader(FileName=fileLocPcls)
        shktb_00000E00pclspvtu.PointArrayStatus = ['cParticle Velocity', 'cParticle Diameter']
        
        # create a new 'Slice'
        slice1 = Slice(Input=shktb_00000E00pvtu)
        slice1.SliceType = 'Plane'
        slice1.SliceOffsetValues = [0.0]
        
        # init the 'Plane' selected for 'SliceType'
        slice1.SliceType.Origin = [0.0, 0.0, 1e-05]
        slice1.SliceType.Normal = [0.0, 0.0, 1.0]
        
        # create a new 'Gradient Of Unstructured DataSet'
        gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=slice1)
        gradientOfUnstructuredDataSet1.ScalarArray = ['CELLS', 'Gas Density']
        gradientOfUnstructuredDataSet1.ResultArrayName = 'gradRho'
        
        # create a new 'Glyph'
        glyph1 = Glyph(Input=shktb_00000E00pclspvtu,
            GlyphType='Sphere')
        glyph1.Scalars = ['POINTS', 'cParticle Diameter']
        glyph1.Vectors = ['POINTS', 'cParticle Velocity']
        glyph1.ScaleFactor = 0.0002
        glyph1.MaximumNumberOfSamplePoints = 3000000
        glyph1.GlyphTransform = 'Transform2'
        
        # create a new 'Slice'
        slice3 = Slice(Input=shktb_00000E00pvtu)
        slice3.SliceType = 'Plane'
        slice3.SliceOffsetValues = [0.0]
        
        # init the 'Plane' selected for 'SliceType'
        slice3.SliceType.Origin = [0.0, 0.0099, 0.0]
        slice3.SliceType.Normal = [0.0, 1.0, 0.0]
        
        # ----------------------------------------------------------------
        # setup color maps and opacity mapes used in the visualization
        # note: the Get..() functions create a new object, if needed
        # ----------------------------------------------------------------
        
        # get color transfer function/color map for 'gradRho'
        gradRhoLUT = GetColorTransferFunction('gradRho')
        gradRhoLUT.RGBPoints = [0.0, 1.0, 1.0, 1.0, 6015.0, 0.0, 0.0, 0.0]
        gradRhoLUT.LockScalarRange = 1
        gradRhoLUT.ColorSpace = 'RGB'
        gradRhoLUT.NanColor = [1.0, 0.0, 0.0]
        gradRhoLUT.ScalarRangeInitialized = 1.0
        
        # get opacity transfer function/opacity map for 'gradRho'
        gradRhoPWF = GetOpacityTransferFunction('gradRho')
        gradRhoPWF.Points = [0.0, 0.0, 0.5, 0.0, 6015.0, 1.0, 0.5, 0.0]
        gradRhoPWF.ScalarRangeInitialized = 1
        
        # get color transfer function/color map for 'cParticleVelocity'
        cParticleVelocityLUT = GetColorTransferFunction('cParticleVelocity')
        cParticleVelocityLUT.RGBPoints = [0.0, 0.278431, 0.278431, 0.858824, 11.44, 0.0, 0.0, 0.360784, 22.8, 0.0, 1.0, 1.0, 34.32, 0.0, 0.501961, 0.0, 45.68, 1.0, 1.0, 0.0, 57.12, 1.0, 0.380392, 0.0, 68.56, 0.419608, 0.0, 0.0, 80.0, 0.878431, 0.301961, 0.301961]
        cParticleVelocityLUT.LockScalarRange = 1
        cParticleVelocityLUT.ColorSpace = 'RGB'
        cParticleVelocityLUT.NanColor = [1.0, 1.0, 0.0]
        cParticleVelocityLUT.ScalarRangeInitialized = 1.0
        
        # get opacity transfer function/opacity map for 'cParticleVelocity'
        cParticleVelocityPWF = GetOpacityTransferFunction('cParticleVelocity')
        cParticleVelocityPWF.Points = [0.0, 0.0, 0.5, 0.0, 80.0, 1.0, 0.5, 0.0]
        cParticleVelocityPWF.ScalarRangeInitialized = 1
        
        # get color transfer function/color map for 'cParticleVelocity'
        cParticleVelocityLUT_1 = GetColorTransferFunction('cParticleVelocity')
        cParticleVelocityLUT_1.RGBPoints = [0.0, 0.278431, 0.278431, 0.858824, 11.44, 0.0, 0.0, 0.360784, 22.8, 0.0, 1.0, 1.0, 34.32, 0.0, 0.501961, 0.0, 45.68, 1.0, 1.0, 0.0, 57.12, 1.0, 0.380392, 0.0, 68.56, 0.419608, 0.0, 0.0, 80.0, 0.878431, 0.301961, 0.301961]
        cParticleVelocityLUT_1.LockScalarRange = 1
        cParticleVelocityLUT_1.ColorSpace = 'RGB'
        cParticleVelocityLUT_1.NanColor = [1.0, 1.0, 0.0]
        cParticleVelocityLUT_1.ScalarRangeInitialized = 1.0
        
        # get opacity transfer function/opacity map for 'cParticleVelocity'
        cParticleVelocityPWF_1 = GetOpacityTransferFunction('cParticleVelocity')
        cParticleVelocityPWF_1.Points = [0.0, 0.0, 0.5, 0.0, 80.0, 1.0, 0.5, 0.0]
        cParticleVelocityPWF_1.ScalarRangeInitialized = 1
        
        # get color transfer function/color map for 'Pressure'
        pressureLUT = GetColorTransferFunction('Pressure')
        pressureLUT.RGBPoints = [70000.0, 0.705882, 0.0156863, 0.14902, 185000.0, 0.865003, 0.865003, 0.865003, 300000.0, 0.231373, 0.298039, 0.752941]
        pressureLUT.LockScalarRange = 1
        pressureLUT.NanColor = [0.247059, 0.0, 0.0]
        pressureLUT.ScalarRangeInitialized = 1.0
        
        # get opacity transfer function/opacity map for 'Pressure'
        pressurePWF = GetOpacityTransferFunction('Pressure')
        pressurePWF.Points = [70000.0, 0.0, 0.5, 0.0, 300000.0, 1.0, 0.5, 0.0]
        pressurePWF.ScalarRangeInitialized = 1
        
        # ----------------------------------------------------------------
        # setup the visualization in view 'renderView1'
        # ----------------------------------------------------------------
        
        # show data from gradientOfUnstructuredDataSet1
        gradientOfUnstructuredDataSet1Display = Show(gradientOfUnstructuredDataSet1, renderView1)
        # trace defaults for the display properties.
        gradientOfUnstructuredDataSet1Display.ColorArrayName = ['CELLS', 'gradRho']
        gradientOfUnstructuredDataSet1Display.LookupTable = gradRhoLUT
        
        # show data from slice2
        slice2Display = Show(slice2, renderView1)
        # trace defaults for the display properties.
        slice2Display.ColorArrayName = ['CELLS', 'Pressure']
        slice2Display.LookupTable = pressureLUT
        
        # show color legend
        slice2Display.SetScalarBarVisibility(renderView1, True)
        
        # show data from glyph1
        glyph1Display = Show(glyph1, renderView1)
        # trace defaults for the display properties.
        glyph1Display.ColorArrayName = ['POINTS', 'cParticle Velocity']
        glyph1Display.LookupTable = cParticleVelocityLUT
        
        # show color legend
        glyph1Display.SetScalarBarVisibility(renderView1, True)
        
        # setup the color legend parameters for each legend in this view
        
        # get color legend/bar for cParticleVelocityLUT in view renderView1
        cParticleVelocityLUTColorBar = GetScalarBar(cParticleVelocityLUT, renderView1)
        cParticleVelocityLUTColorBar.Position = [0.111200967850896, 0.610778827124928]
        cParticleVelocityLUTColorBar.Position2 = [0.235316593040378, 0.12]
        cParticleVelocityLUTColorBar.Orientation = 'Horizontal'
        cParticleVelocityLUTColorBar.Title = 'Particle Velocity'
        cParticleVelocityLUTColorBar.ComponentTitle = '(m/s)'
        cParticleVelocityLUTColorBar.TitleBold = 1
        cParticleVelocityLUTColorBar.LabelFontSize = 10
        cParticleVelocityLUTColorBar.AutomaticLabelFormat = 0
        cParticleVelocityLUTColorBar.LabelFormat = '%4.0f'
        cParticleVelocityLUTColorBar.NumberOfLabels = 3
        cParticleVelocityLUTColorBar.DrawSubTickMarks = 0
        cParticleVelocityLUTColorBar.RangeLabelFormat = '%4.0f'
        
        # get color legend/bar for pressureLUT in view renderView1
        pressureLUTColorBar = GetScalarBar(pressureLUT, renderView1)
        pressureLUTColorBar.Position = [0.534843447260327, 0.206937799043062]
        pressureLUTColorBar.Position2 = [0.230124002170038, 0.12]
        pressureLUTColorBar.Orientation = 'Horizontal'
        pressureLUTColorBar.Title = 'Pressure (Pa)'
        pressureLUTColorBar.ComponentTitle = ''
        pressureLUTColorBar.TitleBold = 1
        pressureLUTColorBar.LabelFontSize = 16
        pressureLUTColorBar.AutomaticLabelFormat = 0
        pressureLUTColorBar.LabelFormat = '%4.0E'
        pressureLUTColorBar.NumberOfLabels = 3
        pressureLUTColorBar.DrawSubTickMarks = 0
        pressureLUTColorBar.RangeLabelFormat = '%4.0E'
        
        # ----------------------------------------------------------------
        # setup the visualization in view 'renderView2'
        # ----------------------------------------------------------------
        
        # show data from glyph1
        glyph1Display_1 = Show(glyph1, renderView2)
        # trace defaults for the display properties.
        glyph1Display_1.ColorArrayName = ['POINTS', 'cParticle Velocity']
        glyph1Display_1.LookupTable = cParticleVelocityLUT_1
        
        # show data from gradientOfUnstructuredDataSet1
        gradientOfUnstructuredDataSet1Display_1 = Show(gradientOfUnstructuredDataSet1, renderView2)
        # trace defaults for the display properties.
        gradientOfUnstructuredDataSet1Display_1.ColorArrayName = ['CELLS', 'gradRho']
        gradientOfUnstructuredDataSet1Display_1.LookupTable = gradRhoLUT
        
        # ----------------------------------------------------------------
        # setup the visualization in view 'renderView3'
        # ----------------------------------------------------------------
        
        # show data from glyph1
        glyph1Display_2 = Show(glyph1, renderView3)
        # trace defaults for the display properties.
        glyph1Display_2.ColorArrayName = ['POINTS', 'cParticle Velocity']
        glyph1Display_2.LookupTable = cParticleVelocityLUT_1
        
        # show data from slice3
        slice3Display = Show(slice3, renderView3)
        # trace defaults for the display properties.
        slice3Display.ColorArrayName = ['CELLS', 'Pressure']
        slice3Display.LookupTable = pressureLUT

	SaveScreenshot(fileLocWrite, magnification=1, quality=100, layout=aLayout)
        
        Delete(shktb_000000E00pvtu)
        del shktb_000000E00pvtu

        # Create a new 'Render View'
#        renderView1 = CreateView('RenderView')
#        renderView1.ViewSize = [1600, 383]
#        renderView1.OrientationAxesVisibility = 0
#        renderView1.CenterOfRotation = [0.139141411118526, 0.00248620830684373, 0.00499999988824129]
#        renderView1.StereoType = 0
        renderView1.CameraPosition = [0.0799080965819302, 0.0540748649202405, 0.0636053958967809]
        renderView1.CameraFocalPoint = [0.154440872954601, -0.00556274772717295, -0.00650778746958239]
        renderView1.CameraViewUp = [0.28207746045249693, 0.8577599622706518, -0.42974428842059087]
        renderView1.CameraParallelScale = 0.175142795897187
        renderView1.Background = [0.32, 0.34, 0.43]
        
#        aLayout = GetLayout()
#        aLayout.SplitVertical(0, 0.5)

        # Create a new 'Render View'
#        renderView2 = CreateView('RenderView')
#        renderView2.ViewSize = [1600, 197]
#        renderView2.InteractionMode = '2D'
#        renderView2.OrientationAxesVisibility = 0
#        renderView2.CenterOfRotation = [0.174999997019768, 0.00499999988824129, 9.99999974737875e-06]
#        renderView2.StereoType = 0
        renderView2.CameraPosition = [0.174999997019768, 0.00499999988824129, 0.676433989388009]
        renderView2.CameraFocalPoint = [0.174999997019768, 0.00499999988824129, 9.99999974737875e-06]
        renderView2.CameraParallelScale = 0.00829180933043838
        renderView2.Background = [0.32, 0.34, 0.43]
        
#        aLayout = GetLayout()
#        aLayout.SplitVertical(2, 0.5)

        # Create a new 'Render View'
#        renderView3 = CreateView('RenderView')
#        renderView3.ViewSize = [1600, 197]
#        renderView3.InteractionMode = '2D'
#        renderView3.OrientationAxesVisibility = 0
#        renderView3.CenterOfRotation = [0.174999997019768, 0.00989999994635582, 0.00499999988824129]
#        renderView3.StereoType = 0
        renderView3.CameraPosition = [0.174999997019768, -0.666523989441906, 0.00499999988824129]
        renderView3.CameraFocalPoint = [0.174999997019768, 0.00989999994635582, 0.00499999988824129]
        renderView3.CameraViewUp = [0.0, 0.0, 1.0]
        renderView3.CameraParallelScale = 0.00829180933043838
        renderView3.Background = [0.32, 0.34, 0.43]
 
        Disconnect()
        Connect()

f.close()
