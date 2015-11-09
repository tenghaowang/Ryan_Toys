import maya.cmds as maya

def cc_import(*arg):
	filepath=maya.fileDialog(m=0,t='Import')
	print filepath
	filenumbers=maya.intField(filenumberGUI,q=True,v=True)
	print filenumbers
	nameSpace=maya.textField(nameSpaceGUI,q=True,tx=True)
	print nameSpace
	if(filepath!=None):
		for i in range(filenumbers):
			maya.file(filepath,i=True,ns=nameSpace)

def importpanel():	
	maya.window(windowID,widthHeight=(300,100),title='Batch Import',s=True)
	maya.columnLayout(w=300,h=100,rs=5)
	maya.rowColumnLayout(nc=2,cw=[(1,200),(2,50)])
	maya.text(l='Specify the number of files:')
	global filenumberGUI
	filenumberGUI=maya.intField()
	maya.setParent('..')
	maya.rowColumnLayout(nc=2,cw=[(1,150),(2,100)],cat=[(1,'left',50),(2,'right',20)])
	maya.text(l='nameSpace:')
	global nameSpaceGUI
	nameSpaceGUI=maya.textField()
	maya.setParent('..')
	maya.columnLayout(cat=['left',90])
	maya.button(l='Import',w=120,h=30,c=cc_import)
	maya.setParent('..')
	maya.showWindow(windowID)

def importGUI():
	if (maya.window(windowID,ex=True)):
		maya.deleteUI(windowID, wnd=True)
	importpanel()
	
importGUI()	
		