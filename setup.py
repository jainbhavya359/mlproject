from setuptools import find_packages, setup
from typing import List

HYPEN_dot='-e .'

def get_requirements(file_path:str)->List:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","") for req in requirements]

        if HYPEN_dot in requirements:
            requirements.remove(HYPEN_dot)


setup(
    name='MLProject',
    version='0.0.1',
    author='Bhavya',
    author_email='jainbhavya359@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)