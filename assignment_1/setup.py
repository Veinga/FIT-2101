import cx_Freeze
import sys
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\JEEVAN\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\JEEVAN\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("marking_software.py",base=base,icon="markiv.ico")]

cx_Freeze.setup(
    name = "Testing-Name",
    options = {"build_exe": {"packages":["tkinter", "PIL"],"include_files":["C:/Users/JEEVAN/AppData/Local/Programs/Python/Python36-32/DLLs/tcl86t.dll","markiv.ico", "mark_iv.png","monash-university-malaysia.png", "C:/Users/JEEVAN/AppData/Local/Programs/Python/Python36-32/DLLs/tk86t.dll"]}},
    version = "0.01",
    description = "This is a test description",
    executables = executables
    )
