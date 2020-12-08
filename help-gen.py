#!/usr/bin/python3
#
# generate help.pd files
# arguments:
# nothing - help
# 1 - file

###############################################################################
# import
import sys

###############################################################################
# default style
# offset main window. 
Cnv_main_ox = 50
Cnv_main_oy = 50

# width window.
Cnv_main_w = 600

# font for comments.
Cnv_main_fs = 10
Cnv_main_font_w = 6
Cnv_main_font_h = 11

# for all canvas.
Cnv_all_size = 4

# for top canvas.
Cnv_top_ldx = 8
Cnv_top_ldy = 12
Cnv_top_font = 0
Cnv_top_fs = 16

# for rest canvas.
Cnv_rest_ldx = 8
Cnv_rest_ldy = 12
Cnv_rest_font = 0
Cnv_rest_fs = 12

# for top canvas.
Cnv_top_bcol = 14
Cnv_top_lcol = -1
Cnv_top_h = 0
Cnv_top_h_add = 0

# for canvas Example.
Cnv_example_bcol = 18
Cnv_example_lcol = -1
Cnv_example_h = 4
Cnv_example_h_add = 200

# for canvas Desc.
Cnv_desc_bcol = 18
Cnv_desc_lcol = -1
Cnv_desc_h = 4

# for canvas Argument.
Cnv_arg_bcol = 18
Cnv_arg_lcol = -1
Cnv_arg_h = 4

# for canvas Inlet.
Cnv_inlet_bcol = 18
Cnv_inlet_lcol = -1
Cnv_inlet_h = 4

# for canvas Outlet.
Cnv_outlet_bcol = 18
Cnv_outlet_lcol = -1
Cnv_outlet_h = 4

# for canvas Info.
Cnv_info_bcol = 19
Cnv_info_lcol = -1
Cnv_info_h = 0

# offset comments.
Text_cnv_ox = 24
Text_cnv_oy_hi = 18
Text_cnv_oy_lo = 6
Text_text_oy = 2

###############################################################################
# default
ObjectName = []
ObjectName.append('empty')
DescBriefly = []
DescBriefly.append('none')
Example = []
Desc = []
Argument = []
Inlet = []
Outlet = []
Info = []

###############################################################################
# buffer
Buffer = []

