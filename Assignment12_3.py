import os;
import sys;
import psutil;
import time;
def main():
    if sys.argv[1]:
        if not os.path.exists(sys.argv[1]):
            os.mkdir(sys.argv[1]);

        filename = os.path.join(sys.argv[1], "log%s.txt" % time.ctime());
        line = "~" * 40;
        fobj = open(filename, 'w');
        fobj.write(line + "\n");

        for pobj in psutil.process_iter():
            fobj.write("Username->"+str(pobj.username())+" PID->"+str(pobj.pid)+" Name->"+str(pobj.name())+"\n");
            fobj.write(line + "\n");

if __name__ == "__main__":
    main();