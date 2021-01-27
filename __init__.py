import svgwrite
import math
import pickle
import linecache
import os
import string as st

sysPath=os.path.dirname(os.path.abspath(__file__)[:-11])
__all__=['colour','draw','setFont','font_width']

printChar=st.printable[:-5]

width=0.3
intersection_spot_side=4
pin_spot_radius=2

font_size_pt=12 #pt
font_size=round(font_size_pt*4.0/3.0,4) #px
font_weight="bold"
font_family="Tahoma"
flag_font_size=10 #pt
pin_font_size_pt=6 #pt
pin_font_size=round(pin_font_size_pt*4.0/3.0,4) #px
pin_font_weight="normal"
pin_font_family="Arial"

symbColor_="#000000"
symbTextColor_="#42f5aa"
symbAttrColor_="#f59e42"
symbPinColor_="#8742f5"
symbFillColor_="#fff9eb"
flagColor_="#77fc03"
gndColor_="#fc0352"
comColor_="#03bafc"
wireColor_="#524e63"
intsecColor_="#0000ff"
textColor_="#eb3464"
busTapColor_="#ec03fc"

fontFamilies=["Arial","Bahnschrift","Calibri","Cambria","Candara","Comic Sans MS","Consolas","Constantia","Corbel","Courier New","Ebrima","Franklin Gothic Medium","Gabriola","Gadugi","Impact","Ink Free","Javanese Text","Leelawadee UI","Lucida Console","Malgun Gothic","Microsoft Himalaya","Mongolian Baiti","MS Gothic","MV Boli","Myanmar Text","Nirmala UI","Segoe Print","SimSun","Sitka Text","Sylfaen","Tahoma","Times New Roman","Trebuchet MS"]
fontString=""
for fontF in fontFamilies:
    fontString+=(fontF+" or ")
fontString=fontString[:-4]

def setPen(lineWidth=0.3,ISside=4,PPradius=2):
    global width,intersection_spot_side,pin_spot_radius
    if type(lineWidth)!=float and type(lineWidth)!=int:
        raise(TypeError("Line width thickness must be a float or integer from 0 to 5 except 0. [Units: pt]"))
    if lineWidth<=0 or lineWidth>5:
        raise(ValueError("Line width thickness must be a float or integer from 0 to 5 except 0. [Units: pt]"))
    if type(ISside)!=float and type(ISside)!=int:
        raise(TypeError("Intersection spot square side must be a float or integer from 1 to 20. [Units: pt]"))
    if ISside<1 or ISside>20:
        raise(ValueError("Intersection spot square side must be a float or integer from 1 to 20. [Units: pt]"))
    if type(PPradius)!=float and type(PPradius)!=int:
        raise(TypeError("Pin point radius must be a float or integer from 1 to 20. [Units: pt]"))
    if PPradius<1 or PPradius>20:
        raise(ValueError("Pin point radius must be a float or integer from 1 to 20. [Units: pt]"))
    width=lineWidth
    intersection_spot_side=ISside
    pin_spot_radius=PPradius
    
def setFont(fontSize=12,fontWeight="bold",fontFamily="Tahoma",flagFontSize=10,pinFontSize=6,pinFontWeight="normal",pinFontFamily="Arial"):

    global font_size_pt, font_size, font_weight, font_family, flag_font_size, pin_font_size_pt
    global pin_font_size, pin_font_weight, pin_font_family
    if type(fontSize)!=int:
        raise(TypeError("Font size must be from 1 to 144 Integer only. [Units: pt]"))
    if fontSize<1 or fontSize>144:
        raise(ValueError("Font size must be from 1 to 144 Integer only. [Units: pt]"))
    if type(pinFontSize)!=int:
        raise(TypeError("Pin font size must be from 1 to 144 Integer only. [Units: pt]"))
    if pinFontSize<1 or pinFontSize>144:
        raise(ValueError("Pin font size must be from 1 to 144 Integer only. [Units: pt]"))
    if type(flagFontSize)!=int:
        raise(TypeError("Flag font size must be from 1 to 144 Integer only. [Units: pt]"))
    if flagFontSize<1 or flagFontSize>144:
        raise(ValueError("Flag font size must be from 1 to 144 Integer only. [Units: pt]"))
    if type(fontWeight)!=str:
        raise(TypeError("Font weight must be 'normal' or 'bold' only."))
    if fontWeight!='normal' and fontWeight!='bold':
        raise(ValueError("Font weight must be 'normal' or 'bold' only."))
    if type(pinFontWeight)!=str:
        raise(TypeError("Pin font weight must be 'normal' or 'bold' only."))
    if pinFontWeight!='normal' and pinFontWeight!='bold':
        raise(ValueError("Pin font weight must be 'normal' or 'bold' only."))
    if fontFamily not in fontFamilies:
        raise(ValueError("Font family must be either "+fontString+" only."))
    if pinFontFamily not in fontFamilies:
        raise(ValueError("Pin font family must be either "+fontString+" only."))
    font_size_pt=fontSize #pt
    font_size=round(font_size_pt*4.0/3.0,4) #px
    font_weight=fontWeight
    font_family=fontFamily
    flag_font_size=flagFontSize #pt
    pin_font_size_pt=pinFontSize #pt
    pin_font_size=round(pin_font_size_pt*4.0/3.0,4) #px
    pin_font_weight=pinFontWeight
    pin_font_family=pinFontFamily
        

