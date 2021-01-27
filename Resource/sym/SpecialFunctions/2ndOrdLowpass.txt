Version 4
SymbolType CELL
LINE Normal -80 8 -72 16
LINE Normal -80 24 -72 16
LINE Normal -80 -27 143 -27
LINE Normal -80 -27 -80 64
LINE Normal -80 64 144 64
LINE Normal 144 64 160 16
LINE Normal 143 -27 160 16
LINE Normal 35 -7 -4 -7
LINE Normal 60 39 35 -7
WINDOW 0 -65 -43 Left 2
WINDOW 3 -64 80 Left 2
SYMATTR Value f0=1k Q=.5 H=1
SYMATTR Prefix X
SYMATTR Description Second Order High Pass Filter
SYMATTR ModelFile 2ndOrderLowpass.sub
SYMATTR SpiceModel 2ndOrderLowpass
PIN -80 16 LEFT 12
PINATTR PinName IN
PINATTR SpiceOrder 1
PIN 160 16 RIGHT 12
PINATTR PinName OUT
PINATTR SpiceOrder 2
