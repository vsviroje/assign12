import os;
import sys;
import psutil;

def main():
    for pobj in psutil.process_iter():
        print(pobj);


if __name__ == "__main__":
    main();