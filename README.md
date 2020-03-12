# Instalite
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codebeat badge](https://codebeat.co/badges/65446fb8-a94e-4fc2-bd6f-46329c72f163)](https://codebeat.co/projects/github-com-mutugiii-instalite-master)

## Description
A python django app that is a lite clone of the instagram web app

## User Stories
- User can post a picture with a caption
- User can comment on post
- User can View image description
- User can update profile
- User can follow other users 


# Installation

## Clone
    
```bash
    git clone https://github.com/mutugiii/Pinstagram.git
    
```
##  Create virtual environment
```bash
    pipenv shell
    
```
## Run initial migration
```bash
   $ python3.6 manage.py makemigrations instagram
   $ python3.6 manage.py migrate
    
```


## Run app
```bash
   $ python3 manage.py runserver
    
```

## Test class

```bash
    $ python3 manage.py test
```


## Contributing

To contribute, Open an issue first if it is a major contribution, for minor issues create a pull request

## Technologies
    Python 3.6
    Django
    PostgreSQL
    Cloudinary

## Author
Mutugi


## License
[LICENSE](LICENSE)


