#!/usr/bin/env python
import setuptools

# d2to1 basically installs itself!  See setup.cfg for the project metadata.
import d2to1.util


setuptools.setup(**d2to1.util.cfg_to_args())
