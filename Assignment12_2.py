import os;
import sys;
import psutil;

def main():
    if sys.argv[1]:
        for pobj in psutil.process_iter():
            if pobj.name()==sys.argv[1]:
                print(pobj);


if __name__ == "__main__":
    main();