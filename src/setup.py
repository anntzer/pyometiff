from setuptools import setup

setup(
      name="pyometiff",
      version="0.0.1",
      description="Read and Write OME-TIFFs in Python",
      py_modules = ["omereader", "omewriter", "omexml"],
      package_dir = {"": "src"},
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
          # "Operating System :: Os Independent",
          ],
      )