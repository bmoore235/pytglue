from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pytglue',
    version='1.0.2',
    description='An Unofficial Python Wrapper for ITGlue.',
    py_modules=["pytglue"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
