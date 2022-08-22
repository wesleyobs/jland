from templateframework.metadata import Metadata
import pathlib, os, shutil


def run(metadata: Metadata = None):
    compilation_tool = metadata.inputs.get("compilation_tool")
    source_path = absolute_path(number_levels_to_go_back=1)
    destination_path = current_path() + "/" + metadata.inputs.get("project_name")
    print(destination_path)
    if compilation_tool == "Gradle":
        copy_folder(source_path + "/gradle", destination_path)
    elif compilation_tool == "Maven":
        copy_folder(source_path + "/maven/", destination_path)
    return metadata


def absolute_path(number_levels_to_go_back=0):
    return str(pathlib.Path(__file__).parents[number_levels_to_go_back])


def current_path():
    return str(os.getcwd())


def copy_folder(source, target):
    shutil.copytree(source,
                    target,
                    symlinks=False,
                    ignore=None,
                    ignore_dangling_symlinks=False,
                    dirs_exist_ok=True
                    )
