#
Just a little self study
## Set up virtual env
```
sudo yum install python-virtualenv
mkdir venv
echo "venv" > .gitignore
git add .gitignore
virtualenv -p python3 venv/
. venv/bin/activate
pip install -r requirements.txt
```