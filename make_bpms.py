from opimodel import colors, fonts, rules, widgets
from renderers.css import render
import os

#each green rectangle
def green_rectangle (x,y):
	#top right square
	w = widgets.Rectangle(x+10, y+5, 11, 11)
	w.set_bg_color(colors.GREEN)
	w.line_color = colors.BLACK
	w.line_width = 1
	w.transparent = False
	d.add_child(w)

	#top left square
	w = widgets.Rectangle(x, y+5, 11, 11)
	w.set_bg_color(colors.GREEN)
	w.line_color = colors.BLACK
	w.line_width = 1
	w.transparent = False
	d.add_child(w)


	#mini rectangle
	w = widgets.Rectangle(x, y, 21, 6)
	w.set_bg_color(colors.GREEN)
	w.line_color = colors.BLACK
	w.line_width = 1
	w.transparent = False
	d.add_child(w)

	#bottom right square
	w = widgets.Rectangle(x+10, y+15, 11, 11)
	w.set_bg_color(colors.GREEN)
	w.line_color = colors.BLACK
	w.line_width = 1
	w.transparent = False
	d.add_child(w)

	#bottom left square
	w = widgets.Rectangle(x, y+15, 11, 11)
	w.set_bg_color(colors.GREEN)
	w.line_color = colors.BLACK
	w.line_width = 1
	w.transparent = False
	d.add_child(w)

# Read the color and font data CSStudio configuration files
example_dir = os.path.dirname(os.path.realpath(__file__))
colors.parse_css_color_file(os.path.join(example_dir, 'examples', 'color.def'))
fonts.parse_css_font_file(os.path.join(example_dir, 'examples', 'font.def'))

# root widgetz
d = widgets.Display(604, 367)
d.set_bg_color(colors.CANVAS)

#most of the green rectangles
for x in range(24):
	for y in range(7):
		green_rectangle(28+24*x, 135+29*y)
		
#isolated green rectangle 
green_rectangle(52,338)

#other four isolatedish green rectangles
green_rectangle(220,77)
green_rectangle(316,77)
green_rectangle(220,106)
green_rectangle(316,106)

#horizontal grey squares

for i in range(24):
	l = widgets.Label(28 +24*i, 48, 20, 25, '{:02d}'.format(i+1))
	l.set_font(fonts.FINE_PRINT)
	d.add_child(l)
	l.set_bg_color(colors.GREY_50_)
	l.transparent = False



l = widgets.Label(4, 77, 20, 25, "S1")
l.set_font(fonts.FINE_PRINT)
d.add_child(l)
l.set_bg_color(colors.GREY_50_)
l.transparent = False

l = widgets.Label(4, 106, 20, 25, "S2")
l.set_font(fonts.FINE_PRINT)
d.add_child(l)
l.set_bg_color(colors.GREY_50_)
l.transparent = False

#vertical grey squares
for i in range(8):
	l= widgets.Label(4, 135+29*i, 20, 25, '{:02d}'.format(i+1))
	l.set_font(fonts.FINE_PRINT)
	d.add_child(l)
	l.set_bg_color(colors.GREY_50_)
	l.transparent = False

#textbox
l = widgets.Label(354, 80, 164, 32, "All globally enabled BPMs\n are used by RF feedback")
l.set_font(fonts.FINE_PRINT)
d.add_child(l)
l.set_bg_color(colors.CANVAS)
l.transparent = False

#other textboxes
l = widgets.Label(558, 78, 40, 18, "master")
l.set_font(fonts.FINE_PRINT)
d.add_child(l)
l.set_bg_color(colors.CANVAS)
l.border_color = colors.BLACK
l.border_width = 1
l.border_style = 1
l.transparent = False

l = widgets.Label(558, 95, 21, 18, "SH")
l.set_font(fonts.FINE_PRINT)
d.add_child(l)
l.set_bg_color(colors.CANVAS)
l.border_color = colors.BLACK
l.border_width = 1
l.border_style = 1
l.transparent = False

l = widgets.Label(578, 95, 20, 18, "SV")
l.set_font(fonts.FINE_PRINT)
d.add_child(l)
l.set_bg_color(colors.CANVAS)
l.border_color = colors.BLACK
l.border_width = 1
l.border_style = 1
l.transparent = False

l = widgets.Label(558, 112, 21, 17, "FH")
l.set_font(fonts.FINE_PRINT)
d.add_child(l)
l.set_bg_color(colors.CANVAS)
l.border_color = colors.BLACK
l.border_width = 1
l.border_style = 1
l.transparent = False

l = widgets.Label(578, 112, 20, 17, "FV")
l.set_font(fonts.FINE_PRINT)
d.add_child(l)
l.set_bg_color(colors.CANVAS)
l.border_color = colors.BLACK
l.border_width = 1
l.border_style = 1
l.transparent = False

# Header
l = widgets.Label(4, 4, 596, 40, "SOFB and FOFB BPM Mask")
l.set_font(fonts.	HEADER_3)
d.add_child(l)
l.set_bg_color(colors.Color(rgb=(198,181,198)))
l.transparent = False

# Write the OPI file.
o = render.get_opi_renderer(d)
o.write_to_file("bpms.opi")