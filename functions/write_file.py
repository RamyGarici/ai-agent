import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
 try:
    absolute_path = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(absolute_path, file_path))
    valid_target_file = os.path.commonpath([full_path, absolute_path]) == absolute_path
    if not valid_target_file:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if  os.path.isdir(full_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    os.makedirs( os.path.dirname(full_path),exist_ok=True)
    with open(full_path,"w") as f:
        f.write(content)
        return  f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
 except Exception as e:
    return f"Error: {e}"