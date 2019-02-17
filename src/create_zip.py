"""
Tool used for coping the needed source files and the dependencies into a zip file to be uploaded to alexa.
Currently the location of the virtual environment is hard coded in.

TODO:
    Add dynamic definition of virtual environment location
@author: Collin Bolles
"""
import os
import zipfile
import shutil
from distutils.dir_util import copy_tree


def zipdir(path, ziph):
    """
    Zip the target folder into a single file
    :param path: location of the folder to zip
    :param ziph: zip option used to write the files into the zipped directory
    :return: None
    """
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), path))


def main():
    """
    Handles creating a temporary folder to have the source code and dependencies stored in.
    Then zips the generated folder
    :return:
    """
    # Defining folders to copy
    project_dir = os.path.abspath(os.path.dirname(__file__))
    dependencies = os.path.join(project_dir, '../venv/lib/python3.6/site-packages')
    zip_folder = os.path.join(project_dir, '../alexa-project')
    zip_file = zip_folder + '.zip'

    # Make directory to zip
    shutil.rmtree(zip_folder, ignore_errors=True)
    shutil.rmtree(zip_file, ignore_errors=True)
    os.mkdir(zip_folder)

    # Copy important directories to zip
    copy_tree(project_dir, zip_folder)
    copy_tree(dependencies, zip_folder)

    # Zip output
    zipf = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    zipdir(zip_folder, zipf)
    zipf.close()


if __name__ == '__main__':
    main()