from opimodel import colors, fonts, rules, widgets
from renderers.css import render
import os

# Read the color and font data CSStudio configuration files
example_dir = os.path.dirname(os.path.realpath(__file__))
colors.parse_css_color_file(os.path.join(example_dir, 'examples', 'color.def'))
fonts.parse_css_font_file(os.path.join(example_dir, 'examples', 'font.def'))


# root widgetz
d = widgets.Display(604, 367)
d.set_bg_color(colors.CANVAS)

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
#each green rectangle
def green_rectangle (x,y,pv_prefix,pv_prefix2):
	#top right square
	w = widgets.Led(x+10, y+5, 11, 11,pv_prefix.format("V")+"SLOW:DISABLED")
	w.set_bg_color(colors.GREEN)
	w.transparent = False
	w.square_led = True
	w.effect_3d = False
	w.border_alarm_sensitive = False
	w.bulb_border_color = colors.BLACK
	w.off_color = colors.GREEN_LED_ON
	w.on_color = colors.GREEN_LED_OFF
	w.bulb_border = '1'
	d.add_child(w)

	#top left square
	w = widgets.Led(x, y+5, 11, 11,pv_prefix.format("H")+"SLOW:DISABLED")
	w.set_bg_color(colors.GREEN)
	w.transparent = False
	w.square_led = True
	w.effect_3d = False
	w.border_alarm_sensitive = False
	w.bulb_border_color = colors.BLACK
	w.off_color = colors.GREEN_LED_ON
	w.on_color = colors.GREEN_LED_OFF
	w.bulb_border = '1'
	d.add_child(w)


	#mini rectangle
	w = widgets.Led(x, y, 21, 6,pv_prefix2+"CF:ENABLED_S")
	w.set_bg_color(colors.GREEN)
	w.transparent = False
	w.square_led = True
	w.effect_3d = False
	w.border_alarm_sensitive = False
	w.bulb_border_color = colors.BLACK
	w.off_color = colors.GREEN_LED_OFF
	w.on_color = colors.GREEN_LED_ON
	w.bulb_border = '1'
	d.add_child(w)

	#bottom right square
	w = widgets.Led(x+10, y+15, 11, 11, pv_prefix.format("V")+"FAST:DISABLED")
	w.set_bg_color(colors.GREEN)
	w.transparent = False
	w.square_led = True
	w.effect_3d = False
	w.border_alarm_sensitive = False
	w.bulb_border_color = colors.BLACK
	w.off_color = colors.GREEN_LED_ON
	w.on_color = colors.GREEN_LED_OFF
	w.bulb_border = '1'
	d.add_child(w)

	#bottom left square
	w = widgets.Led(x, y+15, 11, 11, pv_prefix.format("H")+"FAST:DISABLED")
	w.set_bg_color(colors.GREEN)
	w.transparent = False
	w.square_led = True
	w.effect_3d = False
	w.border_alarm_sensitive = False
	w.bulb_border_color = colors.BLACK
	w.off_color = colors.GREEN_LED_ON
	w.on_color = colors.GREEN_LED_OFF
	w.bulb_border = '1'
	d.add_child(w)


#most of the green rectangles
for x in range(24):
	for y in range(7):
		green_rectangle(28+24*x, 135+29*y, "SR{:02d}C-PC-{}BPM-{:02d}:".format(x+1,"{}",y+1),"SR{:02d}C-DI-EBPM-{:02d}:".format(x+1,y+1 ))


#isolated green rectangle 
green_rectangle(52,338,"SR02C-PC-{}BPM-08:","SR02C-DI-EBPM-08:")

#other four isolatedish green rectangles
green_rectangle(220,77,"SR09S-PC-{}BPM-01:","SR09S-DI-EBPM-01:")
green_rectangle(316,77,"SR13S-PC-{}BPM-01:","SR13S-DI-EBPM-01:")
green_rectangle(220,106,"SR09S-PC-{}BPM-02:","SR09S-DI-EBPM-02:")
green_rectangle(316,106,"SR09S-PC-{}BPM-02:","SR13S-DI-EBPM-02:")



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