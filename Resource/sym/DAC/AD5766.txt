Version 4
SymbolType CELL
LINE Normal -160 144 -160 -144
LINE Normal 96 144 -160 144
LINE Normal 209 -1 96 144
LINE Normal 96 -144 209 -1
LINE Normal -160 -144 96 -144
TEXT 0 0 Center 2 ADI
WINDOW 0 0 -47 Center 2
WINDOW 3 6 42 Center 2
WINDOW 39 7 74 Center 0
WINDOW 40 7 86 Center 0
WINDOW 123 6 63 Center 0
SYMATTR Value AD5766
SYMATTR SpiceLine dither_scale=0
SYMATTR SpiceLine2 dither_inv=0
SYMATTR Value2 Range=8
SYMATTR Prefix X
SYMATTR Description 16-Channel, 16Bit Voltage Output denseDACs (one channel, output stage modeled)
SYMATTR ModelFile AD5766.sub
PIN -160 -64 LEFT 8
PINATTR PinName Vdac
PINATTR SpiceOrder 1
PIN -160 80 LEFT 8
PINATTR PinName NO
PINATTR SpiceOrder 2
PIN 32 -144 TOP 8
PINATTR PinName AVdd
PINATTR SpiceOrder 3
PIN 32 144 BOTTOM 8
PINATTR PinName AVss
PINATTR SpiceOrder 4
PIN 208 0 RIGHT 8
PINATTR PinName Vout
PINATTR SpiceOrder 5
PIN -80 144 BOTTOM 8
PINATTR PinName GND
PINATTR SpiceOrder 6
