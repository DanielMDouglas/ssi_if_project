from setuptools import setup, find_packages

setup(
    name='iftools',
    version='0.1',
    author='calcuttj',
    description='if project',
    packages=find_packages(),
    url='https://github.com/calcuttj/ssi_if_project',
    scripts=[],
    install_requires=['gdown','fire','h5py','torch','torch_geometric','plotly','matplotlib'],
)