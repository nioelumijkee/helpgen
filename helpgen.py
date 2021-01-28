#!/usr/bin/python3

# ---------------------------------------------------------------------------- #
import sys

# ---------------------------------------------------------------------------- #
def to_canvas_main(d):
    return("#N canvas %d %d %d %d %d;\n" %
           (d['ox'], d['oy'], d['w'], d['h'], d['fs']))

# ---------------------------------------------------------------------------- #
def to_canvas(d):
    return("#X obj %d %d cnv %d %d %d %s %s %s %d %d %d %d %d %d 0;\n" % 
           (d['ox'], d['oy'], d['size'], d['w'], d['h'], 
            d['snd'], d['rcv'], d['lab'],
            d['ldx'], d['ldy'], d['font'], d['fs'],
            d['bcol'], d['lcol']))

# ---------------------------------------------------------------------------- #
def to_text(d):
    return("#X text %d %d %s, f %d;\n" %
           (d['ox'], d['oy'], d['text'], d['ws']))

# ---------------------------------------------------------------------------- #
def write_to_buffer(s):
    global oy
    oy = oy - s['top_oy_px']
    oy_top = oy
    canvas = {'ox' : 0,
              'oy' : 0, 
              'size' : 4,
              'w' : 4,
              'h' : 4, 
              'snd' : 'empty',
              'rcv' : 'empty',
              'lab' : 'empty', 
              'ldx' : 0,
              'ldy' : 0,
              'font' : 0, 
              'fs' : 12,
              'bcol' : 0,
              'lcol' : 22}
    text = {'ox' : 0,
            'oy' : 0,
            'text' : 'comment',
            'ws' : 80}

    # canvas bot frame
    canvas['ox'] = s['bot_ox_px']
    canvas['oy'] = oy
    canvas['size'] = s['cnv_size']
    canvas['w'] = s['bot_frame_px'] + s['bot_w_px'] + s['bot_frame_px']
    canvas['h'] = s['bot_frame_px'] + s['text_oy_top_px'] + (s['font_h_px'] * len(s['text'])) + s['text_oy_bot_px'] + s['bot_frame_px']
    canvas['lab'] = 'empty'
    canvas['snd'] = 'bot_frame'
    canvas['ldx'] = 16
    canvas['ldy'] = 16
    canvas['font'] = 0
    canvas['fs'] = 10
    canvas['bcol'] = s['bot_frame_color']
    canvas['lcol'] = s['bot_frame_color'] 
    buf.append(to_canvas(canvas))
    oy = oy + s['bot_frame_px']
    
    # canvas bot back
    canvas['ox'] = s['bot_ox_px'] + s['bot_frame_px']
    canvas['oy'] = oy
    canvas['size'] = s['cnv_size']
    canvas['w'] = s['bot_w_px']
    canvas['h'] = s['text_oy_top_px'] + (s['font_h_px'] * len(s['text'])) + s['text_oy_bot_px']
    canvas['lab'] = 'empty'
    canvas['snd'] = 'bot_back'
    canvas['ldx'] = 16
    canvas['ldy'] = 16
    canvas['font'] = 0
    canvas['fs'] = 10
    canvas['bcol'] = s['bot_back_color']
    canvas['lcol'] = s['bot_back_color'] 
    buf.append(to_canvas(canvas))
    oy = oy + s['text_oy_top_px']

    # text ------------------------------------------------------------------- #
    text_ws = (s['bot_w_px'] - s['text_ox_px'] - s['text_ox_px']) // s['font_w_px']
    row = 0
    for str in s['text']:
        # one string
        if debug:
            print("-" * 20)
            print(str)
        buf_str = []
        white_space = []
        text_ofs = []
        word = 0
        word_start = 0
        word_end = 0
        sym = ' '
        sym_z = ' '
        i = 0
        while i < len(str):
            sym = str[i]
            if (sym != ' '):
                word = 1
            if i == (len(str) - 1):
                buf_str.append(str[word_start:])
                i = i + 1
            elif (sym_z == ' ') and (sym == ' ') and (word == 1):
                word_end = i - 1
                buf_str.append(str[word_start:word_end])
                word_start = i - 1
                word = 0
                i = i + 1
            else:
                i = i + 1
            sym_z = sym
        # whitespace, text offset
        ofs = 0
        for l in buf_str:
            i = 0
            j = 0
            word = 0
            while i < len(l):
                if l[i] != ' ':
                    j =  i
                    i = len(l)
                else:
                    i = i + 1
            white_space.append(j)
            text_ofs.append(ofs + j)
            ofs = ofs + len(l)
        if debug:
            print(buf_str)
            print(white_space)
            print(text_ofs)
        # add to buffer
        i = 0
        for l in buf_str:
            t_ox = s['bot_ox_px'] + s['bot_frame_px'] + s['text_ox_px']
            t_ox += text_ofs[i] * s['font_w_px']
            text['ox'] = t_ox
            text['oy'] = oy + (row * s['font_h_px']) + 4 # correction
            text['text'] = l
            text['ws'] = text_ws - text_ofs[i]
            buf.append(to_text(text))
            i = i + 1
        #
        row = row + 1
    # text ------------------------------------------------------------------- #

    
    # canvas top frame
    oy_top = oy_top + s['top_oy_px']
    canvas['ox'] = s['top_ox_px']
    canvas['oy'] = oy_top
    canvas['size'] = s['cnv_size']
    canvas['w'] = s['top_frame_px'] + s['top_w_px'] + s['top_frame_px']
    canvas['h'] = s['top_frame_px'] + s['top_h_px'] + s['top_frame_px']
    canvas['lab'] = 'empty'
    canvas['snd'] = 'top_frame'
    canvas['ldx'] = 16
    canvas['ldy'] = 16
    canvas['font'] = 0
    canvas['fs'] = 10
    canvas['bcol'] = s['top_frame_color']
    canvas['lcol'] = s['top_frame_color'] 
    buf.append(to_canvas(canvas))
    oy_top = oy_top + s['top_frame_px']
    
    # canvas top back
    canvas['ox'] = s['top_ox_px'] + s['top_frame_px']
    canvas['oy'] = oy_top
    canvas['size'] = s['cnv_size']
    canvas['w'] = s['top_w_px']
    canvas['h'] = s['top_h_px']
    canvas['lab'] = s['name']
    canvas['snd'] = 'top_back'
    canvas['ldx'] = s['top_ldx_px']
    canvas['ldy'] = s['top_ldy_px']
    canvas['font'] = s['top_font']
    canvas['fs'] = s['top_fs']
    canvas['bcol'] = s['top_back_color']
    canvas['lcol'] = s['top_font_color'] 
    buf.append(to_canvas(canvas))

    oy = oy + (s['font_h_px'] * len(s['text'])) + s['text_oy_bot_px']
    oy = oy + s['bot_frame_px'] + s['section_oy']

