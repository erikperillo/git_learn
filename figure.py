import balloon as bl

class Figure(object):
    def __init__(self, fig_filename, msg_shift=0.5):
        f = open(fig_filename,"r")
        self.figure = "".join([ line for line in f ])
        f.close()
        self.shift = msg_shift

    def say(self, msg, max_width=bl.BALLOON_MAX_WIDTH, ver_border_chr="|", hor_border_chr="-", left_tail=False):
        #making balloon from message
        balloon = bl.balloon(msg,max_width,ver_border_chr,hor_border_chr,left_tail)
        bal_list = balloon.replace("\r\n","\n").split("\n")
        balloon_width = max([ len(line) for line in bal_list ])
        
        fig_list = self.figure.replace("\r\n","\n").split("\n")
        fig_width = max([ len(i) for i in fig_list ])
        
        #putting balloon and self.figure in the right place
        fig_loc = int(self.shift * fig_width)
        if balloon_width > fig_loc:
            self.figure = "\n".join([ " " * (balloon_width - fig_loc) + line for line in fig_list ])
        else:
            balloon = "\n".join([ " " * (fig_loc - balloon_width) + line for line in bal_list ])
        
        print balloon + "\n" + self.figure
     

if __name__ == "__main__":
    import oarg

    #arguments
    filename = oarg.Oarg(str,"-f --filename","","Path of filename",1)
    message = oarg.Oarg(str,"-m --message","Hello my friend!","Message to display",2)
    hlp = oarg.Oarg(bool,"-h --help",False,"This help message")

    #checking for errors in parsing
    if oarg.parse() != 0:
        print "error: invalid arguments:", ", ".join([i for i in oarg.Oarg.invalid_options])
        exit(1)

    #displaying help message if required
    if hlp.getVal():
        oarg.describeArgs("Avaliable options:")
        exit()

    #checking validity of argument
    if filename.getVal() == "":
        print "you must specify a file. use '--help' for more information"
        exit()

    figure = Figure(filename.getVal(),0.8)
    figure.say(message.getVal())
