import maya.cmds as maya
import random
import sys
#query the target range
windowID='scatterWindow'
global maxinteger
maxinteger=sys.maxint
global mininteger
mininteger=-sys.maxint


def selection(*arg):
    selectScatteredObj = maya.textScrollList(scatterObjBox, q=True, si=True)
    # print selectObj
    if selectScatteredObj == None:
        selectObjSrc = []
    maya.select(selectScatteredObj)
    # maya.select(selectObjSrc)




def AddObject(*arg):
	selectobj=maya.ls(sl=True)
	exisingobj=maya.textScrollList(scatterObjBox,q=True,ai=True)
	if exisingobj == None:
		exisingobj=[]
	newobj=list(set(selectobj)-set(exisingobj))
	maya.textScrollList(scatterObjBox,e=True,a=newobj)

def RemoveObject(*arg):
	selectobj=maya.textScrollList(scatterObjBox,q=True,si=True)
	print selectobj
	if selectobj!=None:
		maya.textScrollList(scatterObjBox,e=True,ri=selectobj)

def AddRange(*arg):
    selectobj = maya.ls(sl=True)
    exisingobj = maya.textScrollList(rangeObjBox, q=True, ai=True)
    if exisingobj == None:
        exisingobj = []
    # find unique object in the list
    newobj = list(set(selectobj)-set(exisingobj))
    maya.textScrollList(rangeObjBox, e=True, a=newobj)
    #if no objects selected-select the object
    if not maya.textScrollList(rangeObjBox,q=True,si=True):
    	maya.textScrollList(rangeObjBox,e=True,si=newobj)


def RemoveRange(*arg):
	selectobj = maya.textScrollList(rangeObjBox, q=True, si=True)
	if selectobj != None:
		maya.textScrollList(rangeObjBox,e=True,ri=selectobj)

def rangecalculation(*arg):
	bbox=[maxinteger,maxinteger,maxinteger,mininteger,mininteger,mininteger]
	rangeobj=maya.textScrollList(rangeObjBox,q=True,si=True)
	for obj in rangeobj:
		objbbox=maya.xform(obj,bb=True,q=True)
		bbox=combinebbox(objbbox,bbox)
	return bbox

def combinebbox(bbox1,bbox2):
	bbox=[]
	bbox.append(min(bbox1[0],bbox2[0]))
	bbox.append(min(bbox1[1],bbox2[1]))
	bbox.append(min(bbox1[2],bbox2[2]))
	bbox.append(max(bbox1[3],bbox2[3]))
	bbox.append(max(bbox1[4],bbox2[4]))
	bbox.append(max(bbox1[5],bbox2[5]))
	return bbox

def scatter(*arg):
	rangeobj=maya.textScrollList(rangeObjBox,q=True,ai=True)
	if rangeobj==None:
		maya.warning('Please Define Scatter Range First')
		return
	bbox=rangecalculation()
	xmin=bbox[0]
	ymin=bbox[1]
	zmin=bbox[2]
	xmax=bbox[3]
	ymax=bbox[4]
	zmax=bbox[5]
	#grp_scatter=maya.group(n='scatter_transform',em=True)
	#print grp_scatter
	if maya.checkBox(dupcheckBox,q=True,value=True):
		grp_scatter=maya.group(n='scatter_transform',em=True)
		number=maya.intField(dupnumber,q=True,v=True)
		selectobj=maya.textScrollList(scatterObjBox,q=True,ai=True)
		for obj in selectobj:
			for i in range(number):
				dupobj=maya.duplicate(obj)
				maya.parent(dupobj,grp_scatter)
				xRandom=random.uniform(xmin,xmax)
				yRandom=random.uniform(ymin,ymax)
				zRandom=random.uniform(zmin,zmax)
				maya.move(xRandom,yRandom,zRandom,dupobj,a=True,ws=True)
	else:
		selectobj=maya.textScrollList(scatterObjBox,q=True,ai=True)
		for obj in selectobj:
			#maya.parent(obj,grp_scatter)
			xRandom=random.uniform(xmin,xmax)
			yRandom=random.uniform(ymin,ymax)
			zRandom=random.uniform(zmin,zmax)
			maya.move(xRandom,yRandom,zRandom,obj,a=True,ws=True)



def allowDuplicate(*arg):
	status=maya.checkBox(dupcheckBox,q=True,value=True)
	if not status:
		maya.intField(dupnumber,e=True,en=False)
	else:
		maya.intField(dupnumber,e=True,en=True)

def scatterPanel():	
	maya.window(windowID,widthHeight=(300,250),title='Scatter',s=True,rtf=True)
	layout=maya.columnLayout(w=300,h=250)
	maya.columnLayout(h=5)
	maya.setParent('..')
	#maya.separator(w=200)
	maya.text(l='Scatter Tool',al='center',w=300,h=10,fn='boldLabelFont')
	maya.columnLayout(h=10)
	maya.setParent('..')
	maya.columnLayout(cat=['left',25],rs=5)
	maya.text(l='Define Scatter Range:',al='left',fn='boldLabelFont')
	global rangeObjBox
	rangeObjBox=maya.textScrollList(w=250,h=40)
	maya.setParent('..')
	maya.columnLayout(h=5)
	maya.setParent('..')
	maya.rowLayout(nc=2,cat=[(1,'left',30),(2,'left',30)])
	maya.button(l='Add Range',w=105,h=25,c=AddRange)
	maya.button(l='Remove Range',w=105,h=25,c=RemoveRange)
	maya.setParent('..')
	maya.columnLayout(h=10)
	maya.setParent('..')
	maya.separator(w=300,st='in')
	maya.columnLayout(cat=['left',25],rs=10)
	maya.text(l='Define Scattered Object:',al='left',fn='boldLabelFont')
	global scatterObjBox
	scatterObjBox=maya.textScrollList(w=250,h=60,ams=True)
	maya.setParent('..')
	maya.columnLayout(h=5)
	maya.setParent('..')
	maya.rowLayout(nc=2,cat=[(1,'left',30),(2,'left',30)])
	maya.button(l='Add Object',w=105,h=25,c=AddObject)
	maya.button(l='Remove Object',w=105,h=25,c=RemoveObject)
	maya.setParent('..')

	maya.rowLayout(nc=3,cat=[(1,'left',30),(2,'left',60)])
	global dupcheckBox
	dupcheckBox=maya.checkBox(l='Duplicate',cc=allowDuplicate)
	maya.text(l='Numbers:')
	global dupnumber
	dupnumber=maya.intField(en=False,w=40)
	maya.setParent('..')
	maya.setParent('..')
	maya.columnLayout(cat=['left',100])
	maya.button(l='Scatter',w=100,h=25,c=scatter)
	maya.showWindow(windowID)
def scatterGUI():
	if (maya.window(windowID,ex=True)):
		maya.deleteUI(windowID, wnd=True)
	scatterPanel()
	
scatterGUI()	