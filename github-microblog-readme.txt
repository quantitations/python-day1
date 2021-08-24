
conda deactivate

[here we'll demonstrate a good pattern that enables you to run other people's python programs:
clone code, create virtual environment, install requirements]

[if you have git command line installed on your computer:]
[click "clone" at https://github.com/miguelgrinberg/microblog then copy link, then]
git clone https://github.com/miguelgrinberg/microblog.git

[otherwise: download the zip file]

conda create --name microblog python=3.7.9

conda activate microblog

pip install -r requirements.txt

flask db upgrade
[only need to run that once to create the database]

flask run

[you may need to install and configure additional software including "elasticsearch" to get this program to work -- see tutorial:]
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