def checkColor(color):
    validCA='abcdefABCDEF0123456789'
    if type(color)!=str:
        return(False)
    if color[0]!='#':
        return (False)
    else:
        if len(color[1:]) in [3,6]:
            for A in color[1:]:
                if A not in validCA:
                    return(False)
                else:
                    continue
            else:
                return(True)
        else:
            return(False)
            

def colour(isBW=False,symbColor="#000000",symbTextColor="#42f5aa",symbAttrColor="#f59e42",symbPinColor="#8742f5",symbFillColor="#fff9eb",flagColor="#77fc03",gndColor="#fc0352",comColor="#03bafc",wireColor="#524e63",intsecColor="#0000ff",textColor="#eb3464",busTapColor="#ec03fc"):
    global symbColor_,symbTextColor_,symbAttrColor_,symbPinColor_,symbFillColor_
    global flagColor_,gndColor_,comColor_,wireColor_,intsecColor_,textColor_,busTapColor_

    if type(isBW)!=bool:
        raise(ValueError("isBW (is Black and White) parameter must be either True and False. If isBW is set to True then other parameters have no effect."))

    colorNames=["symbColor","symbTextColor","symbAttrColor","symbPinColor","symbFillColor","flagColor","gndColor","comColor","wireColor","intsecColor","textColor","busTapColor"]
    colorValue=[symbColor,symbTextColor,symbAttrColor,symbPinColor,symbFillColor,flagColor,gndColor,comColor,wireColor,intsecColor,textColor,busTapColor]

    for i in range(len(colorValue)):
        color=colorValue[i]
        if checkColor(color):
            continue
        else:
            raise(ValueError("Inappropriate "+colorNames[i]+"."))
        
    if isBW:
        symbColor_="#000000"
        symbTextColor_="#000000"
        symbAttrColor_="#000000"
        symbPinColor_="#000000"
        symbFillColor_="#000000"
        flagColor_="#000000"
        gndColor_="#000000"
        comColor_="#000000"
        wireColor_="#000000"
        intsecColor_="#000000"
        textColor_="#000000"
        busTapColor_="#000000"
    else:
        symbColor_=symbColor
        symbTextColor_=symbTextColor
        symbAttrColor_=symbAttrColor
        symbPinColor_=symbPinColor
        symbFillColor_=symbFillColor
        flagColor_=flagColor
        gndColor_=gndColor
        comColor_=comColor
        wireColor_=wireColor
        intsecColor_=intsecColor
        textColor_=textColor
        busTapColor_=busTapColor
        
    

pIntsecLocations={} #probable intersection locations #Coordinate:count
pIntsecDirections={} #coordinate: [Left:1,Right:2,Top:3,Bottom:4]

AttributeIndices={'Prefix':0,'Value':3,'SpiceModel':38,'Value2':123,'SpiceLine':39,'SpiceLine2':40,'Type':1}
sizes=[4,6,10,12,16,22,30,44] #0.625,1,1.5,2,2.5,3.5,5,7 px

nGnCflags={} #Coordinate: text #non ground non common flags

class font_width:
    def __init__(self,family='',normal={},bold={}):
        self.family=family
        self.normal=normal
        self.bold=bold
    def getFamily(self):
        return(self.family)
    def getNormal(self):
        return(self.normal)
    def getBold(self):
        return(self.bold)

def _line(ix,iy,fx,fy,colour,dash='none'):
    #i=initial and f=final
    dwg.add(dwg.line((ix,iy), (fx,fy), stroke=colour,fill='none',stroke_width=width,stroke_dasharray='{dashes}'.format(dashes=dash)))

def _arc(cx1,cy1,cx2,cy2,ix,iy,fx,fy,colour,dash='none'):

    #example

    #ARC Normal 0 64 32 96 16 96 4 68
    #arc(0,64,32,96,16,96,4,68)
    
    #radii
    rx=abs(cx1-cx2)*0.5
    ry=abs(cy1-cy2)*0.5

    #center
    cx=(cx1+cx2)*0.5
    cy=(cy1+cy2)*0.5

    #relative coordinates
    ixr=ix-cx
    iyr=iy-cy
    fxr=fx-cx
    fyr=fy-cy
    
    if (ixr*fyr-fxr*iyr)>0:
        #when cross product of two 2D vectors is greater than zero, it means their angle in anticlockwise
        #sense is less than 180, but here y is in opposite direction thus when product is greater than zero angle
        #is greater than 180
        
        l=1
    else:
        l=0

    #rotation is zero
    #sense is anticlockwise from start to stop
        
    dwg.add(dwg.path(d='M{},{} A{},{} {} {},{} {},{}'.format(ix,iy,rx,ry,0,l,0,fx,fy),stroke=colour,fill='none',stroke_width=width,stroke_dasharray='{dashes}'.format(dashes=dash)))

