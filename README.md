A two step application that gathers github programming language data from an API search call and returns it in a visual form within a nodejs server.

Requires python3, pip, virtualenv and nodejs to run.

To run data gatherer (Note that remote database is already populated with default configurations in /dataGatherer/config.json, skip to step 4 for website):

1. Navigate to /dataGatherer

2. run "$ bash installDepenciesAndBuild.sh" in sudo mode

3. run "$ bash executeDataGatherer.sh"

4. navigate to frontend-server

5. run "$ npm install" to install depencies required by package.json

6. use "$ npm start" to run the SERVER

7. Navigate to "localhost" in your browser to view graphically rendered search results from step 3.

NOTE: You may have to run "$ sudo npm start" in step 6 as superuser permissions may be required for port 80. If you wish to kill whatever process is alive on 80 if npm is being blocked, run "$ sudo fuser -k 80/tcp" or disable apache2.service if it is running on your machine.

Manipulate values in /dataGatherer/config.json to write to your own firebase db
