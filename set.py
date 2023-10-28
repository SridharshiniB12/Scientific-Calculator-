from cx_Freeze import setup,Executable,sys
includefiles=['calculator.ico']
excludes=[]
packages=[]
base=None
if sys.platform=="win32":
    base="Win32GUI"

shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "Scientific Calculator",
     "TARGETDIR",
     "[TARGETDIR]\Calci.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data={"Shortcut":shortcut_table}

bdist_msi_options={'data':msi_data}
setup(
    version="0.1",
    description="Scientific Calculator",
   
    name="Scientific Calculator",
    options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="Calci.py",
            base=base,
            icon='calculator.ico',
        )
    ]
)