def _rect(brx,bry,ulx,uly,colour,fillColour,dash='none'):
    if uly>bry:
        y=bry
    else:
        y=uly
    if brx<ulx:
        x=brx
    else:
        x=ulx
    #br=bottom right and ul=upper left
    dwg.add(dwg.rect((x,y), (abs(ulx-brx),abs(uly-bry)), stroke=colour, fill=fillColour,stroke_width=width,stroke_dasharray='{dashes}'.format(dashes=dash)))

def _squareSpot(x,y,colour):
    dwg.add(dwg.rect((x-intersection_spot_side/2,y-intersection_spot_side/2),(intersection_spot_side,intersection_spot_side),stroke='none',fill=colour))

def _circle(brx,bry,ulx,uly,colour,dash='none'):
    #br=bottom right and ul=upper left
    cx=(brx+ulx)*0.5
    cy=(bry+uly)*0.5
    rx=abs(brx-ulx)*0.5
    ry=abs(bry-uly)*0.5
    if (rx==ry):
        dwg.add(dwg.circle((cx,cy),rx,stroke=colour,fill='none',stroke_width=width,stroke_dasharray='{dashes}'.format(dashes=dash)))
    else:
        dwg.add(dwg.ellipse((cx,cy),(rx,ry),stroke=colour,fill='none',stroke_width=width,stroke_dasharray='{dashes}'.format(dashes=dash)))
def _spot(x,y,colour):
    dwg.add(dwg.circle((x,y),pin_spot_radius,stroke='none',fill=colour,stroke_width=width))
def _text(x,y,string,size,weight,family,rAngle,colour):
    dwg.add(dwg.text(string,(x,y),font_size='{size}px'.format(size=size),font_weight=weight,font_family=family,stroke='none',fill=colour,transform="rotate({rAngle} {xRotate} {yRotate})".format(rAngle=rAngle,xRotate=x,yRotate=y)))

def _container(new1,new2,current_Max,current_Min):
    maxC=max(new1,new2)
    minC=min(new1,new2)
    new_max_min=[current_Max,current_Min]
    if current_Max<maxC:
        new_max_min[0]=maxC
    if current_Min>minC:
        new_max_min[1]=minC
    return(new_max_min)

def _close(x):
    x1=int(x)
    x2=math.ceil(x)
    if (2*x)<(x2+x1):
        return(x1)
    else:
        return(x2)

def _tw_in_px(text,family,size,weight): #text width in pixel, size in px from 1 to 144, weight only normal or bold
    filer=open(sysPath+r'\Resource\widths\\'+str(size)+'.dat','rb')
    try:
        while True:
            z=font_width()
            z=pickle.load(filer)
            if z.getFamily()==family:
                break
    except EOFError:
        pass
    filer.close()
    if weight=='normal':
        widths=z.getNormal()
    else:
        widths=z.getBold()
    width=0
    for character in text:
        width+=(widths[character])
    return(width)#-len(text)*0.5)
class Coordinate: #Coordinates are in px
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def getX(self):
        return(self.x)
    def getY(self):
        return(self.y)
    def rotate(self,theta):
        x1=(self.x*math.cos(math.radians(theta)))-(self.y*math.sin(math.radians(theta)))
        y1=(self.y*math.cos(math.radians(theta)))+(self.x*math.sin(math.radians(theta)))
        return (Coordinate(x1,y1))
    def translate(self,origin):
        return(Coordinate(self.x-origin.getX(),self.y-origin.getY()))
    def mirror(self):
        return(Coordinate(-1*self.x,self.y))
    def __eq__(self,comparer):
        if self.x==comparer.getX() and self.y==comparer.getY():
            return (True)
        else:
            return (False)
    def __hash__(self):
        return(hash(str(self)))

class Window:
    def __init__(self,coordinate,alignment,sizeIndex):
        self.coordinate=coordinate
        self.alignment=alignment
        self.sizeIndex=sizeIndex
    def getCoordinate(self):
        return(self.coordinate)
    def getAlignment(self):
        return(self.alignment)
    def getSIndex(self):
        return(self.sizeIndex)

def _transform(coordinate,mirrorBool,rAngle,origin):
    coordinate=coordinate.rotate(rAngle)
    if mirrorBool:
        coordinate=coordinate.mirror()
    coordinate=coordinate.translate(origin)
    return(coordinate)

def _rotateAlign(alignment,rAngle):
    opposite={'Left':'Right','Right':'Left','Center':'Center','Top':'Bottom','Bottom':'Top'}
    if rAngle==90:
        if alignment[0]=='V':
            alignment=alignment[1:]
        else:
            alignment='V'+opposite[alignment]
    if rAngle==180:
        for i in range(2):
            alignment=_rotateAlign(alignment,90)
    if rAngle==270:
        for i in range(3):
            alignment=_rotateAlign(alignment,90)
    return(alignment)

def _mirrorAlign(alignment,isMirror):
    if isMirror:
        mirrors={'Left':'Right','Right':'Left','VTop':'VBottom','VBottom':'VTop'}
        try:
            alignment=mirrors[alignment]
        except KeyError:
            pass
    return(alignment)
        
        
