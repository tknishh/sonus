from __future__ import annotations
from cx_Freeze import Executable, setup

setup(
    name="sonus",
    version="v2.0.1",
    description="sonus GUI",
    executables=[Executable("main.py", icon="icon.ico", target_name="sonus.exe")],
    options={
        "build_exe": {
            "include_files": [("icon.png")],
            "zip_include_packages": ["env/"],
            "zip_exclude_packages": []
        }
    },
)