# This script is good for 2D shktb
# Generated using PV trace
# Edited: Rahul Babu Koneru

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

#Render()
import time
f=open('/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_SM15MA/timeSteps-test.dat',"r")
#f=open('/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_MM15OP/timeSteps.dat',"r")
times = f.readlines()
#basedir = "/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_SM15MA"
#basedir = "/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_MM15OP"
basedir = "/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_SM15MA"
filename = "/shktb_"
ext = ".pvtu"
extPcls = ".pcls.pvtu"
#basedirWrite = "/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_SM15MA/PNG-test"
basedirWrite = "/home/local/UFAD/rahul.koneru/post_processing/bertrand/PNGS"
#basedirWrite = "/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_MM15OP/PNGS"
filenameWrite = "/SM15MA_"
#filenameWrite = "/MM15OP_"
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

        # create a new 'XML Partitioned Unstructured Grid Reader'
#        shktb_850000E04pvtu = XMLPartitionedUnstructuredGridReader(FileName=['/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_SM15MA/shktb_8.50000E-04.pvtu'])
        shktb_850000E04pvtu = XMLPartitionedUnstructuredGridReader(FileName=fileLoc)
        shktb_850000E04pvtu.CellArrayStatus = ['Gas Density', 'Momentum', 'Energy', 'Pressure', 'Temperature', 'Speed of Sound', 'dp3', 'dp4', 'Particle Density', 'Particle Velocity', 'Particle Temperature', 'Particle Mass Fraction', 'Particle Volume Fraction', 'Particle Reynolds Number']
        shktb_850000E04pvtu.PointArrayStatus = []
        
        # create a new 'XML Partitioned Unstructured Grid Reader'
        partsPcls = [basedir, filename, timeStamp, extPcls]
        fileLocPcls = ''.join(partsPcls)
        print fileLocPcls,
        #shktb_850000E04pclspvtu = XMLPartitionedUnstructuredGridReader(FileName=['/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_SM15MA/shktb_8.50000E-04.pcls.pvtu'])
        shktb_850000E04pclspvtu = XMLPartitionedUnstructuredGridReader(FileName=fileLocPcls)
        shktb_850000E04pclspvtu.CellArrayStatus = []
        shktb_850000E04pclspvtu.PointArrayStatus = ['cParticle Velocity', 'cParticle Diameter']
        
        # set active source
        SetActiveSource(shktb_850000E04pvtu)
        
        # get active view
        renderView1 = GetActiveViewOrCreate('RenderView')
        renderView1.OrientationAxesVisibility = 0
        # uncomment following to set a specific view size
        renderView1.ViewSize = [1551, 858]
        
        # show data in view
        shktb_850000E04pclspvtuDisplay = Show(shktb_850000E04pclspvtu, renderView1)
        # trace defaults for the display properties.
        shktb_850000E04pclspvtuDisplay.CubeAxesVisibility = 0
        shktb_850000E04pclspvtuDisplay.Representation = 'Surface'
        shktb_850000E04pclspvtuDisplay.AmbientColor = [1.0, 1.0, 1.0]
        shktb_850000E04pclspvtuDisplay.ColorArrayName = [None, '']
        shktb_850000E04pclspvtuDisplay.DiffuseColor = [1.0, 1.0, 1.0]
        shktb_850000E04pclspvtuDisplay.LookupTable = None
        shktb_850000E04pclspvtuDisplay.MapScalars = 1
        shktb_850000E04pclspvtuDisplay.InterpolateScalarsBeforeMapping = 1
        shktb_850000E04pclspvtuDisplay.Opacity = 1.0
        shktb_850000E04pclspvtuDisplay.PointSize = 2.0
        shktb_850000E04pclspvtuDisplay.LineWidth = 1.0
        shktb_850000E04pclspvtuDisplay.Interpolation = 'Gouraud'
        shktb_850000E04pclspvtuDisplay.Specular = 0.0
        shktb_850000E04pclspvtuDisplay.SpecularColor = [1.0, 1.0, 1.0]
        shktb_850000E04pclspvtuDisplay.SpecularPower = 100.0
        shktb_850000E04pclspvtuDisplay.Ambient = 0.0
        shktb_850000E04pclspvtuDisplay.Diffuse = 1.0
        shktb_850000E04pclspvtuDisplay.EdgeColor = [0.0, 0.0, 0.5]
        shktb_850000E04pclspvtuDisplay.BackfaceRepresentation = 'Follow Frontface'
        shktb_850000E04pclspvtuDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
        shktb_850000E04pclspvtuDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
        shktb_850000E04pclspvtuDisplay.BackfaceOpacity = 1.0
        shktb_850000E04pclspvtuDisplay.Position = [0.0, 0.0, 0.0]
        shktb_850000E04pclspvtuDisplay.Scale = [1.0, 1.0, 1.0]
        shktb_850000E04pclspvtuDisplay.Orientation = [0.0, 0.0, 0.0]
        shktb_850000E04pclspvtuDisplay.Origin = [0.0, 0.0, 0.0]
        shktb_850000E04pclspvtuDisplay.Pickable = 1
        shktb_850000E04pclspvtuDisplay.Texture = None
        shktb_850000E04pclspvtuDisplay.Triangulate = 0
        shktb_850000E04pclspvtuDisplay.NonlinearSubdivisionLevel = 1
        shktb_850000E04pclspvtuDisplay.GlyphType = 'Arrow'
        shktb_850000E04pclspvtuDisplay.CubeAxesColor = [1.0, 1.0, 1.0]
        shktb_850000E04pclspvtuDisplay.CubeAxesCornerOffset = 0.0
        shktb_850000E04pclspvtuDisplay.CubeAxesFlyMode = 'Closest Triad'
        shktb_850000E04pclspvtuDisplay.CubeAxesInertia = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesTickLocation = 'Inside'
        shktb_850000E04pclspvtuDisplay.CubeAxesXAxisMinorTickVisibility = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesXAxisTickVisibility = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesXAxisVisibility = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesXGridLines = 0
        shktb_850000E04pclspvtuDisplay.CubeAxesXTitle = 'X-Axis'
        shktb_850000E04pclspvtuDisplay.CubeAxesUseDefaultXTitle = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesYAxisMinorTickVisibility = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesYAxisTickVisibility = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesYAxisVisibility = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesYGridLines = 0
        shktb_850000E04pclspvtuDisplay.CubeAxesYTitle = 'Y-Axis'
        shktb_850000E04pclspvtuDisplay.CubeAxesUseDefaultYTitle = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesZAxisMinorTickVisibility = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesZAxisTickVisibility = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesZAxisVisibility = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesZGridLines = 0
        shktb_850000E04pclspvtuDisplay.CubeAxesZTitle = 'Z-Axis'
        shktb_850000E04pclspvtuDisplay.CubeAxesUseDefaultZTitle = 1
        shktb_850000E04pclspvtuDisplay.CubeAxesGridLineLocation = 'All Faces'
        shktb_850000E04pclspvtuDisplay.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
        shktb_850000E04pclspvtuDisplay.CustomBoundsActive = [0, 0, 0]
        shktb_850000E04pclspvtuDisplay.OriginalBoundsRangeActive = [0, 0, 0]
        shktb_850000E04pclspvtuDisplay.CustomRange = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
        shktb_850000E04pclspvtuDisplay.CustomRangeActive = [0, 0, 0]
        shktb_850000E04pclspvtuDisplay.UseAxesOrigin = 0
        shktb_850000E04pclspvtuDisplay.AxesOrigin = [0.0, 0.0, 0.0]
        shktb_850000E04pclspvtuDisplay.CubeAxesXLabelFormat = '%-#6.3g'
        shktb_850000E04pclspvtuDisplay.CubeAxesYLabelFormat = '%-#6.3g'
        shktb_850000E04pclspvtuDisplay.CubeAxesZLabelFormat = '%-#6.3g'
        shktb_850000E04pclspvtuDisplay.StickyAxes = 0
        shktb_850000E04pclspvtuDisplay.CenterStickyAxes = 0
        shktb_850000E04pclspvtuDisplay.SelectionCellLabelBold = 0
        shktb_850000E04pclspvtuDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
        shktb_850000E04pclspvtuDisplay.SelectionCellLabelFontFamily = 'Arial'
        shktb_850000E04pclspvtuDisplay.SelectionCellLabelFontSize = 18
        shktb_850000E04pclspvtuDisplay.SelectionCellLabelItalic = 0
        shktb_850000E04pclspvtuDisplay.SelectionCellLabelJustification = 'Left'
        shktb_850000E04pclspvtuDisplay.SelectionCellLabelOpacity = 1.0
        shktb_850000E04pclspvtuDisplay.SelectionCellLabelShadow = 0
        shktb_850000E04pclspvtuDisplay.SelectionPointLabelBold = 0
        shktb_850000E04pclspvtuDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
        shktb_850000E04pclspvtuDisplay.SelectionPointLabelFontFamily = 'Arial'
        shktb_850000E04pclspvtuDisplay.SelectionPointLabelFontSize = 18
        shktb_850000E04pclspvtuDisplay.SelectionPointLabelItalic = 0
        shktb_850000E04pclspvtuDisplay.SelectionPointLabelJustification = 'Left'
        shktb_850000E04pclspvtuDisplay.SelectionPointLabelOpacity = 1.0
        shktb_850000E04pclspvtuDisplay.SelectionPointLabelShadow = 0
        shktb_850000E04pclspvtuDisplay.ScalarOpacityUnitDistance = 0.0026555508600791984
        shktb_850000E04pclspvtuDisplay.SelectMapper = 'Projected tetra'
        
        # init the 'Arrow' selected for 'GlyphType'
        shktb_850000E04pclspvtuDisplay.GlyphType.TipResolution = 6
        shktb_850000E04pclspvtuDisplay.GlyphType.TipRadius = 0.1
        shktb_850000E04pclspvtuDisplay.GlyphType.TipLength = 0.35
        shktb_850000E04pclspvtuDisplay.GlyphType.ShaftResolution = 6
        shktb_850000E04pclspvtuDisplay.GlyphType.ShaftRadius = 0.03
        shktb_850000E04pclspvtuDisplay.GlyphType.Invert = 0
        
        # reset view to fit data
        renderView1.ResetCamera()
        
        # Properties modified on shktb_850000E04pvtu
        shktb_850000E04pvtu.CellArrayStatus = ['Gas Density']
        
        # show data in view
        shktb_850000E04pvtuDisplay = Show(shktb_850000E04pvtu, renderView1)
        # trace defaults for the display properties.
        shktb_850000E04pvtuDisplay.CubeAxesVisibility = 0
        shktb_850000E04pvtuDisplay.Representation = 'Surface'
        shktb_850000E04pvtuDisplay.AmbientColor = [1.0, 1.0, 1.0]
        shktb_850000E04pvtuDisplay.ColorArrayName = [None, '']
        shktb_850000E04pvtuDisplay.DiffuseColor = [1.0, 1.0, 1.0]
        shktb_850000E04pvtuDisplay.LookupTable = None
        shktb_850000E04pvtuDisplay.MapScalars = 1
        shktb_850000E04pvtuDisplay.InterpolateScalarsBeforeMapping = 1
        shktb_850000E04pvtuDisplay.Opacity = 1.0
        shktb_850000E04pvtuDisplay.PointSize = 2.0
        shktb_850000E04pvtuDisplay.LineWidth = 1.0
        shktb_850000E04pvtuDisplay.Interpolation = 'Gouraud'
        shktb_850000E04pvtuDisplay.Specular = 0.0
        shktb_850000E04pvtuDisplay.SpecularColor = [1.0, 1.0, 1.0]
        shktb_850000E04pvtuDisplay.SpecularPower = 100.0
        shktb_850000E04pvtuDisplay.Ambient = 0.0
        shktb_850000E04pvtuDisplay.Diffuse = 1.0
        shktb_850000E04pvtuDisplay.EdgeColor = [0.0, 0.0, 0.5]
        shktb_850000E04pvtuDisplay.BackfaceRepresentation = 'Follow Frontface'
        shktb_850000E04pvtuDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
        shktb_850000E04pvtuDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
        shktb_850000E04pvtuDisplay.BackfaceOpacity = 1.0
        shktb_850000E04pvtuDisplay.Position = [0.0, 0.0, 0.0]
        shktb_850000E04pvtuDisplay.Scale = [1.0, 1.0, 1.0]
        shktb_850000E04pvtuDisplay.Orientation = [0.0, 0.0, 0.0]
        shktb_850000E04pvtuDisplay.Origin = [0.0, 0.0, 0.0]
        shktb_850000E04pvtuDisplay.Pickable = 1
        shktb_850000E04pvtuDisplay.Texture = None
        shktb_850000E04pvtuDisplay.Triangulate = 0
        shktb_850000E04pvtuDisplay.NonlinearSubdivisionLevel = 1
        shktb_850000E04pvtuDisplay.GlyphType = 'Arrow'
        shktb_850000E04pvtuDisplay.CubeAxesColor = [1.0, 1.0, 1.0]
        shktb_850000E04pvtuDisplay.CubeAxesCornerOffset = 0.0
        shktb_850000E04pvtuDisplay.CubeAxesFlyMode = 'Closest Triad'
        shktb_850000E04pvtuDisplay.CubeAxesInertia = 1
        shktb_850000E04pvtuDisplay.CubeAxesTickLocation = 'Inside'
        shktb_850000E04pvtuDisplay.CubeAxesXAxisMinorTickVisibility = 1
        shktb_850000E04pvtuDisplay.CubeAxesXAxisTickVisibility = 1
        shktb_850000E04pvtuDisplay.CubeAxesXAxisVisibility = 1
        shktb_850000E04pvtuDisplay.CubeAxesXGridLines = 0
        shktb_850000E04pvtuDisplay.CubeAxesXTitle = 'X-Axis'
        shktb_850000E04pvtuDisplay.CubeAxesUseDefaultXTitle = 1
        shktb_850000E04pvtuDisplay.CubeAxesYAxisMinorTickVisibility = 1
        shktb_850000E04pvtuDisplay.CubeAxesYAxisTickVisibility = 1
        shktb_850000E04pvtuDisplay.CubeAxesYAxisVisibility = 1
        shktb_850000E04pvtuDisplay.CubeAxesYGridLines = 0
        shktb_850000E04pvtuDisplay.CubeAxesYTitle = 'Y-Axis'
        shktb_850000E04pvtuDisplay.CubeAxesUseDefaultYTitle = 1
        shktb_850000E04pvtuDisplay.CubeAxesZAxisMinorTickVisibility = 1
        shktb_850000E04pvtuDisplay.CubeAxesZAxisTickVisibility = 1
        shktb_850000E04pvtuDisplay.CubeAxesZAxisVisibility = 1
        shktb_850000E04pvtuDisplay.CubeAxesZGridLines = 0
        shktb_850000E04pvtuDisplay.CubeAxesZTitle = 'Z-Axis'
        shktb_850000E04pvtuDisplay.CubeAxesUseDefaultZTitle = 1
        shktb_850000E04pvtuDisplay.CubeAxesGridLineLocation = 'All Faces'
        shktb_850000E04pvtuDisplay.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
        shktb_850000E04pvtuDisplay.CustomBoundsActive = [0, 0, 0]
        shktb_850000E04pvtuDisplay.OriginalBoundsRangeActive = [0, 0, 0]
        shktb_850000E04pvtuDisplay.CustomRange = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
        shktb_850000E04pvtuDisplay.CustomRangeActive = [0, 0, 0]
        shktb_850000E04pvtuDisplay.UseAxesOrigin = 0
        shktb_850000E04pvtuDisplay.AxesOrigin = [0.0, 0.0, 0.0]
        shktb_850000E04pvtuDisplay.CubeAxesXLabelFormat = '%-#6.3g'
        shktb_850000E04pvtuDisplay.CubeAxesYLabelFormat = '%-#6.3g'
        shktb_850000E04pvtuDisplay.CubeAxesZLabelFormat = '%-#6.3g'
        shktb_850000E04pvtuDisplay.StickyAxes = 0
        shktb_850000E04pvtuDisplay.CenterStickyAxes = 0
        shktb_850000E04pvtuDisplay.SelectionCellLabelBold = 0
        shktb_850000E04pvtuDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
        shktb_850000E04pvtuDisplay.SelectionCellLabelFontFamily = 'Arial'
        shktb_850000E04pvtuDisplay.SelectionCellLabelFontSize = 18
        shktb_850000E04pvtuDisplay.SelectionCellLabelItalic = 0
        shktb_850000E04pvtuDisplay.SelectionCellLabelJustification = 'Left'
        shktb_850000E04pvtuDisplay.SelectionCellLabelOpacity = 1.0
        shktb_850000E04pvtuDisplay.SelectionCellLabelShadow = 0
        shktb_850000E04pvtuDisplay.SelectionPointLabelBold = 0
        shktb_850000E04pvtuDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
        shktb_850000E04pvtuDisplay.SelectionPointLabelFontFamily = 'Arial'
        shktb_850000E04pvtuDisplay.SelectionPointLabelFontSize = 18
        shktb_850000E04pvtuDisplay.SelectionPointLabelItalic = 0
        shktb_850000E04pvtuDisplay.SelectionPointLabelJustification = 'Left'
        shktb_850000E04pvtuDisplay.SelectionPointLabelOpacity = 1.0
        shktb_850000E04pvtuDisplay.SelectionPointLabelShadow = 0
        shktb_850000E04pvtuDisplay.ScalarOpacityUnitDistance = 0.0036541236638406374
        shktb_850000E04pvtuDisplay.SelectMapper = 'Projected tetra'
        
        # init the 'Arrow' selected for 'GlyphType'
        shktb_850000E04pvtuDisplay.GlyphType.TipResolution = 6
        shktb_850000E04pvtuDisplay.GlyphType.TipRadius = 0.1
        shktb_850000E04pvtuDisplay.GlyphType.TipLength = 0.35
        shktb_850000E04pvtuDisplay.GlyphType.ShaftResolution = 6
        shktb_850000E04pvtuDisplay.GlyphType.ShaftRadius = 0.03
        shktb_850000E04pvtuDisplay.GlyphType.Invert = 0
        
        # set scalar coloring
        ColorBy(shktb_850000E04pvtuDisplay, ('CELLS', 'Gas Density'))
        
        # rescale color and/or opacity maps used to include current data range
        shktb_850000E04pvtuDisplay.RescaleTransferFunctionToDataRange(True)
        
        # show color bar/color legend
        shktb_850000E04pvtuDisplay.SetScalarBarVisibility(renderView1, True)
        
        # get color transfer function/color map for 'GasDensity'
        gasDensityLUT = GetColorTransferFunction('GasDensity')
        gasDensityLUT.LockDataRange = 0
        gasDensityLUT.InterpretValuesAsCategories = 0
        gasDensityLUT.ShowCategoricalColorsinDataRangeOnly = 0
        gasDensityLUT.RescaleOnVisibilityChange = 0
        gasDensityLUT.EnableOpacityMapping = 0
        gasDensityLUT.RGBPoints = [1.1236108624747745, 0.231373, 0.298039, 0.752941, 2.864689932173462, 0.865003, 0.865003, 0.865003, 4.605769001872149, 0.705882, 0.0156863, 0.14902]
        gasDensityLUT.UseLogScale = 0
        gasDensityLUT.ColorSpace = 'Diverging'
        gasDensityLUT.UseBelowRangeColor = 0
        gasDensityLUT.BelowRangeColor = [0.0, 0.0, 0.0]
        gasDensityLUT.UseAboveRangeColor = 0
        gasDensityLUT.AboveRangeColor = [1.0, 1.0, 1.0]
        gasDensityLUT.NanColor = [1.0, 1.0, 0.0]
        gasDensityLUT.Discretize = 1
        gasDensityLUT.NumberOfTableValues = 256
        gasDensityLUT.ScalarRangeInitialized = 1.0
        gasDensityLUT.HSVWrap = 0
        gasDensityLUT.VectorComponent = 0
        gasDensityLUT.VectorMode = 'Magnitude'
        gasDensityLUT.AllowDuplicateScalars = 1
        gasDensityLUT.Annotations = []
        gasDensityLUT.ActiveAnnotatedValues = []
        gasDensityLUT.IndexedColors = []
        
        # Color bar
        gasDensityLUTColorBar = GetScalarBar(gasDensityLUT, renderView1)
        gasDensityLUTColorBar.Position = [0.4, 0.65]
        gasDensityLUTColorBar.Position2 = [0.1, 0.3]
        gasDensityLUTColorBar.AutoOrient = 1
        gasDensityLUTColorBar.Orientation = 'Horizontal'
        gasDensityLUTColorBar.Title = 'Gas Density'
        gasDensityLUTColorBar.ComponentTitle = ''
        gasDensityLUTColorBar.TitleJustification = 'Centered'
        gasDensityLUTColorBar.TitleColor = [1.0, 1.0, 1.0]
        gasDensityLUTColorBar.TitleOpacity = 1.0
        gasDensityLUTColorBar.TitleFontFamily = 'Arial'
        gasDensityLUTColorBar.TitleBold = 0
        gasDensityLUTColorBar.TitleItalic = 0
        gasDensityLUTColorBar.TitleShadow = 0
        gasDensityLUTColorBar.TitleFontSize = 7
        gasDensityLUTColorBar.LabelColor = [1.0, 1.0, 1.0]
        gasDensityLUTColorBar.LabelOpacity = 1.0
        gasDensityLUTColorBar.LabelFontFamily = 'Arial'
        gasDensityLUTColorBar.LabelBold = 0
        gasDensityLUTColorBar.LabelItalic = 0
        gasDensityLUTColorBar.LabelShadow = 0
        gasDensityLUTColorBar.LabelFontSize = 7
        gasDensityLUTColorBar.AutomaticLabelFormat = 1
        gasDensityLUTColorBar.LabelFormat = '%-#6.3g'
        gasDensityLUTColorBar.NumberOfLabels = 5
        gasDensityLUTColorBar.DrawTickMarks = 1
        gasDensityLUTColorBar.DrawSubTickMarks = 1
        gasDensityLUTColorBar.DrawTickLabels = 1
        gasDensityLUTColorBar.AddRangeLabels = 1
        gasDensityLUTColorBar.RangeLabelFormat = '%4.3e'
        gasDensityLUTColorBar.DrawAnnotations = 1
        gasDensityLUTColorBar.AddRangeAnnotations = 0
        gasDensityLUTColorBar.AutomaticAnnotations = 0
        gasDensityLUTColorBar.DrawNanAnnotation = 0
        gasDensityLUTColorBar.NanAnnotation = 'NaN'
        gasDensityLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
        #gasDensityLUTColorBar.AspectRatio = 25.0
        
        # Properties modified on gasDensityLUTColorBar
        gasDensityLUTColorBar.ComponentTitle = '$(kg/m^3)$'
        gasDensityLUTColorBar.RangeLabelFormat = '%4.2f'
        
        # get opacity transfer function/opacity map for 'GasDensity'
        gasDensityPWF = GetOpacityTransferFunction('GasDensity')
        gasDensityPWF.Points = [1.1236108624747745, 0.0, 0.5, 0.0, 4.605769001872149, 1.0, 0.5, 0.0]
        gasDensityPWF.AllowDuplicateScalars = 1
        gasDensityPWF.ScalarRangeInitialized = 1
        
        # Rescale transfer function
        gasDensityLUT.RescaleTransferFunction(0.8, 4.5)
        
        # Rescale transfer function
        gasDensityPWF.RescaleTransferFunction(0.8, 4.5)
        # set active source
        SetActiveSource(shktb_850000E04pclspvtu)
        
        # create a new 'Glyph'
        glyph1 = Glyph(Input=shktb_850000E04pclspvtu,
            GlyphType='Arrow')
        glyph1.Scalars = ['POINTS', 'None']
        glyph1.Vectors = ['POINTS', 'None']
        glyph1.Orient = 1
        glyph1.ScaleMode = 'off'
        glyph1.ScaleFactor = 0.021363320946693423
        glyph1.GlyphMode = 'Uniform Spatial Distribution'
        glyph1.MaximumNumberOfSamplePoints = 5000
        glyph1.Seed = 10339
        glyph1.Stride = 1
        glyph1.GlyphTransform = 'Transform2'
        
        # init the 'Arrow' selected for 'GlyphType'
        glyph1.GlyphType.TipResolution = 6
        glyph1.GlyphType.TipRadius = 0.1
        glyph1.GlyphType.TipLength = 0.35
        glyph1.GlyphType.ShaftResolution = 6
        glyph1.GlyphType.ShaftRadius = 0.03
        glyph1.GlyphType.Invert = 0
        
        # init the 'Transform2' selected for 'GlyphTransform'
        glyph1.GlyphTransform.Translate = [0.0, 0.0, 0.0]
        glyph1.GlyphTransform.Rotate = [0.0, 0.0, 0.0]
        glyph1.GlyphTransform.Scale = [1.0, 1.0, 1.0]
        
        # Properties modified on glyph1
        glyph1.GlyphType = 'Sphere'
        glyph1.Vectors = ['POINTS', 'cParticle Velocity']
        glyph1.ScaleFactor = 0.02
        glyph1.MaximumNumberOfSamplePoints = 10000
        
        # show data in view
        glyph1Display = Show(glyph1, renderView1)
        # trace defaults for the display properties.
        glyph1Display.CubeAxesVisibility = 0
        glyph1Display.Representation = 'Surface'
        glyph1Display.AmbientColor = [1.0, 1.0, 1.0]
        glyph1Display.ColorArrayName = [None, '']
        glyph1Display.DiffuseColor = [1.0, 1.0, 1.0]
        glyph1Display.LookupTable = None
        glyph1Display.MapScalars = 1
        glyph1Display.InterpolateScalarsBeforeMapping = 1
        glyph1Display.Opacity = 1.0
        glyph1Display.PointSize = 2.0
        glyph1Display.LineWidth = 1.0
        glyph1Display.Interpolation = 'Gouraud'
        glyph1Display.Specular = 0.0
        glyph1Display.SpecularColor = [1.0, 1.0, 1.0]
        glyph1Display.SpecularPower = 100.0
        glyph1Display.Ambient = 0.0
        glyph1Display.Diffuse = 1.0
        glyph1Display.EdgeColor = [0.0, 0.0, 0.5]
        glyph1Display.BackfaceRepresentation = 'Follow Frontface'
        glyph1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
        glyph1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
        glyph1Display.BackfaceOpacity = 1.0
        glyph1Display.Position = [0.0, 0.0, 0.0]
        glyph1Display.Scale = [1.0, 1.0, 1.0]
        glyph1Display.Orientation = [0.0, 0.0, 0.0]
        glyph1Display.Origin = [0.0, 0.0, 0.0]
        glyph1Display.Pickable = 1
        glyph1Display.Texture = None
        glyph1Display.Triangulate = 0
        glyph1Display.NonlinearSubdivisionLevel = 1
        glyph1Display.GlyphType = 'Arrow'
        glyph1Display.CubeAxesColor = [1.0, 1.0, 1.0]
        glyph1Display.CubeAxesCornerOffset = 0.0
        glyph1Display.CubeAxesFlyMode = 'Closest Triad'
        glyph1Display.CubeAxesInertia = 1
        glyph1Display.CubeAxesTickLocation = 'Inside'
        glyph1Display.CubeAxesXAxisMinorTickVisibility = 1
        glyph1Display.CubeAxesXAxisTickVisibility = 1
        glyph1Display.CubeAxesXAxisVisibility = 1
        glyph1Display.CubeAxesXGridLines = 0
        glyph1Display.CubeAxesXTitle = 'X-Axis'
        glyph1Display.CubeAxesUseDefaultXTitle = 1
        glyph1Display.CubeAxesYAxisMinorTickVisibility = 1
        glyph1Display.CubeAxesYAxisTickVisibility = 1
        glyph1Display.CubeAxesYAxisVisibility = 1
        glyph1Display.CubeAxesYGridLines = 0
        glyph1Display.CubeAxesYTitle = 'Y-Axis'
        glyph1Display.CubeAxesUseDefaultYTitle = 1
        glyph1Display.CubeAxesZAxisMinorTickVisibility = 1
        glyph1Display.CubeAxesZAxisTickVisibility = 1
        glyph1Display.CubeAxesZAxisVisibility = 1
        glyph1Display.CubeAxesZGridLines = 0
        glyph1Display.CubeAxesZTitle = 'Z-Axis'
        glyph1Display.CubeAxesUseDefaultZTitle = 1
        glyph1Display.CubeAxesGridLineLocation = 'All Faces'
        glyph1Display.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
        glyph1Display.CustomBoundsActive = [0, 0, 0]
        glyph1Display.OriginalBoundsRangeActive = [0, 0, 0]
        glyph1Display.CustomRange = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
        glyph1Display.CustomRangeActive = [0, 0, 0]
        glyph1Display.UseAxesOrigin = 0
        glyph1Display.AxesOrigin = [0.0, 0.0, 0.0]
        glyph1Display.CubeAxesXLabelFormat = '%-#6.3g'
        glyph1Display.CubeAxesYLabelFormat = '%-#6.3g'
        glyph1Display.CubeAxesZLabelFormat = '%-#6.3g'
        glyph1Display.StickyAxes = 0
        glyph1Display.CenterStickyAxes = 0
        glyph1Display.SelectionCellLabelBold = 0
        glyph1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
        glyph1Display.SelectionCellLabelFontFamily = 'Arial'
        glyph1Display.SelectionCellLabelFontSize = 18
        glyph1Display.SelectionCellLabelItalic = 0
        glyph1Display.SelectionCellLabelJustification = 'Left'
        glyph1Display.SelectionCellLabelOpacity = 1.0
        glyph1Display.SelectionCellLabelShadow = 0
        glyph1Display.SelectionPointLabelBold = 0
        glyph1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
        glyph1Display.SelectionPointLabelFontFamily = 'Arial'
        glyph1Display.SelectionPointLabelFontSize = 18
        glyph1Display.SelectionPointLabelItalic = 0
        glyph1Display.SelectionPointLabelJustification = 'Left'
        glyph1Display.SelectionPointLabelOpacity = 1.0
        glyph1Display.SelectionPointLabelShadow = 0
        
        # init the 'Arrow' selected for 'GlyphType'
        glyph1Display.GlyphType.TipResolution = 6
        glyph1Display.GlyphType.TipRadius = 0.1
        glyph1Display.GlyphType.TipLength = 0.35
        glyph1Display.GlyphType.ShaftResolution = 6
        glyph1Display.GlyphType.ShaftRadius = 0.03
        glyph1Display.GlyphType.Invert = 0
        
        # Properties modified on glyph1
        glyph1.ScaleFactor = 0.002
        
        # Properties modified on glyph1
        glyph1.ScaleFactor = 0.0015
        glyph1.MaximumNumberOfSamplePoints = 100000
        
        # Properties modified on glyph1
        glyph1.MaximumNumberOfSamplePoints = 60000
        
        # hide data in view
        Hide(shktb_850000E04pclspvtu, renderView1)
        
        # set scalar coloring
        ColorBy(glyph1Display, ('POINTS', 'cParticle Velocity'))
        
        # rescale color and/or opacity maps used to include current data range
        glyph1Display.RescaleTransferFunctionToDataRange(True)
        
        # show color bar/color legend
        glyph1Display.SetScalarBarVisibility(renderView1, True)
        
        # get color transfer function/color map for 'cParticleVelocity'
        cParticleVelocityLUT = GetColorTransferFunction('cParticleVelocity')
        cParticleVelocityLUT.LockDataRange = 0
        cParticleVelocityLUT.InterpretValuesAsCategories = 0
        cParticleVelocityLUT.ShowCategoricalColorsinDataRangeOnly = 0
        cParticleVelocityLUT.RescaleOnVisibilityChange = 0
        cParticleVelocityLUT.EnableOpacityMapping = 0
        cParticleVelocityLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 78.48157347452862, 0.865003, 0.865003, 0.865003, 156.96314694905723, 0.705882, 0.0156863, 0.14902]
        cParticleVelocityLUT.UseLogScale = 0
        cParticleVelocityLUT.ColorSpace = 'Diverging'
        cParticleVelocityLUT.UseBelowRangeColor = 0
        cParticleVelocityLUT.BelowRangeColor = [0.0, 0.0, 0.0]
        cParticleVelocityLUT.UseAboveRangeColor = 0
        cParticleVelocityLUT.AboveRangeColor = [1.0, 1.0, 1.0]
        cParticleVelocityLUT.NanColor = [1.0, 1.0, 0.0]
        cParticleVelocityLUT.Discretize = 1
        cParticleVelocityLUT.NumberOfTableValues = 256
        cParticleVelocityLUT.ScalarRangeInitialized = 1.0
        cParticleVelocityLUT.HSVWrap = 0
        cParticleVelocityLUT.VectorComponent = 0
        cParticleVelocityLUT.VectorMode = 'Magnitude'
        cParticleVelocityLUT.AllowDuplicateScalars = 1
        cParticleVelocityLUT.Annotations = []
        cParticleVelocityLUT.ActiveAnnotatedValues = []
        cParticleVelocityLUT.IndexedColors = []
        
        # get opacity transfer function/opacity map for 'cParticleVelocity'
        cParticleVelocityPWF = GetOpacityTransferFunction('cParticleVelocity')
        cParticleVelocityPWF.Points = [0.0, 0.0, 0.5, 0.0, 156.96314694905723, 1.0, 0.5, 0.0]
        cParticleVelocityPWF.AllowDuplicateScalars = 1
        cParticleVelocityPWF.ScalarRangeInitialized = 1
        
        # Rescale transfer function
        cParticleVelocityLUT.RescaleTransferFunction(0.0, 150.0)
        
        # Rescale transfer function
        cParticleVelocityPWF.RescaleTransferFunction(0.0, 150.0)
        
        # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
        cParticleVelocityLUT.ApplyPreset('erdc_iceFire_L', True)
        
        # get color legend/bar for cParticleVelocityLUT in view renderView1
        cParticleVelocityLUTColorBar = GetScalarBar(cParticleVelocityLUT, renderView1)
        cParticleVelocityLUTColorBar.Position = [0.4, 0.1]
        cParticleVelocityLUTColorBar.Position2 = [0.1, 0.3]
        cParticleVelocityLUTColorBar.AutoOrient = 1
        cParticleVelocityLUTColorBar.Orientation = 'Horizontal'
        cParticleVelocityLUTColorBar.Title = 'cParticle Velocity'
        cParticleVelocityLUTColorBar.ComponentTitle = 'Magnitude'
        cParticleVelocityLUTColorBar.TitleJustification = 'Centered'
        cParticleVelocityLUTColorBar.TitleColor = [1.0, 1.0, 1.0]
        cParticleVelocityLUTColorBar.TitleOpacity = 1.0
        cParticleVelocityLUTColorBar.TitleFontFamily = 'Arial'
        cParticleVelocityLUTColorBar.TitleBold = 0
        cParticleVelocityLUTColorBar.TitleItalic = 0
        cParticleVelocityLUTColorBar.TitleShadow = 0
        cParticleVelocityLUTColorBar.TitleFontSize = 7
        cParticleVelocityLUTColorBar.LabelColor = [1.0, 1.0, 1.0]
        cParticleVelocityLUTColorBar.LabelOpacity = 1.0
        cParticleVelocityLUTColorBar.LabelFontFamily = 'Arial'
        cParticleVelocityLUTColorBar.LabelBold = 0
        cParticleVelocityLUTColorBar.LabelItalic = 0
        cParticleVelocityLUTColorBar.LabelShadow = 0
        cParticleVelocityLUTColorBar.LabelFontSize = 7
        cParticleVelocityLUTColorBar.AutomaticLabelFormat = 1
        cParticleVelocityLUTColorBar.LabelFormat = '%-#6.3g'
        cParticleVelocityLUTColorBar.NumberOfLabels = 5
        cParticleVelocityLUTColorBar.DrawTickMarks = 1
        cParticleVelocityLUTColorBar.DrawSubTickMarks = 1
        cParticleVelocityLUTColorBar.DrawTickLabels = 1
        cParticleVelocityLUTColorBar.AddRangeLabels = 1
        cParticleVelocityLUTColorBar.RangeLabelFormat = '%4.3e'
        cParticleVelocityLUTColorBar.DrawAnnotations = 1
        cParticleVelocityLUTColorBar.AddRangeAnnotations = 0
        cParticleVelocityLUTColorBar.AutomaticAnnotations = 0
        cParticleVelocityLUTColorBar.DrawNanAnnotation = 0
        cParticleVelocityLUTColorBar.NanAnnotation = 'NaN'
        cParticleVelocityLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
        #cParticleVelocityLUTColorBar.AspectRatio = 25.0
        
        # Properties modified on cParticleVelocityLUTColorBar
        cParticleVelocityLUTColorBar.Title = 'Particle Velocity'
        cParticleVelocityLUTColorBar.ComponentTitle = 'Magnitude $(m/s)$'
        cParticleVelocityLUTColorBar.RangeLabelFormat = '%4.0f'
        
        
        # set active source
        SetActiveSource(shktb_850000E04pvtu)
        
        # Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
        gasDensityLUT.ApplyPreset('Cool to Warm (Extended)', True)
        
        # current camera placement for renderView1
        renderView1.CameraPosition = [0.17504430159021875, 0.01959540907286294, 0.36733830844019966]
        renderView1.CameraFocalPoint = [0.17504430159021875, 0.01959540907286294, -0.05299105846375752]
        renderView1.CameraParallelScale = 0.10878924537062937

        # save screenshot
        #SaveScreenshot('/home/local/UFAD/rahul.koneru/post_processing/bertrand/VTU_SM15MA/PNG-test/SM15MA_800.png', magnification=1, quality=100, view=renderView1)
        time.sleep(14)        
	partsWrite = [basedirWrite, filenameWrite, timePNG, extWrite]
	fileLocWrite = ''.join(partsWrite)

	SaveScreenshot(fileLocWrite, magnification=1, quality=100, view=renderView1)

        # set active source
        SetActiveSource(glyph1)
        
        # set active source
        SetActiveSource(shktb_850000E04pclspvtu)
        
        # hide data in view
        Hide(glyph1, renderView1)
        
        # show data in view
        shktb_850000E04pclspvtuDisplay = Show(shktb_850000E04pclspvtu, renderView1)
        
        # destroy glyph1
        Delete(glyph1)
        del glyph1
        
        # destroy shktb_850000E04pclspvtu
        Delete(shktb_850000E04pclspvtu)
        del shktb_850000E04pclspvtu
        
        # set active source
        SetActiveSource(shktb_850000E04pvtu)
        
        # destroy shktb_850000E04pvtu
        Delete(shktb_850000E04pvtu)
        del shktb_850000E04pvtu
        
        #### saving camera placements for all active views
        
        # current camera placement for renderView1

        renderView1.CameraPosition = [0.17504430159021875, 0.01959540907286294, 0.36733830844019966]
        renderView1.CameraFocalPoint = [0.17504430159021875, 0.01959540907286294, -0.05299105846375752]
        renderView1.CameraParallelScale = 0.10878924537062937
        
        Disconnect()
        Connect()
#ResetCamera()
#### uncomment the following to render all views
#RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
f.close()