###############################################################################
# functions
def f_parse_file(filename):
    global Cnv_main_ox
    global Cnv_main_oy
    global Cnv_main_w
    global Cnv_main_fs
    global Cnv_main_font_w
    global Cnv_main_font_h
    global Cnv_all_size
    global Cnv_top_ldx
    global Cnv_top_ldy
    global Cnv_top_font
    global Cnv_top_fs
    global Cnv_rest_ldx
    global Cnv_rest_ldy
    global Cnv_rest_font
    global Cnv_rest_fs
    global Cnv_top_bcol
    global Cnv_top_lcol
    global Cnv_top_h
    global Cnv_top_h_add
    global Cnv_top_bcol
    global Cnv_top_lcol
    global Cnv_top_h
    global Cnv_top_h_add
    global Cnv_example_bcol
    global Cnv_example_lcol
    global Cnv_example_h
    global Cnv_example_h_add
    global Cnv_desc_bcol
    global Cnv_desc_lcol
    global Cnv_desc_h
    global Cnv_desc_h_add
    global Cnv_arg_bcol
    global Cnv_arg_lcol
    global Cnv_arg_h
    global Cnv_arg_h_add
    global Cnv_inlet_bcol
    global Cnv_inlet_lcol
    global Cnv_inlet_h
    global Cnv_inlet_h_add
    global Cnv_outlet_bcol
    global Cnv_outlet_lcol
    global Cnv_outlet_h
    global Cnv_outlet_h_add
    global Cnv_info_bcol
    global Cnv_info_lcol
    global Cnv_info_h
    global Cnv_info_h_add
    global Text_cnv_ox
    global Text_cnv_oy_hi
    global Text_cnv_oy_lo
    global Text_txt_oy
    fd = open(filename, "r")
    line = '0'
    s_par = ''
    s_arg = ''
    while line:
        line = fd.readline()
        if line and line[0] != '#':
            i = line.find('=')
            s_par = line[:i]
            s_arg = line[i+1:]
            s_par = s_par.strip()
            s_arg = s_arg.strip()
            if s_par == 'ObjectName':
                ObjectName[0] = s_arg
            elif s_par == 'DescBriefly':
                DescBriefly[0] = s_arg
            elif s_par == 'Example':
                Example.append(s_arg)
            elif s_par == 'Desc':
                Desc.append(s_arg)
            elif s_par == 'Argument':
                Argument.append(s_arg)
            elif s_par == 'Inlet':
                Inlet.append(s_arg)
            elif s_par == 'Outlet':
                Outlet.append(s_arg)
            elif s_par == 'Info':
                Info.append(s_arg)
            elif s_par == 'Cnv_main_ox':
                Cnv_main_ox = int(s_arg)
            elif s_par == 'Cnv_main_oy':
                Cnv_main_oy = int(s_arg)
            elif s_par == 'Cnv_main_w':
                Cnv_main_w = int(s_arg)
            elif s_par == 'Cnv_main_fs':
                Cnv_main_fs = int(s_arg)
            elif s_par == 'Cnv_main_font_w':
                Cnv_main_font_w = int(s_arg)
            elif s_par == 'Cnv_main_font_h':
                Cnv_main_font_h = int(s_arg)
            elif s_par == 'Cnv_all_size':
                Cnv_all_size = int(s_arg)
            elif s_par == 'Cnv_top_ldx':
                Cnv_top_ldx = int(s_arg)
            elif s_par == 'Cnv_top_ldy':
                Cnv_top_ldy = int(s_arg)
            elif s_par == 'Cnv_top_font':
                Cnv_top_font = int(s_arg)
            elif s_par == 'Cnv_top_fs':
                Cnv_top_fs = int(s_arg)
            elif s_par == 'Cnv_rest_ldx':
                Cnv_rest_ldx = int(s_arg)
            elif s_par == 'Cnv_rest_ldy':
                Cnv_rest_ldy = int(s_arg)
            elif s_par == 'Cnv_rest_font':
                Cnv_rest_font = int(s_arg)
            elif s_par == 'Cnv_rest_fs':
                Cnv_rest_fs = int(s_arg)
            elif s_par == 'Cnv_top_bcol':
                Cnv_top_bcol = int(s_arg)
            elif s_par == 'Cnv_top_lcol':
                Cnv_top_lcol = int(s_arg)
            elif s_par == 'Cnv_top_h':
                Cnv_top_h = int(s_arg)
            elif s_par == 'Cnv_top_h_add':
                Cnv_top_h_add = int(s_arg)
            elif s_par == 'Cnv_top_bcol':
                Cnv_top_bcol = int(s_arg)
            elif s_par == 'Cnv_top_lcol':
                Cnv_top_lcol  = int(s_arg)
            elif s_par == 'Cnv_top_h':
                Cnv_top_h = int(s_arg)
            elif s_par == 'Cnv_top_h_add':
                Cnv_top_h_add = int(s_arg)
            elif s_par == 'Cnv_example_bcol':
                Cnv_example_bcol = int(s_arg)
            elif s_par == 'Cnv_example_lcol':
                Cnv_example_lcol = int(s_arg)
            elif s_par == 'Cnv_example_h':
                Cnv_example_h = int(s_arg)
            elif s_par == 'Cnv_example_h_add':
                Cnv_example_h_add = int(s_arg)
            elif s_par == 'Cnv_desc_bcol':
                Cnv_desc_bcol = int(s_arg)
            elif s_par == 'Cnv_desc_lcol':
                Cnv_desc_lcol = int(s_arg)
            elif s_par == 'Cnv_desc_h':
                Cnv_desc_h = int(s_arg)
            elif s_par == 'Cnv_desc_h_add':
                Cnv_desc_h_add = int(s_arg)
            elif s_par == 'Cnv_arg_bcol':
                Cnv_arg_bcol = int(s_arg)
            elif s_par == 'Cnv_arg_lcol':
                Cnv_arg_lcol = int(s_arg)
            elif s_par == 'Cnv_arg_h':
                Cnv_arg_h = int(s_arg)
            elif s_par == 'Cnv_arg_h_add':
                Cnv_arg_h_add = int(s_arg)
            elif s_par == 'Cnv_inlet_bcol':
                Cnv_inlet_bcol = int(s_arg)
            elif s_par == 'Cnv_inlet_lcol':
                Cnv_inlet_lcol = int(s_arg)
            elif s_par == 'Cnv_inlet_h':
                Cnv_inlet_h = int(s_arg)
            elif s_par == 'Cnv_inlet_h_add':
                Cnv_inlet_h_add = int(s_arg)
            elif s_par == 'Cnv_outlet_bcol':
                Cnv_outlet_bcol = int(s_arg)
            elif s_par == 'Cnv_outlet_lcol':
                Cnv_outlet_lcol = int(s_arg)
            elif s_par == 'Cnv_outlet_h':
                Cnv_outlet_h = int(s_arg)
            elif s_par == 'Cnv_outlet_h_add':
                Cnv_outlet_h_add = int(s_arg)
            elif s_par == 'Cnv_info_bcol':
                Cnv_info_bcol = int(s_arg)
            elif s_par == 'Cnv_info_lcol':
                Cnv_info_lcol = int(s_arg)
            elif s_par == 'Cnv_info_h':
                Cnv_info_h = int(s_arg)
            elif s_par == 'Cnv_info_h_add':
                Cnv_info_h_add = int(s_arg)
            elif s_par == 'Text_cnv_ox':
                Text_cnv_ox = int(s_arg)
            elif s_par == 'Text_cnv_oy_hi':
                Text_cnv_oy_hi = int(s_arg)
            elif s_par == 'Text_cnv_oy_lo':
                Text_cnv_oy_lo = int(s_arg)
            elif s_par == 'Text_txt_oy':
                Text_txt_oy = int(s_arg)
    # close file
    fd.close()

