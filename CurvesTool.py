import maya.cmds as mc


def createDimond():
    mc.curve(n='Dimond_01', d=1, p=[(-2.5, 0, 0), (0, 0, -5), (2.5, 0, 0), (0, 0, 5), (-2.5, 0, 0), ])


def createPlus():
    mc.curve(n='Plus_01', d=1,
             p=[(-2.5, 0, -2.5), (-2.5, 0, -7.5), (2.5, 0, -7.5), (2.5, 0, -2.5), (7.5, 0, -2.5), (7.5, 0, 2.5),
                (2.5, 0, 2.5,), (2.5, 0, 7.5), (-2.5, 0, 7.5), (-2.5, 0, 2.5), (-7.5, 0, 2.5,), (-7.5, 0, -2.5),
                (-2.5, 0, -2.5), ])


def createArrow():
    mc.curve(n='Arrow_01', d=1,
             p=[(-7.5, 0, -2.5), (0, 0, -10), (7.5, 0, -2.5), (2.5, 0, -2.5), (2.5, 0, 10), (-2.5, 0, 10),
                (-2.5, 0, -2.5), (-7.5, 0, -2.5), ])


def createDoubleArrow():
    mc.curve(n='DoubleArrow_01', d=1,
             p=[(0, 0, -2.5), (-10, 0, -2.5), (-7.5, 0, -7.5), (-17.5, 0, 0), (-7.5, 0, 7.5), (-10, 0, 2.5),
                (0, 0, 2.5,), (10, 0, 2.5), (7.5, 0, 7.5), (17.5, 0, 0), (7.5, 0, -7.5), (10, 0, -2.5), (0, 0, -2.5), ])


def createBox():
    mc.curve(n='Box_01', d=1,
             p=[(-5, 0, -5), (5, 0, -5), (5, 0, 5), (-5, 0, 5), (-5, 0, -5), (-5, 7.5, -5), (5, 7.5, -5), (5, 0, -5),
                (5, 0, 5), (5, 7.5, 5), (5, 7.5, -5), (5, 7.5, -5), (-5, 7.5, -5), (-5, 7.5, 5), (5, 7.5, 5),
                (-5, 7.5, 5), (-5, 0, 5), ])


def create3Dimond():
    mc.curve(n='d_Dimond_01', d=1,
             p=[(-2.5, 2.5, 0), (0, 5, 0), (2.5, 2.5, 0), (2.5, -2.5, 0), (0, -5, 0), (-2.5, -2.5, 0), (-2.5, 2.5, 0),
                (-2.5, 2.5, -2.5), (0, 5, -2.5), (2.5, 2.5, -2.5), (2.5, -2.5, -2.5), (0, -5, -2.5), (-2.5, -2.5, -2.5),
                (-2.5, -2.5, 0), (-2.5, -2.5, -2.5), (-2.5, 2.5, -2.5), (0, 5, -2.5), (0, 5, 0), (2.5, 2.5, 0),
                (2.5, 2.5, -2.5), (2.5, -2.5, -2.5), (2.5, -2.5, 0), (0, -5, 0), (0, -5, -2.5), ])


def createQuadArrow():
    mc.curve(n='qArrow_01', d=1,
             p=[(-2.5, 0, -2.5), (-2.5, 0, -7.5), (-5, 0, -7.5), (0, 0, -12.5), (5, 0, -7.5), (2.5, 0, -7.5),
                (2.5, 0, -2.5), (7.5, 0, -2.5), (7.5, 0, -5), (12.5, 0, 0), (7.5, 0, 5), (7.5, 0, 2.5), (2.5, 0, 2.5),
                (2.5, 0, 7.5), (5, 0, 7.5), (0, 0, 12.5), (-5, 0, 7.5), (-2.5, 0, 7.5), (-2.5, 0, 2.5), (-7.5, 0, 2.5),
                (-7.5, 0, 5), (-12.5, 0, 0), (-7.5, 0, -5), (-7.5, 0, -2.5), (-2.5, 0, -2.5), ])


def createSharpDiamond():
    aDiamond = mc.curve(n='aDiamond_01', d=1, p=[(-2.5, 0, 0,), (0, 7.5, 0), (2.5, 0, 0), (0, -7.5, 0), (-2.5, 0, 0), ])
    bDiamond = mc.curve(n='bDiamond_01', d=1,
                        p=[(0, 0, 2.5), (0, 7.5, 0), (0, 0, -2.5), (0, -7.5, 0), (0, 0, 2.5), (0, 7.5, 0), (0, 0, -2.5),
                           (0, -7.5, 0), (0, 0, 2.5), (0, 7.5, 0), ])
    cDiamond = mc.curve(n='cDiamond_01', d=1, p=[(0, 0, -2.5), (-2.5, 0, 0), (0, 0, 2.5), (2.5, 0, 0), (0, 0, -2.5), ])
    mc.attachCurve(aDiamond, bDiamond, cDiamond, rpo=False)
    mc.delete(aDiamond, bDiamond, cDiamond)


def changeCurveColor(newColor):
    sel = mc.ls(sl=True)
    for myCurve in sel:
        shape = mc.listRelatives(myCurve, s=True)
        shape = shape[0]
        mc.setAttr(shape + '.overrideEnabled', 1)
        if newColor == 'blue':
            mc.setAttr(shape + '.overrideColor', 6)
        if newColor == 'red':
            mc.setAttr(shape + '.overrideColor', 13)
        if newColor == 'green':
            mc.setAttr(shape + '.overrideColor', 14)


def createWindow(wind):
    if mc.window(wind, exists=True):
        mc.deleteUI(wind)
    mc.window(wind)
    mc.columnLayout()
    mc.button(label='Dimond', c='createDimond()')
    mc.button(label='Plus', c='createPlus()')
    mc.button(label='Arrow', c='createArrow()')
    mc.button(label='DoubleArrow', c='createDoubleArrow()')
    mc.button(label='Box', c='createBox()')
    mc.button(label='3Dimond', c='create3Dimond()')
    mc.button(label='QuadArrow', c='createQuadArrow()')
    mc.button(label='SharpDiamond', c='createSharpDiamond()')
    mc.text(label='ChangeControlColor')
    mc.button(label='Blue', bgc=(0, 0, 1), c='changeCurveColor("blue")')
    mc.button(label='Red', bgc=(1, 0, 0), c='changeCurveColor("red")')
    mc.button(label='Green', bgc=(0, 1, 0), c='changeCurveColor("green")')
    mc.showWindow(wind)


createWindow('RigCurves')
