# Video Time Index 

#### Prepared by Alexandar Jelenic


| Timestamps | Comment |
|------------|----------------|
|1:40 | running the first cli using python .cli.py |
| 4:20 | create directory "snakesay" to contain project. which will be the name of the package move all files to that folder |
| 5:10 | python snakesay does not work. need __main__. but still runs using .\snakesay\cli.py |
| 6:48 | rename clip.py to _main_ |
| 7:30 | python snakesay works now, but... |
| 8:15 | if you call a folder it needs to have _main_ |
| 8:40 | python -m to call module, does not work as python looks in its path |
| 9:45 | python uses two paths, the active path, and another path of all libraries. |
| 13:45 | absolute imports " from snakesay import snake" is needed when using -m ans points to snake module explicity |
| 15:05 | now "python snakesay" does not work again due to module not found |
| 15:30 | python with -m searches for different paths to get both "python" and "python -m" both working |
| 16:00 | you should not sys.path.append(yourpath) this will work, but does not scale well. this is commonly used but is a bad practice scaling problem is that you cant share it easily and does not help you merge programs |
| 17:25 | the plan is to install the package, you will pip install, but no need to upload it anywhere you can pip install your directory. 
| 18:00 | you will be able to use consistent inports and it will work in any CWD |
| 19:00 | historical solutions |
| 20:24 | intro to setuptools. it is not part of the standard library. |
| 22:00 | most importantant PEPs on how to setup packagages historically. messy history |
| 22:50 | create a local package |
| 23:00 | create pyproject.toml one directory up all consifg can be placed here, this replaces setup.py, or setup.cfg |
| 24:20 | setuptools home page shows config setup tools using .toml,build system, project, and optional dependenace, like a dictionary |
| 25:50 | PEP 621 storing metadata in pyproject.toml |
| 26:40 | toml is not python specific, it is general |
| 27:05 | copy the build-system section from the [setuptools.pypa.io](setuptools.pypa.io/en/latest/userguide/pyproject_config.html) and paste into pyproject.toml |
| 30:44 | create "snakesay-project" and move contents into it |
| 31:40 | and move the .toml into the project folder and now install this into a virtual environment |
| 32:00 | in the project folder  python -m venv venv |
| 32:20 | for windows activate the venv by ".\venv\Scripts\activate |
| 32:50 | in the toml create the [project] name = "snakesay" version ="1.0.0" |
| 33:30 | inside the snake-project folder python -m pip install -e . to allow changes updates to the source code |
| 36:20 | "Successfull installed snakesay-1.0.0" now can can call it from anywhere using with or without the -m flag |
| 37:50 | now you can "import snakesay" in any python script when the venv is activated |
| 38:20 | now there is no reason to think about the path, or relative imports,even if deep inside you package, you can always "from snakesave import snake" |
| 38:48 | the last step, to create an entry point, so that it is recognized by the terminal. |
| 39:20 | including project scripts to create an entry point, updating the .toml |
| 41:50 | need to pip instal the pyproject as changes where made to it. |
| 42:30 | now you can go anywhere on the commange line and call your program, but now it calls the program twice |
| 43:40 | to fix you need if __name__== "__main__" in the __main__.py |4920 Flint, Poetry support .toml as well now |
| 46:35 | whats an .egg? egg is a predecceor for wheels, it contains metadata and source for editable installs. |
| 48:10 | from inportlib import metdata to see metadata on a project from an egg. gitignore egg files |
| 49:35 | summary |

