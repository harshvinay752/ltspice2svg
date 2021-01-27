# ltspice2svg 2021.01

Many times engineers need high resolution images of LTspice schematics. Specially in case of large schematics, the inbuilt option of 'Copy to Clipboard' picks up raster images which are uneasy to use.
Also in case of using schematics in Documents, the raster images are not good to render.

This tool can be used to convert LTspice schematic .asc files to SVG files, which can then  be fine tuned for beautiful schematics.


# Words of Developer

This is the first version of this library, however being frank to users, this version is not able to detect the GND, COM, directional flag envelopes and flag directions. I would appreciate any developer from any community who wants to contribute to this project.

Being a graduation student, I am unable to work over it for long. I will try to release next version having the above features as soon as possible.

# Features

The following attributes of SVG drawing can be manipulated from defaults. With syntax written along with.

## Color of different parts of Schematic

Function called 'colour' can be used to manipulate the colors.

|Color variable |Default Value| Description |
|----------------|-------------------------------|---|
|symbColor|#000000|Color of stroke of basic shapes viz. Rectangle, Circle, Line and Arc used for making Symbols or Components|
|symbTextColor|#42f5aa|Color of text used for making Symbols or Components|
|symbAttrColor|#f59e42|Color of attributes of Symbols or Components|
|symbPinColor|#8742f5|Color of pin symbols of Symbols or Components, here circle is used to represent it|
|symbFillColor|#fff9eb|Color of rectangle fill color used to make Symbols or Components|
|flagColor|#77fc03|Color of Text flags|
|gndColor|#fc0352|Color of GROUND/GND symbol|
|comColor|#03bafc|Color of COMMON/COM symbol|
|wireColor|#524e63|Color of wires|
|intsecColor|#0000ff|Color of junctions symbols, here square is used to represent it|
|textColor|#eb3464|Color of Text/Comment|
|busTapColor|#ec03fc|Color of bus taps|

Syntax:

>colour( isBW=False, symbColor="#000000", symbTextColor="#42f5aa", symbAttrColor="#f59e42", symbPinColor="#8742f5", symbFillColor="#fff9eb", flagColor="#77fc03", gndColor="#fc0352", comColor="#03bafc", wireColor="#524e63", intsecColor="#0000ff", textColor="#eb3464", busTapColor="#ec03fc")

Example:
> from ltspice2svg import * <br>
> colour (gndColor ="#20fc03",  comColor ="#00bbff")

`There is a special variable in colour settings described as follows which holds a special importance:`
|Variable|Default Value|Description|
|--|--|--|
|isBW|False|If isBW is set to True then all colors are set to Black, hence generating Black and White SVGs.


`For all color variables any valid hex-coded color value is acceptable, wheras for isBW only Boolean values are accepted.`


## Font properties

Function called 'setFont' can be used to manipulate the font properties.

|Variable |Default Value| Description|
|-|-|-|
|fontSize|12|Font size of Text/Comments in pt|
|fontWeight|"bold"|Font weight of Text/Comments/Flags|
|fontFamily|"Tahoma"|Font family of Text/Comments/Flags|
|flagFontSize|10|Font size of Flag texts in pt|
|pinFontSize|6|Font size for pin text in pt|
|pinFontWeight|"normal"|Font weight for pin text|
|pinFontFamily|"Arial"|Font family for pin text|

Syntax:
>setFont (fontSize=12, fontWeight="bold", fontFamily="Tahoma", flagFontSize=10, pinFontSize=6, pinFontWeight="normal", pinFontFamily="Arial")

Example:
> from ltspice2svg import * <br>
> setFont (fontSize  =12, pinFontWeight  ='Normal', fontFamily  ="SimSun")

`For all font sizes any integer value from 1 to 144 are acceptable. Font weight can be either 'Normal' or 'Bold'. Also font family can be any font from those mentioned below:`

||||||
|-|-|-|-|-|
|Arial|Bahnschrift|Calibri|Cambria|Candara|
|Comic Sans MS|Consolas|Constantia|Corbel|Courier New|
|Ebrima|Franklin Gothic Medium|Gabriola|Gadugi|Impact|
|Ink Free|Javanese Text|Leelawadee UI|Lucida Console|Malgun Gothic|
|Microsoft Himalaya|Mongolian Baiti|MS Gothic|MV Boli|Myanmar Text|
|Nirmala UI|Segoe Print|SimSun|Sitka Text|Sylfaen|
Tahoma|Times New Roman|Trebuchet MS|

## Pen properties

Function called 'setPen' can be used to manipulate the pen.

|Variable |Default Value| Description|
|-|-|-|
|lineWidth|0.3|Width of stroke of basic shapes|
|ISside|4|Junction square side in pt|
|PPradius|2|Pin circle radius in pt|

Syntax:
> setPen (lineWidth=0.3, ISside=4, PPradius=2)

Example:
> from ltspice2svg import * <br>
> setPen (width =0.6)

`All three parameters can be Float or Integer value with  stroke width, junction square side, pin circle radius from 0 to 5, 1 to 20 and 1 to 20 respectively.`

# Drawing SVG

SVG can be drawn using 'draw' function with attributes set (as described above). If none attribute is set, then default values are used.
Syntax:
> draw (spiceFileAddress, saveAddress)

Example:
> from ltspice2svg import * <br>
> draw (r'starter.asc', r'schematic.svg')
