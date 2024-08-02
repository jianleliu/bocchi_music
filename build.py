"""python build.py to run.
install inno setup first.

"""
import os
import subprocess

ICON = os.path.join(os.getcwd(), 'resource', 'images', 'logo.ico')
NAME = 'bocchi music'
RESOURCE_PATH = os.path.join(os.getcwd(), 'resource')
ENTRY = os.path.join(os.getcwd(), 'main.py')
ISS_FILE_PATH = os.path.join(os.getcwd(), 'comp_script.iss')
ISCC_PATH = r'C:\Program Files (x86)\Inno Setup 6\ISCC.exe'


def compile_iss_script(iss_path: str, compiler_path: str = ISCC_PATH) -> None:
    """compile iss script to a setup.exe

    Args:
        iss_path (str): path for the iss script file.
        compiler_path (str, optional): compiler path. Defaults to ISCC_PATH.

    Raises:
        FileNotFoundError: _description_
    """
    if not os.path.isfile(iss_path):
        raise FileNotFoundError(f"The script file {iss_path} does not exist.")

    # Command to run Inno Setup Compiler
    command = [compiler_path, iss_path]

    try:
        # Run the command
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Compilation succeeded.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Compilation failed.")
        print(e.stderr)


subprocess.run(
    ['pyinstaller', '--noconfirm', '--onedir', '--windowed', f'--icon={ICON}', f'--name={NAME}',
     '--clean', f'--add-data={RESOURCE_PATH};resource', ENTRY],
    check=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Path to your .iss script
iss_script_path = os.path.join(os.getcwd(), 'comp_script.iss')
compile_iss_script(iss_script_path)
