# Detailed solution 

[-0]: https://tom.preston-werner.com/2010/08/23/readme-driven-development.html "Readme Driven Development"
[-1]: https://choosealicense.com/licenses/ "Choose a License"
[-2]: https://semver.org/ "Semantic Versioning"
[-3]: https://www.conventionalcommits.org/en/v1.0.0/ "Conventional Commits"
[-4]: https://keepachangelog.com/en/1.0.0/ "Keep a Changelog"
[-5]: https://www.repostatus.org "Repo status"
[-6]: https://en.wikipedia.org/wiki/Don't_repeat_yourself "Don't repeat yourself"
[-7]: https://12factor.net/ "Twelve-factor app"

[>1]: https://git-scm.com/ "Git"
[>2]: https://www.gnu.org/software/make/ "GNU Make"
[>3]: https://www.jetbrains.com/pycharm/ "PyCharm"
[>4]: https://github.com "Github"
[>5]: https://en.wikipedia.org/wiki/Markdown "Markdown"
[>6]: https://www.mkdocs.org/ "Mkdocs"


## Convention compliance
This project was developed taking into account the following standards:

### Repository maintenance
* [Readme Driven Development][-0]
* [Choose a License][-1]
* [Semantic Versioning][-2]
* [Conventional Commits][-3]
* [Keep a Changelog][-4]
* [Repo status][-5]

### Development guidelines
* [Don't repeat yourself][-6]
* [Twelve-factor app][-7]


## Used technologies
The next technologies were used during project conception, development, test or deploy: 

### Development tools
* [Git][>1] for code versioning control
* [Make][>2] for development process management
* [PyCharm][>3] as integrated development environment
* [Github][>4] for code integration management

### Documentation aparatus
* [Markdown][>5] for text formatting
* [Mkdocs][>6] as static site generator


## Project specifications
Here some descriptions about this project:

### Folder structure
```
.
├── .git/                       Version control system folder
├── .gitignore                  VCS ignored files manifest
├── CHANGELOG.md                Release notes description
├── LICENSE                     License file
├── Makefile                    Development management facilities
├── README.md                   Repo readme document

└── data/
    └── img/                    Project level images

└── docs/                       Documentation root folder
    ├── mkdocs.yml              MkDocs configuration file  
    └── pages/                  
        ├── challenge.pdf       Original challenge description
        ├── index.md            Documentation home page
        ├── management.md       Development management summary
        ├── setup.md            Application setup instructions
        └── solution.md         Detailed solution report
```
