import os, subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
 try:
    absolute_path = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(absolute_path, file_path))
    valid_target_dir = os.path.commonpath([full_path, absolute_path]) == absolute_path
   

    if not valid_target_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", full_path]
    if args:
        command.extend(args)
    result= subprocess.run(command,cwd=absolute_path,capture_output=True,text=True,timeout=30)
    return_string = ""
    if result.returncode !=0:
        return_string += f"Process exited with code {result.returncode}"
    if not result.stderr and not result.stdout:
        return_string += "No output produced"
    else:
        return_string += f"STDOUT: {result.stdout} STDERR: {result.stderr}"
    return return_string
 except Exception as e:
     return f"Error: {e}"

