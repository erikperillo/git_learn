BALLOON_MAX_WIDTH = 128

def chunks(src_list, length):
    return [ src_list[i:i+length] for i in range(len(src_list))[::length] ]

def balloonFormat(message, max_width):
    message = message.replace("\r\n","\n").split("\n")
    return "\n".join([ "\n".join(chunks(line,max_width)) for line in message ])

def balloonFromFmt(fmt_msg, ver_border_chr, hor_border_chr, left_tail):
    fmt_msg_list = fmt_msg.split("\n") 
    balloon_max_size = max([ len(line) for line in fmt_msg_list ])

    hor_border = hor_border_chr * (balloon_max_size + 2)

    balloon = hor_border + "\n"
    balloon += "\n".join([ ver_border_chr + line + " " * (balloon_max_size - len(line)) + ver_border_chr for line in fmt_msg_list ])
    balloon += "\n" + hor_border
    balloon += "\n" + ("|/" if left_tail else balloon_max_size * " " + "\|")
    return balloon

def balloon(message, max_width=BALLOON_MAX_WIDTH, ver_border_chr="|", hor_border_chr="-", left_tail=False):
    fmt = balloonFormat(message,max_width)
    return balloonFromFmt(fmt,ver_border_chr,hor_border_chr,left_tail)

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        print balloon(sys.argv[1])
