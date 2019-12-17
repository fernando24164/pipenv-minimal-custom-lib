# from distutils.core import setup, Extension
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

print_message_class = Extension(
    name="test", sources=["./print_json.pyx"], include_dirs=["./config"]
)

setup(
    name="pipenv_test",
    version="0.0.1",
    description="Test with cython",
    ext_modules=cythonize(print_message_class),
    data_files=[("config/config.json")],
    include_package_data=True,
    package_data={'config': ['config.json']},
)