###############################################################################
def write_to_buffer(Src, str_lab, bcol, lcol, h, h_add):
    global Cnv_oy
    Canvas['oy'] = Cnv_oy
    Canvas['lab'] = str_lab
    Canvas['bcol'] = bcol
    Canvas['lcol'] = lcol

    Text_oy = Text_cnv_oy_hi + Canvas['oy']

    # text
    if len(Src) == 0:
        Text['oy'] = Text_oy
        Text['text'] = 'none.'
        i = Cnv_main_font_h
        i = i + Text_cnv_oy_hi + Text_cnv_oy_lo
        Canvas['h'] = i + h_add
        Cnv_oy = Canvas['oy'] + Canvas['h'] + 1
        if h > 0:
            Canvas['h'] = h
        Buffer.append(f_canvas(Canvas))
        if str_lab != 'Example:':
            Buffer.append(f_text(Text))
    elif len(Src) == 1:
        Text['oy'] = Text_oy
        Text['text'] = Src[0]
        i = f_text_height(Src[0], Text['ws'], Cnv_main_font_h)
        i = i + Text_cnv_oy_hi + Text_cnv_oy_lo
        Canvas['h'] = i + h_add
        Cnv_oy = Canvas['oy'] + Canvas['h'] + 1
        if h > 0:
            Canvas['h'] = h
        Buffer.append(f_canvas(Canvas))
        if str_lab != 'Example:':
            Buffer.append(f_text(Text))
    else :
        j = Text_oy
        for str in Src:
            Text['oy'] = j
            Text['text'] = str
            Buffer.append(f_text(Text))
            i = f_text_height(str, Text['ws'], Cnv_main_font_h)
            j = j + i + Text_text_oy
        j = j - Text_text_oy + Text_cnv_oy_lo - Canvas['oy']
        Canvas['h'] = j + h_add
        Cnv_oy = Canvas['oy'] + Canvas['h'] + 1
        if h > 0:
            Canvas['h'] = h
        Buffer.insert((0 - len(Src)),f_canvas(Canvas))
    
###############################################################################
def f_canvas_main(L):
    return("#N canvas %d %d %d %d %d;\n" % (L['ox'], L['oy'], L['w'], L['h'], L['fs']))

###############################################################################
def f_canvas(L):
    return("#X obj %d %d cnv %d %d %d %s %s %s %d %d %d %d %d %d 0;\n" % 
           (L['ox'], L['oy'], L['size'], L['w'], L['h'], 
            L['snd'], L['rcv'], L['lab'],
            L['ldx'], L['ldy'], L['font'], L['fs'],
            L['bcol'], L['lcol']))

###############################################################################
def f_text(L):
    if L['text']:
        str = "#X text %d %d %s, f %d;\n" % (L['ox'], L['oy'], L['text'], L['ws'])
    else:
        str = ''
    return(str)

