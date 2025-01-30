'''
 The setup.py is an essential part of packaging Python projects. 
 It is a script that helps to define the metadata for the project, such as the name, version, and dependencies.
 It also provides a way to install the project using the `pip` package manager.
 It is typically used in conjunction with the `setup.cfg` file to define additional project settings.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    This function reads the requirements.txt file and returns a list of dependencies.
    '''
    requirements: List[str] = []
    try:
        with open("requirements.txt", "r") as f:
            # Read the requirements.txt file and split the lines into a list of dependencies
            lines = f.readlines()
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#") and line != '-e .':  
                    requirements.append(line) 

    except FileNotFoundError:
        print("Requirements file not found.")

    return requirements

setup(
    name= "Network_Security",
    version= "0.1",
    packages= find_packages(),
    install_requires= get_requirements(),

)