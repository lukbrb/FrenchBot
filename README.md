# FrenchBot
Discord bot scraping the Larousse website to translate words from French to German, or vice-versa . It can also conjugate verbs, or give definitions. 
These two options are available only in French.


## Installation
### Creating a virtual environment

On MacOS and Linux :
```
$ python3 -m venv venv
```

Similarly on Windows:

```
$ python -m venv venv
```

Note that in these examples we use the `venv`command from Python to create a virtual environment *called* `venv`. Any name could be chosen.

### Activate the virtual environment

MacOs and Linux :
```
$ source venv\bin\activate 
```

On Windows :

on cmd.exe
```
C:\> venv\Scripts\activate.bat
```
or using powershell :

```
PS C:\> venv\Scripts\Activate.ps1
```

### Setting up the package

Once the virtual environment created, run 

```
$ pip install .
```
to install the larousse package and its dependencies. 

Note that you will have to enter your own bot token in order to use it. Also, the Discord library used in the project is now a bit old. Therefore, using this
specific version is essential.
