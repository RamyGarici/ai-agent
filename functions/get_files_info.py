import os
from google.genai import types

def get_files_info(working_directory: str, directory: str = ".") -> str:
 try:
    absolute_path = os.path.abspath(working_directory)
    full_path = os.path.normpath(os.path.join(absolute_path, directory))
    valid_target_dir = os.path.commonpath([full_path, absolute_path]) == absolute_path
   

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory' 
    
    results = []
    for item in os.listdir(full_path):
       results.append(f"{item}: file_size={os.path.getsize(os.path.join(full_path,item))} bytes, is_dir={os.path.isdir(os.path.join(full_path,item))}")
    return "\n".join(results)
   
 




 except Exception as e:
    return f"Error: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
      
    ),
)




