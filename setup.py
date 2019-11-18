from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "main",
    version = "0.1",
    description = "Configuration network",
    executables = [Executable("main.py")],
)