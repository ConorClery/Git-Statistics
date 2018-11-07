chmod -R 775 installDependenciesAndBuild.sh
chmod -R 775 executeDataGatherer.sh
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