# ---------------------------------------------------------------------------- #
def parse_file(filename):
    par = {'main_ox_px' : 50,
           'main_oy_px' : 50,
           'section_oy' : 4,
           'font_fs': 10,
           'font_w_px' : 6,
           'font_h_px' : 11,
           'cnv_size' : 4,
           'text_ox_px' : 16,
           'text_oy_top_px' : 10,
           'text_oy_bot_px' : 10,
           'name' : 'objectname',
           'top_ox_px' : 16,
           'top_oy_px' : -8,
           'top_w_px' : 100,
           'top_h_px' : 16,
           'top_frame_px' : 1,
           'top_ldx_px' : 8,
           'top_ldy_px' : 8,
           'top_font' : 1,
           'top_fs' : 14,
           'top_frame_color' : 1,
           'top_font_color' : 22,
           'top_back_color' : 0,
           'bot_ox_px' : 2,
           'bot_oy_px' : 20,
           'bot_w_px' : 500,
           'bot_frame_px' : 1,
           'bot_frame_color' : 1,
           'bot_back_color' : 0,
           'text' : []}
    j = 0
    f = open(filename, "r")
    line = f.readline()
    while line:
        if line[0] != '#':
            i = line.find('=')
            s_par = line[:i]
            s_par = s_par.strip()
            s_arg = line[i+1:]
            s_arg = s_arg.rstrip()
            if s_par == 'section':
                if j != 0:
                    ss.append(dict(par))
                    par['text']  = []
                s_arg = s_arg.strip()
                par['name'] = s_arg
                j += 1
            elif s_par == 'text':
                par['text'].append(s_arg)
            elif s_par != '' and s_arg.isdigit:
                par[s_par] = int(s_arg)
        line = f.readline()
    ss.append(dict(par))
    f.close()
   
# ---------------------------------------------------------------------------- #
if (len(sys.argv) <= 1):
    print("usage: file.conf")
    exit()

debug = False
canvas_main = {}
ss = []
file_in = sys.argv[1]
buf = []
oy = 1

parse_file(file_in)

for s in ss:
    write_to_buffer(s)

j = len(ss)
if (j > 0):
    j -= 1
    canvas_main['ox'] = ss[j]['main_ox_px']
    canvas_main['oy'] = ss[j]['main_oy_px']
    canvas_main['w'] =  ss[j]['bot_ox_px'] + ss[j]['bot_frame_px'] + ss[j]['bot_w_px'] + ss[j]['bot_ox_px'] + ss[j]['bot_frame_px'] + 1
    canvas_main['h'] = oy - ss[j]['section_oy'] + 2
    canvas_main['fs'] = 10

file_out = ss[0]['name'] + '-help.pd'
f = open(file_out, "w")
f.write(to_canvas_main(canvas_main))
for i in buf:
    f.write(i)
f.close()

print('"' + file_in + '" -> "' + file_out + '"')
exit()
