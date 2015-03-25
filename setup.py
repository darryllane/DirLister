from distutils.core import setup

setup(
    name='DirLister',
    version='1.0.0',
    author='Darryl lane',
    author_email='DarrylLane101@gmail.com',
    packages=['DirLister', 'DirLister'],
    url='https://bitbucket.org/laned/dirlist.git',
    license='LICENSE.txt',
    description='Detects NetBIOS Spoofing attacks, has counter mesasures and logs data to syslog',
    long_description=open('README.md').read(),
    scripts=['DirLister/DirLister.py'],
    install_requires=[
        "docopt",
    ],
)
