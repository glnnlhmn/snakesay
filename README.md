# Getting Started With Developing
#### Everyday Project Packaging With pyproject.toml

This is the code conversation between Ian Currie and Geir Arne Hjelle from [Real Python](https://realpython.com).  ~~The first 3 recordings are available for free the remained does require a paid subscription.~~  They have realeasd the [enitre video](https://www.youtube.com/watch?v=v6tALyc4C10) for free on youtube!


## 1. Introduction
I will attempt to create and tag a release in this project at the end of each video. I recommend you follow their videos and only peek at my code if you get stuck.

## 2. Index

| Video                                                                                                                             | Description                             | Tag      |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|----------|
| [Overview](https://realpython.com/lessons/packaging-with-pyproject-toml-overview/)                                                | Introduction to the code conversation   | None     |
| [Getting Started With Developing](https://realpython.com/lessons/getting-started-with-developing/)                                | Setting up the project                  | [v0.1.0] |
| [Initially Structuring Your Project](https://realpython.com/lessons/initially-structuring-your-project/)                          | Create initial project structure        | [v0.2.0] |
| [Identifying Issues With the Current Structure](https://realpython.com/lessons/adding-dependencies/)                              | Identify issue with python path         | None     |
| [Changing How You Import](https://realpython.com/lessons/changing-how-you-import/)                                                | Local/absolute import                   | [v0.3.0] |
| [Recognizing How the Structure Still Isn't Ideal](https://realpython.com/lessons/structure-still-isnt-ideal/)                     | Identify new issue with python path     | None     |
| [Playing on the Same Team as the Import System](https://realpython.com/lessons/same-team-as-import-system/)                       | Benefits of Pip to install              | None     |
| [Delving Into a Brief History of Python Packaging](https://realpython.com/lessons/history-of-python-packaging/)                   | history Lesson                          | None     |
| [Writing Your First pyproject.toml](https://realpython.com/lessons/your-first-pyproject-toml/)                                    | Create blank pyproject.toml             | [v0.4.0] |
| [Introducing the pyproject.toml Spec](https://realpython.com/lessons/pyproject-toml-spec/)                                        | Add pep index to README.md              | [v0.5.0] |
| [Including a Build System](https://realpython.com/lessons/including-a-build-system/)                                              | Add build system to pyproject.toml      | [v0.6.0] |
| [Adding Final Configurations to Your Project](https://realpython.com/lessons/final-project-configurations/)                       | Add project to pyproject.toml           | [v0.7.0] |
| [Installing Your Project](https://realpython.com/lessons/installing-your-project/)                                                | python -m pip install -e .              | None     |
| [Using the Project Anywhere](https://realpython.com/lessons/using-the-project-anywhere/)                                          | pDemo various ways to use snakesay      | None     |
| [Adding a Command Script](https://realpython.com/lessons/adding-a-command-script/)                                                | Add project.scripts to pyproject.toml   | [v0.8.0] |
| [Using the Name-Main Idiom](https://realpython.com/lessons/using-the-name-main-idiom/)                                            | Removing the second snake               | [v0.9.0] |
| [Understanding the Adoption of pyproject.toml](https://realpython.com/lessons/adoption-of-pyproject-toml/)                        | Discussion                              | None     |
| [Extra: Understanding What an Egg Is](https://realpython.com/lessons/what-an-egg-is/)                                             | Discussion of egg, wheels, and metadata | None     |
| [Everyday Project Packaging With pyproject.toml (Summary)](https://realpython.com/lessons/packaging-with-pyproject-toml-summary/) | Review                                  | [v1.0.0] |

I hope you find this useful and if you have any questions please feel free to ask. All credit for the information goes to Ian Currie and Geir Arne Hjelle from [Real Python](https://realpython.com).

## 3. Referenced PEPs
| PEP                                          | Description                                                      |
|----------------------------------------------|------------------------------------------------------------------|
| [PEP-427](https://peps.python.org/pep-0427/) | The Wheel Binary Package Format 1.0                              |
| [PEP-440](https://peps.python.org/pep-0440/) | Version Identification and Dependency Specification              |
| [PEP-508](https://peps.python.org/pep-0508/) | Dependency specification for Python Software Packages            |
| [PEP-517](https://peps.python.org/pep-0517/) | A build-system independent format for source trees               |
| [PEP-518](https://peps.python.org/pep-0518/) | Specifying Minimum Build System Requirements for Python Projects |
| [PEP-621](https://peps.python.org/pep-0621/) | Storing project metadata in pyproject.toml                       |
| [PEP-660](https://peps.python.org/pep-0660/) | Editable installs for pyproject.toml based builds (wheel based)  |

## 4. Referenced Links
| Link                                                         | Description                 |
|--------------------------------------------------------------|-----------------------------|
| [Python Packaging User Guide](https://packaging.python.org/) | Python Packaging User Guide |
| [Python Packaging Authority](https://www.pypa.io/en/latest/) | Python Packaging Authority  |
| [Setup Tools](https://setuptools.pypa.io/en/latest/)         | Setup Tools Documentation   |

#### Notes
I added README.md to the project to make it easier to find the videos.  I also added a .gitignore file to ignore files not needed in the [GitHub](https://github.com/glnnlhmn/snakesay) Repo.
