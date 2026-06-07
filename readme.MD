### AI Document Generator

#### How to run this project?

#### Please follow the following steps.

#### frontend folder is the user interface.

#### backend folder contains the ai agents which communicate with gpt mini 4o model and the flask api which integrates both the frontend and agents.

#### To run the backend

#### Create a new virtual environment using the command `python3 -m venv <env_name>`

#### active the virtual environment using the command `env_name\scripts\activate`, the command might be a bit different but most of the part should be similar.

#### run pip install -r requirements.txt

#### Please add openai key with the following key value pair

#### OPENAI_API_KEY = "open-ai-key"

#### run python app.py

#### To run frontend

#### Install react scripts in frontend folder using npm i (Please install node as it is a pre requisite for this)

#### Run npm start

#### The above command should open a webpage on port 3000

#### Please add some python code in the editor and click on generate documentation.

#### As the agents communicate with each other and the openai model, generating the documentation takes some time. Please wait patiently.


