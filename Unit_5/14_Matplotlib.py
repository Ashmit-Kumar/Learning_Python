import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Matplotlib Markers
# Mark each points with a circle
x=np.array([1,2,3,4,5,6])
y=np.array([4,2,4,5,7,3])
# plt.plot(x,y,marker='o') #this will mark each point with a circle and it will also give line
# plt.plot(x,y,marker='^') 
# plt.plot(x,y,marker='*') 
# plt.plot(x,y,marker='s') 
plt.show()

'''
Marker Reference
You can choose any of these markers:

Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
'''

# Format Strings fmt: You can also use the shortcut string notation parameter to specify the marker.
# This parameter is also called fmt, and is written with this syntax: marker|line|color

# plt.plot(x,y,'o:r')
# plt.plot(x,y,'o-.r')
# plt.plot(x,y,'o--r')
# plt.plot(x,y,'o-r')
plt.show()

'''
Line Reference
Line Syntax	Description
'-'	 Solid line	
':'	 Dotted line	
'--' Dashed line	
'-.' Dashed/dotted line

Color Reference
Color Syntax
'r'	  Red	
'g'	  Green	
'b'	  Blue	
'c'	  Cyan	
'm'	  Magenta	
'y'	  Yellow	
'k'	  Black	
'w'	  White
'''

# Marker Size
# plt.plot(x,y,'d:b' ,ms=10)
plt.show()


# Marker Colour
# For Marker Edge Colour
# plt.plot(y,'h--g',ms=10,mec='r')

# For Marker Face Colour
# plt.plot(y,'d-.c',ms=10,mfc='r')
plt.plot(y,'d-.c',ms=10,mfc='r',mec='b')
plt.show()

