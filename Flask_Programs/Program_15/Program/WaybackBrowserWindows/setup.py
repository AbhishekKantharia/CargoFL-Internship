import sys
from cx_Freeze import Executable, setup

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("waybackbrowser.py", base=base)]

setup(
    name="Wayback Browser",
    version="1.0",
    description="Wayback Browser",
    executables=executables,
    includes = ['jinja2.ext'],
    options={"build_exe":{"packages":[],
                      "include_files":['templates\loadpage.html', 'home.png', 'logo.png', 'reload.png', 'back.png', 'forward.png', 'templates', 'templates\home.html', 'server.py']}},
)