def _leftBottomC(coordinate,textAlignment,textSize,tw):
    if textAlignment=='Left':
        #leftMidC=Coordinate
        leftBottom=Coordinate(coordinate.getX(),coordinate.getY()+textSize*0.5)
    elif textAlignment=='Right':
        #rightMidC=Coordinate
        leftBottom=Coordinate(coordinate.getX()-tw,coordinate.getY()+textSize*0.5)
    elif textAlignment=='Center':
        #midMidC=Coordinate
        leftBottom=Coordinate(coordinate.getX()-tw*0.5,coordinate.getY()+textSize*0.5)
    elif textAlignment=='Top':
        #midTopC=Coordinate
        leftBottom=Coordinate(coordinate.getX()-tw*0.5,coordinate.getY()+textSize)
    elif textAlignment=='Bottom':
        #midBottomC=Coordinate
        leftBottom=Coordinate(coordinate.getX()-tw*0.5,coordinate.getY())
    elif textAlignment=='VRight':
        #topMidC=Coordinate
        leftBottom=Coordinate(coordinate.getX()+textSize*0.5,coordinate.getY()+tw)
    elif textAlignment=='VLeft':
        #bottomMidC=Coordinate
        leftBottom=Coordinate(coordinate.getX()+textSize*0.5,coordinate.getY())
    elif textAlignment=='VCenter':
        #midMidC=Coordinate
        leftBottom=Coordinate(coordinate.getX()+textSize*0.5,coordinate.getY()+tw*0.5)
    elif textAlignment=='VTop':
        #leftMidC=Coordinate
        leftBottom=Coordinate(coordinate.getX()+textSize,coordinate.getY()+tw*0.5)
    elif textAlignment=='VBottom':
        #rightMidC=Coordinate
        leftBottom=Coordinate(coordinate.getX(),coordinate.getY()+tw*0.5)
    return(leftBottom)

def _pinOffsetC(pinLoc,offset,alignment):
    if alignment=='Left' or alignment=='VTop':
        pinLoc=pinLoc.translate(Coordinate(-1*offset,0))
    elif alignment=='Right' or alignment=='VBottom':
        pinLoc=pinLoc.translate(Coordinate(offset,0))
    elif alignment=='Top' or alignment=='VRight':
        pinLoc=pinLoc.translate(Coordinate(0,-1*offset))
    elif alignment=='Bottom' or alignment=='VLeft':
        pinLoc=pinLoc.translate(Coordinate(0,offset))
    return(pinLoc)

def _busTap(x,y,TipX,TipY,colour):
    global width
    if x==TipX:
        dx=4
        dy=0
        #up down
    elif y==TipY:
        dx=0
        dy=4
        #left right
    width*=4
    _line(x-dx,y-dy,x+dx,y+dy,colour)
    width/=4
    _line(x-dx,y-dy,TipX,TipY,colour)
    _line(x+dx,y+dy,TipX,TipY,colour)

def _flag(x,y,string,flagColour,rAngle=0):
    #text(x,y,string,size,weight,family,rAngle,colour)
    #0=text
    _text(x,y,string,flag_font_size*4.0/3.0,font_weight,font_family,rAngle,flagColour)

def _gnd(x,y,gndColour,rAngle=0):
    #0=__
    #  \/
    if rAngle==0:
        #baseline
        _line(x-8,y,x+8,y,gndColour)
        _line(x-8,y,x,y+8,gndColour)
        _line(x+8,y,x,y+8,gndColour)
    elif rAngle==180:
        _line(x-8,y,x+8,y,gndColour)
        _line(x-8,y,x,y-8,gndColour)
        _line(x+8,y,x,y-8,gndColour)
    elif rAngle==90:
        _line(x,y-8,x,y+8,gndColour)
        _line(x,y-8,x-8,y,gndColour)
        _line(x,y+8,x-8,y,gndColour)
    elif rAngle==270:
        _line(x,y-8,x,y+8,gndColour)
        _line(x,y-8,x+8,y,gndColour)
        _line(x,y+8,x+8,y,gndColour)
    #_spot(x,y,symbPinColor_)

def _com(x,y,comColour,rAngle=90):
    #0=
    #  \/
    if rAngle==0:
        _line(x,y,x+8,y-8,comColour)
        _line(x,y,x-8,y-8,comColour)
    elif rAngle==180:
        _line(x,y,x+8,y+8,comColour)
        _line(x,y,x-8,y+8,comColour)
    elif rAngle==90:
        _line(x,y,x+8,y+8,comColour)
        _line(x,y,x+8,y-8,comColour)
    elif rAngle==270:
        _line(x,y,x-8,y+8,comColour)
        _line(x,y,x-8,y-8,comColour)
    #_spot(x,y,symbPinColor_)

def _HeadlineText(leftBottom,tw,fontSize,alignment,colour):
    global width
    width*=3
    if alignment[0]!='V':
        xStart=leftBottom.getX()
        xEnd=xStart+tw
        y=leftBottom.getY()-fontSize-2
        _line(xStart,y,xEnd,y,colour)
    else:
        yStart=leftBottom.getY()
        yEnd=yStart-tw
        x=leftBottom.getX()-fontSize-2
        _line(x,yStart,x,yEnd,colour)
    width/=3

