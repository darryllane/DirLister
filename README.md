### What is it? ###

Used to map all files and directories within a given Directory. I found it useful when trying to carry out forced browsing on open source Web Applications. Download the latest version of the relevant Web Application/CMS then DirLister the top level dir. That will give you a nice clean list of potential URLs

### Install Instructions ###

The tool requires various other dependencies. So to make things as easy as possible I have created the setup script to install the relevant dependents and the installer will also install the scripts to your /usr/local/share dir and allow you to execute the script from any command line terminal regardless of the current working dir.

**Note:**

To install the script and the dependancies you will need to use easy_install. Follow the below instructions.

**MAC**

1.Mac and Unix users can simply use the following command; 
>sudo curl https://bootstrap.pypa.io/ez_setup.py -o - | python

2.Once the setuptools/easy_install install is completed you are able to download the distribution file from [here](https://bitbucket.org/laned/dirlist/downloads/DirLister-1.0.0.tar.gz) and run the setup script using easy_install; 
>sudo easy_install DirLister-1.0.0.tar.gz

3.You can now execute the script from any terminal (you may need to close a currently open terminal and reopen it) 


**Windows**

Windows Users, its not as simple. You will need to download the zip version of the dist package. Open the zip up and remove the setup.cfg file. Your install should place the script into the relevant Python Scripts dir, normally located C:\Python2.7\Scripts.

1.Windows users use the following PowerShell command (run as admin); 
>(Invoke-WebRequest https://bootstrap.pypa.io/ez_setup.py).Content | python -

2.Once the setuptools install is completed you are able to run the setup script using easy_install (you will need to navigate to C:\PythonX.X\Scripts); 
>sudo easy_install.exe DirLister-1.0.0.tar.gz

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact