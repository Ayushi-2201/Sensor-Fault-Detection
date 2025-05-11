from setuptools import setup, find_packages
from typing import List


def get_requirements (file_path: str) -> List[str]:
    """
    (file_path: str): A parameter to get the path of the requirements file with a hint of type of parameter.
    -> List[str] : A return type hint of the function which tells that the function will return a list of strings.
    This function will return the list of requirements
    """
    requirements = []
    # open file file_path and store it in the variable file_obj
    with open(file_path) as file_obj:

        # read all the lines of the file and store it in the variable requirements
        requirements = file_obj.readlines()

        # remove the new line character from each line of the file and store it in the variable requirements
        requirements = [req.replace("\n", "") for req in requirements]
        # List comprehension: [... for req in requirements]
        # req: Each line from the file (like 'numpy\n')
        # replace("\n", ""): Removes newline characters (\n)
        # This results in: ['numpy', 'pandas', '-e .']
    
        # if -e . is present in the requirements list then remove it from the list
        #  -e . means: “install this package (current directory) in editable mode
        if '-e .' in requirements:
            requirements.remove('-e .')


    return requirements
 
# This function tells the metadata about the package
setup(
    name="Sensor Fault Detection",
    version="0.0.1",
    author="Ayushi Goel",
    author_email="goelayushi101@gmail.com",
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages(),       # This is an inbuilt function which will find all the packages in the current directory and return them as a list.
) 