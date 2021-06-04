
import setuptools
import inspect
import sys
import os

long_description = """Qiskit Glassy Dynamics is a open-source library of quantum computing glassydynamics/chemistry/physics experiments.
 """

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()

if not hasattr(setuptools, 'find_namespace_packages') or not inspect.ismethod(setuptools.find_namespace_packages):
    print("Your setuptools version:'{}' does not support PEP 420 (find_namespace_packages). "
          "Upgrade it to version >='40.1.0' and repeat install.".format(setuptools.__version__))
    sys.exit(1)

VERSION_PATH = os.path.join(os.path.dirname(__file__), "qiskit_glassydynamics", "VERSION.txt")
with open(VERSION_PATH, "r") as version_file:
    VERSION = version_file.read().strip()

setuptools.setup(
    name='QuGlassyIsing',
    version=VERSION,
    description='Qiskit Glassy Dynamics: A library of quantum computing glassydynamics/chemistry/physics experiments',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/arnavdas88/QuGlassyIsing',
    author='Qiskit Glassy Dynamics Development Team',
    author_email='arnav.das88@gmail.com; turbasu.chatterjee@gmail.com; sishmam51@gmail.com;',
    license='Apache-2.0',
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering"
    ),
    keywords='qiskit quantum glassydynamics chemistry physics',
    packages=setuptools.find_packages(include=['qiskit_glassydynamics', 'qiskit_glassydynamics.*']),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires=">=3.6",
    extras_require={
        'pyscf': ["pyscf; sys_platform != 'win32'"],
    },
    zip_safe=False
)
