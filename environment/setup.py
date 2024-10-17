'''
author name  : Rupesh Garsondiya
github       : @Rupeshgarsondiya
Organization : L.J University
'''
from setuptools import  setup, find_packages

setup(
    name='project-1',  # project name
    version='1.0',  # version number
    description='Classify user behavior based on mobile data',  # description of the project
    packages = find_packages(),  # find all packages
    author='Rupesh-Garsondiya' ,# author of the package
    author_email='rupeshgarsondiya@gmail.com', # email of the author
    url='https://github.com/Rupeshgarsondiya/Project-1.git', # url of the project
    install_requires=['pandas', 'numpy', 'sklearn', 'matplotlib'],
    # list of the dependencies required by the package
    classifiers=['Programining Language :: python :: 3.12.3']
)