def _DirFlag(Point,ContainerMax,ContainerMin,directionIndex,flagColour):
    #Left:1,Right:2,Top:3,Bottom:4,.LeftRight:5,LeftRight.:6,.TopBottom:7,TopBottom.:8
    if directionIndex==1:
        #/----
        #\----
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMin.getY()-2,flagColour)
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMax.getY()+2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMax.getX()+2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
    elif directionIndex==2:
        _line(Point.getX(),Point.getY(),ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
        _line(Point.getX(),Point.getY(),ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMax.getY()+2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
    elif directionIndex==3:
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMin.getY()-2,flagColour)
        _line(Point.getX(),Point.getY(),ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMax.getX()+2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMax.getY()+2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
    elif directionIndex==4:
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(Point.getX(),Point.getY(),ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMax.getX()+2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
    elif directionIndex==5:
        #./----\
        # \----/
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMin.getY()-2,flagColour)
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMax.getY()+2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        PointM=Coordinate(ContainerMax.getX()+ContainerMin.getX()-Point.getX(),Point.getY())
        _line(PointM.getX(),PointM.getY(),ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        _line(PointM.getX(),PointM.getY(),ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
    elif directionIndex==6:
        #/----\.
        #\----/
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMin.getY()-2,flagColour)
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMax.getY()+2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        PointM=Coordinate(ContainerMin.getX()-ContainerMin.getX()+Point.getX(),Point.getY())
        _line(PointM.getX(),PointM.getY(),ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(PointM.getX(),PointM.getY(),ContainerMin.getX()-2,ContainerMin.getY()-2,flagColour)
    elif directionIndex==7:
        #.
        #/\
        #||
        #||
        #\/
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMin.getY()-2,flagColour)
        _line(Point.getX(),Point.getY(),ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMax.getX()+2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        PointM=Coordinate(Point.getX(),ContainerMax.getY()+ContainerMin.getY()-Point.getY())
        _line(PointM.getX(),PointM.getY(),ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(PointM.getX(),PointM.getY(),ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
    elif directionIndex==8:
        #/\
        #||
        #||
        #\/
        #.
        _line(Point.getX(),Point.getY(),ContainerMin.getX()-2,ContainerMin.getY()-2,flagColour)
        _line(Point.getX(),Point.getY(),ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
        _line(ContainerMin.getX()-2,ContainerMin.getY()-2,ContainerMin.getX()-2,ContainerMax.getY()+2,flagColour)
        _line(ContainerMax.getX()+2,ContainerMin.getY()-2,ContainerMax.getX()+2,ContainerMax.getY()+2,flagColour)
        PointM=Coordinate(Point.getX(),ContainerMin.getY()-ContainerMax.getY()+Point.getY())
        _line(PointM.getX(),PointM.getY(),ContainerMin.getX()-2,ContainerMin.getY()-2,flagColour)
        _line(PointM.getX(),PointM.getY(),ContainerMax.getX()+2,ContainerMin.getY()-2,flagColour)
        

    
def _symb(symbC,symbTheta,isMirror,windows,windowValues,filepath):
    lines=[]
    global pIntsecLocations
    #windows={} #attribute_index:Window
    #WINDOW 0 0 56 VBottom 2
    #WINDOW 3 32 56 VTop 2
    #windowValues={} #attribute_index:value
    #filepath=r'C:\\Users\\harsh\\Desktop\\LTspiceToSVG\\sym\\res.txt'
    filer=open(filepath,'r')
    try:
        while True:
            x=filer.readline()
            if x!="":
                if x[-1]=='\n':
                    z=x[:-1].split(' ')
                else:
                    z=x.split(' ')
                if z[0]=="RECTANGLE":
                    lines=[x]+lines
                else:
                    lines.append(x)
            else:
                break
    except EOFError:
        pass
    filer.close()
    extract=["LINE","RECTANGLE","CIRCLE","ARC","SYMATTR","TEXT","PIN","WINDOW","PINATTR"]
    index=0
    while index<len(lines):
        x=lines[index]
        if x[-1]=='\n':
            z=x[:-1].split(' ')
        else:
            z=x.split(' ')
        if z[0] in extract:
            if "LINE"==z[0]:
                startC=_transform(Coordinate(float(z[2]),float(z[3])),isMirror,symbTheta,symbC)
                endC=_transform(Coordinate(float(z[4]),float(z[5])),isMirror,symbTheta,symbC)
                try:
                    containerY=_container(startC.getY(),endC.getY(),containerYmax,containerYmin)
                    containerYmax=containerY[0]
                    containerYmin=containerY[1]
                except NameError:
                    containerYmax=max(startC.getY(),endC.getY())
                    containerYmin=min(startC.getY(),endC.getY())
                try:
                    containerX=_container(startC.getX(),endC.getX(),containerXmax,containerXmin)
                    containerXmax=containerX[0]
                    containerXmin=containerX[1]
                except NameError:
                    containerXmax=max(startC.getX(),endC.getX())
                    containerXmin=min(startC.getX(),endC.getX())
                try:
                    dash=z[6]
                except IndexError:
                    dash='none'
                _line(startC.getX(),startC.getY(),endC.getX(),endC.getY(),symbColor_,dash)
            elif "RECTANGLE"==z[0]:
                corner1C=_transform(Coordinate(float(z[2]),float(z[3])),isMirror,symbTheta,symbC)
                corner2C=_transform(Coordinate(float(z[4]),float(z[5])),isMirror,symbTheta,symbC)
                try:
                    containerY=_container(corner1C.getY(),corner2C.getY(),containerYmax,containerYmin)
                    containerYmax=containerY[0]
                    containerYmin=containerY[1]
                except NameError:
                    containerYmax=max(corner1C.getY(),corner2C.getY())
                    containerYmin=min(corner1C.getY(),corner2C.getY())
                try:
                    containerX=_container(corner1C.getX(),corner2C.getX(),containerXmax,containerXmin)
                    containerXmax=containerX[0]
                    containerXmin=containerX[1]
                except NameError:
                    containerXmax=max(corner1C.getX(),corner2C.getX())
                    containerXmin=min(corner1C.getX(),corner2C.getX())
                try:
                    dash=z[6]
                except IndexError:
                    dash='none'
                _rect(corner1C.getX(),corner1C.getY(),corner2C.getX(),corner2C.getY(),symbColor_,symbFillColor_,dash)
            elif "ARC"==z[0]:
                boxCorner1C=_transform(Coordinate(float(z[2]),float(z[3])),isMirror,symbTheta,symbC)
                boxCorner2C=_transform(Coordinate(float(z[4]),float(z[5])),isMirror,symbTheta,symbC)
                startC=_transform(Coordinate(float(z[6]),float(z[7])),isMirror,symbTheta,symbC)
                endC=_transform(Coordinate(float(z[8]),float(z[9])),isMirror,symbTheta,symbC)
                try:
                    containerY=_container(boxCorner1C.getY(),boxCorner2C.getY(),containerYmax,containerYmin)
                    containerYmax=containerY[0]
                    containerYmin=containerY[1]
                except NameError:
                    containerYmax=max(boxCorner1C.getY(),boxCorner2C.getY())
                    containerYmin=min(boxCorner1C.getY(),boxCorner2C.getY())
                try:
                    containerX=_container(boxCorner1C.getX(),boxCorner2C.getX(),containerXmax,containerXmin)
                    containerXmax=containerX[0]
                    containerXmin=containerX[1]
                except NameError:
                    containerXmax=max(boxCorner1C.getX(),boxCorner2C.getX())
                    containerXmin=min(boxCorner1C.getX(),boxCorner2C.getX())
                try:
                    dash=z[10]
                except IndexError:
                    dash='none'
                _arc(boxCorner1C.getX(),boxCorner1C.getY(),boxCorner2C.getX(),boxCorner2C.getY(),startC.getX(),startC.getY(),endC.getX(),endC.getY(),symbColor_,dash)
            elif "CIRCLE"==z[0]:
                boxCorner1C=_transform(Coordinate(float(z[2]),float(z[3])),isMirror,symbTheta,symbC)
                boxCorner2C=_transform(Coordinate(float(z[4]),float(z[5])),isMirror,symbTheta,symbC)
                try:
                    containerY=_container(boxCorner1C.getY(),boxCorner2C.getY(),containerYmax,containerYmin)
                    containerYmax=containerY[0]
                    containerYmin=containerY[1]
                except NameError:
                    containerYmax=max(boxCorner1C.getY(),boxCorner2C.getY())
                    containerYmin=min(boxCorner1C.getY(),boxCorner2C.getY())
                try:
                    containerX=_container(boxCorner1C.getX(),boxCorner2C.getX(),containerXmax,containerXmin)
                    containerXmax=containerX[0]
                    containerXmin=containerX[1]
                except NameError:
                    containerXmax=max(boxCorner1C.getX(),boxCorner2C.getX())
                    containerXmin=min(boxCorner1C.getX(),boxCorner2C.getX())
                try:
                    dash=z[6]
                except IndexError:
                    dash='none'
                _circle(boxCorner1C.getX(),boxCorner1C.getY(),boxCorner2C.getX(),boxCorner2C.getY(),symbColor_,dash)
            elif "TEXT"==z[0]:
                symbAttrC=_transform(Coordinate(float(z[1]),float(z[2])),isMirror,symbTheta,symbC)
                textSize=sizes[int(z[4])]
                textString=''
                i=5
                try:
                    while True:
                        textString+=(z[i]+' ')
                        i+=1
                except IndexError:
                    textString=textString[:-1]
                tw=_tw_in_px(textString,font_family,_close(textSize),font_weight)
                textAlignment=z[3]
                leftBottom=_leftBottomC(symbAttrC,textAlignment,textSize,tw)

                if textAlignment[0]!='V':
                    vert=textSize #px
                    horz=tw #px
                    rAngle=0
                else:
                    vert=tw #px
                    horz=textSize #px
                    rAngle=270
                    
                try:
                    containerY=_container(leftBottom.getY(),leftBottom.getY()-vert,containerYmax,containerYmin)
                    containerYmax=containerY[0]
                    containerYmin=containerY[1]
                except NameError:
                    containerYmax=max(leftBottom.getY(),leftBottom.getY()-vert)
                    containerYmin=min(leftBottom.getY(),leftBottom.getY()-vert)
                    
                try:
                    containerX=_container(leftBottom.getX(),leftBottom.getX()+horz,containerXmax,containerXmin)
                    containerXmax=containerX[0]
                    containerXmin=containerX[1]
                except NameError:
                    containerXmax=max(leftBottom.getX(),leftBottom.getX()+horz)
                    containerXmin=min(leftBottom.getX(),leftBottom.getX()+horz)
                _text(leftBottom.getX(),leftBottom.getY(),textString,textSize*4.0/3.0,font_weight,font_family,rAngle,symbTextColor_) #some discripancy here textSize should be in px but given in pt units appears as px
            elif "WINDOW"==z[0]:
                windowIndex=list(windows.keys())
                if int(z[1]) not in windowIndex:
                    windows[int(z[1])]=Window(Coordinate(float(z[2]),float(z[3])),z[4],int(z[5]))
            elif "SYMATTR"==z[0]:
                try:
                    correspondingWindow=windows[AttributeIndices[z[1]]]
                    alignment=_rotateAlign(correspondingWindow.getAlignment(),symbTheta)
                    alignment=_mirrorAlign(alignment,isMirror)
                    coordinate=_transform(correspondingWindow.getCoordinate(),isMirror,symbTheta,symbC)
                    textSize=sizes[correspondingWindow.getSIndex()]
                    try:
                        textString=windowValues[AttributeIndices[z[1]]]
                    except KeyError:
                        textString=''
                        i=2
                        try:
                            while True:
                                textString+=(z[i]+' ')
                                i+=1
                        except IndexError:
                            textString=textString[:-1]
                    tw=_tw_in_px(textString,font_family,textSize,font_weight)
                    leftBottom=_leftBottomC(coordinate,alignment,textSize,tw)
                    if alignment[0]!='V':
                        bbMin=Coordinate(leftBottom.getX(),leftBottom.getY()-textSize)
                        bbMax=Coordinate(leftBottom.getX()+tw,leftBottom.getY())
                        rAngle=0
                    else:
                        bbMin=Coordinate(leftBottom.getX()-textSize,leftBottom.getY()-tw)
                        bbMax=Coordinate(leftBottom.getX(),leftBottom.getY())
                        rAngle=270
                    containerMax=Coordinate(containerXmax,containerYmax)
                    containerMin=Coordinate(containerXmin,containerYmin)
                    _text(leftBottom.getX(),leftBottom.getY(),textString,textSize*4.0/3.0,font_weight,font_family,rAngle,symbAttrColor_)
                except KeyError:
                    pass    
            elif "PIN"==z[0]:
                pinAlignment=z[3]
                pinOffset=int(z[4])
                pinLoc=Coordinate(float(z[1]),float(z[2]))
                pinSpot=_transform(pinLoc,isMirror,symbTheta,symbC)
                _spot(pinSpot.getX(),pinSpot.getY(),symbPinColor_)
                roundPinSpot=Coordinate(round(pinSpot.getX(),3),round(pinSpot.getY(),3))
                if len(pIntsecLocations)!=0:
                    for intersectionC in list(pIntsecLocations.keys()):
                        if intersectionC==roundPinSpot:
                            pIntsecLocations[intersectionC]+=1
                            break
                    else:
                        pIntsecLocations[roundPinSpot]=1
                else:
                    pIntsecLocations[roundPinSpot]=1
                        
                if pinAlignment!='NONE':
                    index+=1
                    xNext=lines[index][:-1].split(' ')
                    if xNext[0]=="PINATTR" and xNext[1]=="PinName":
                        if xNext[2][0]=='_':
                            pinName=xNext[2][1:]
                            isHeadLine=True
                        else:
                            pinName=xNext[2]
                            isHeadLine=False
                            
                        correctedAlignments={'LEFT':'Left','RIGHT':'Right','TOP':'Top','BOTTOM':'Bottom','VLEFT':'VTop','VRIGHT':'VBottom','VTOP':'VRight','VBOTTOM':'VLeft'}
                        pinAlignment=correctedAlignments[pinAlignment]
                        pinLoc=_transform(_pinOffsetC(pinLoc,pinOffset,pinAlignment),isMirror,symbTheta,symbC)
                        pinAlignment=_rotateAlign(pinAlignment,symbTheta)
                        pinAlignment=_mirrorAlign(pinAlignment,isMirror)
                        tw=_tw_in_px(pinName,pin_font_family,pin_font_size_pt,pin_font_weight)
                        leftBottom=_leftBottomC(pinLoc,pinAlignment,pin_font_size,tw)
                        if pinAlignment[0]!='V':
                            rAngle=0
                        else:
                            rAngle=270
                        _text(leftBottom.getX(),leftBottom.getY(),pinName,pin_font_size*4.0/3.0,pin_font_weight,pin_font_family,rAngle,symbPinColor_)
                        if isHeadLine:
                            _HeadlineText(leftBottom,tw,pin_font_size,pinAlignment,symbPinColor_)
        index+=1
def _refineLine(line):
    out=''
    for char in line:
        if char in printChar:
            out+=char
    out+='\n'
    return(out)

def draw(spiceFile,saveAddress):
    global pIntsecLocations,pIntsecDirections,nGnCflags
    global dwg
    
    pIntsecLocations={}
    pIntsecDirections={}
    nGnCflags={}
    linecache.clearcache()
    dwg = svgwrite.Drawing(saveAddress, profile='tiny')
    lineNo=1
    with open(spiceFile,'r') as firstfile, open(r'temp.txt','w') as secondfile:
        for lineX in firstfile:
            secondfile.write(_refineLine(lineX))
    firstfile.close()
    secondfile.close()
    try:
        while True:
            x=linecache.getline(r'temp.txt',lineNo)
            if x!="":
                if x[-1]=='\n':
                    z=x[:-1].split(' ')
                else:
                    z=x.split(' ')
                if z[0]=='WIRE':
                    start=Coordinate(float(z[1]),float(z[2]))
                    end=Coordinate(float(z[3]),float(z[4]))
                    _line(start.getX(),start.getY(),end.getX(),end.getY(),wireColor_)
                    if len(pIntsecLocations)!=0:
                        for intersectionC in list(pIntsecLocations.keys()):
                            if intersectionC==start:
                                pIntsecLocations[intersectionC]+=1
                                break
                        else:
                            pIntsecLocations[start]=1
                        for intersectionC in list(pIntsecLocations.keys()):
                            if intersectionC==end:
                                pIntsecLocations[intersectionC]+=1
                                break
                        else:
                            pIntsecLocations[end]=1
                    else:
                        pIntsecLocations[start]=1
                        pIntsecLocations[end]=1
                elif z[0]=='SYMBOL':
                    filePath=sysPath+r'\Resource\sym\\'+z[1]+'.txt'
                    symbC=Coordinate(-float(z[2]),-float(z[3]))
                    orientation=z[4]
                    if orientation[0]=='M':
                        isMirror=True
                    else:
                        isMirror=False
                    rAngle=int(orientation[1:])
                    windows={}
                    values={}
                    lineNo+=1
                    x=linecache.getline(r'temp.txt',lineNo)
                    try:
                        if x[-1]=='\n':
                            z=x[:-1].split(' ')
                        else:
                            z=x.split(' ')
                    except IndexError:
                        break
                    while z[0]=='WINDOW' or z[0]=='SYMATTR':
                        if z[0]=='WINDOW':
                            windows[int(z[1])]=Window(Coordinate(float(z[2]),float(z[3])),z[4],int(z[5]))
                        elif z[0]=='SYMATTR':
                            AttributeIndicesX={'InstName':0,'Value':3,'SpiceModel':38,'Value2':123,'SpiceLine':39,'SpiceLine2':40,'Type':1}
                            attributeValue=''
                            i=2
                            try:
                                while True:
                                    attributeValue+=(z[i]+' ')
                                    i+=1
                            except IndexError:
                                attributeValue=attributeValue[:-1]
                            values[AttributeIndicesX[z[1]]]=attributeValue
                        lineNo+=1
                        x=linecache.getline(r'temp.txt',lineNo)
                        try:
                            if x[-1]=='\n':
                                z=x[:-1].split(' ')
                            else:
                                z=x.split(' ')
                        except IndexError:
                            break
                    lineNo-=2
                    _symb(symbC,rAngle,isMirror,windows,values,filePath)
                elif z[0]=='TEXT':
                    textLoc=Coordinate(float(z[1]),float(z[2]))
                    textAlignment=z[3]
                    textSize=sizes[int(z[4])]
                    textString=''
                    i=5
                    try:
                        while True:
                            textString+=(z[i]+' ')
                            i+=1
                    except IndexError:
                        textString=textString[1:-1]
                    tw=_tw_in_px(textString,font_family,_close(textSize),font_weight)
                    leftBottom=_leftBottomC(textLoc,textAlignment,textSize,tw)
                    if textAlignment[0]!='V':
                        rAngle=0
                    else:
                        rAngle=270
                    _text(leftBottom.getX(),leftBottom.getY(),textString,font_size,font_weight,font_family,rAngle,textColor_)
                elif z[0]=='FLAG' and z[3]!='0' and z[3]!='COM':
                    _flag(float(z[1]),float(z[2]),z[3],flagColor_,0)
                    nGnCflags[Coordinate(float(z[1]),float(z[2]))]=[z[3],'']#alignment]
                elif z[0]=='FLAG' and z[3]=='0':
                    _gnd(float(z[1]),float(z[2]),gndColor_,0)
                elif z[0]=='FLAG' and z[3]=='COM':
                    _com(float(z[1]),float(z[2]),comColor_,0)
                elif z[0]=='BUSTAP':
                    _busTap(float(z[1]),float(z[2]),float(z[3]),float(z[4]),busTapColor_)
            else:
                break
            lineNo+=1
    except EOFError:
        pass
    for x in list(pIntsecLocations.keys()):
        if pIntsecLocations[x]>=3:
            _squareSpot(x.getX(),x.getY(),intsecColor_)
    dwg.save()
    os.remove(r'temp.txt')