###############################################################################
def f_text_height(str, str_ws, str_h):
    row = 1
    sz = ' '
    sw = 0
    k = 0
    i = 0
    while i < len(str):
        s = str[i]
        # start word
        if sz == ' ' and s != ' ':
            sw = i
        sz = s
        i = i + 1
        # end row
        if k == str_ws - 1 :
            k = 0
            if s != ' ':
                row = row + 1
                i = sw
            else :  
                row = row + 1
        else :
            k = k + 1
    return(row * str_h)

###############################################################################
# structures
Canvas_main = {'ox' : 0,
               'oy' : 0,
               'w'  : 1, 
               'h'  : 1, 
               'fs' : 12}

Canvas = {'ox'   : 0,
          'oy'   : 0, 
          'size' : 2,
          'w'    : 1,
          'h'    : 1, 
          'snd'  : 'empty',
          'rcv'  : 'empty',
          'lab'  : 'empty', 
          'ldx'  : 0,
          'ldy'  : 0,
          'font' : 0, 
          'fs'   : 12,
          'bcol' : 0,
          'lcol' : 0}

Text = {'ox'   : 0,
        'oy'   : 0,
        'text' : 'comment',
        'ws'   : 40}

###############################################################################
# arguments
if (len(sys.argv) <= 1):
    print("usage: file.conf")
    exit()

###############################################################################
# files
f_parse_file('style.conf')
f_parse_file(sys.argv[1])

###############################################################################
# print result
print("File = " + sys.argv[1])
print("ObjectName = " , ObjectName)
print("DescBriefly = " , DescBriefly)
print("Example = " , Example)
print("Desc = " , Desc)
print("Argument = " , Argument)
print("Inlet = " , Inlet)
print("Outlet = " , Outlet)
print("Info = " , Info)
print("...")

###############################################################################
Cnv_oy = 1

###############################################################################
# for all
Canvas['ox'] = 1
Canvas['size'] = Cnv_all_size
Canvas['w'] = Cnv_main_w
Text['ox'] = Text_cnv_ox
Text['ws'] = (Cnv_main_w - (Text_cnv_ox * 2)) // Cnv_main_font_w

###############################################################################
# for top
Canvas['ldx'] = Cnv_top_ldx
Canvas['ldy'] = Cnv_top_ldy
Canvas['font'] = Cnv_top_font
Canvas['fs'] = Cnv_top_fs

write_to_buffer(DescBriefly, ObjectName[0], Cnv_top_bcol, Cnv_top_lcol, Cnv_top_h, 0)

###############################################################################
# for rest
Canvas['ldx'] = Cnv_rest_ldx
Canvas['ldy'] = Cnv_rest_ldy
Canvas['font'] = Cnv_rest_font
Canvas['fs'] = Cnv_rest_fs

write_to_buffer(Example, 'Example:', Cnv_example_bcol, Cnv_example_lcol, Cnv_example_h, Cnv_example_h_add)
write_to_buffer(Desc, 'Description:', Cnv_desc_bcol, Cnv_desc_lcol, Cnv_desc_h, 0)
write_to_buffer(Argument, 'Arguments:', Cnv_arg_bcol, Cnv_arg_lcol, Cnv_arg_h, 0)
write_to_buffer(Inlet, 'Inlets:', Cnv_inlet_bcol, Cnv_inlet_lcol, Cnv_inlet_h, 0)
write_to_buffer(Outlet, 'Outlets:', Cnv_outlet_bcol, Cnv_outlet_lcol, Cnv_outlet_h, 0)
write_to_buffer(Info, 'Info:', Cnv_info_bcol, Cnv_info_lcol, Cnv_info_h, 0)

###############################################################################
# for main
Canvas_main['ox'] = Cnv_main_ox
Canvas_main['oy'] = Cnv_main_oy
Canvas_main['w'] = Cnv_main_w + 3
Canvas_main['h'] = Cnv_oy + 1
Canvas_main['fs'] = Cnv_main_fs
###############################################################################
# write to file
file_help = ObjectName[0] + '-help.pd'
print("output file: " + file_help)
f_help = open(file_help, "w")

f_help.write(f_canvas_main(Canvas_main))
for i in Buffer:
    f_help.write(i)

f_help.close()

