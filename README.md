
## Exercise:
Create a Google Workspace Plugin that does the following

- When a user is composing an email, the Add On captures the following info
	- To, CC, Bcc recipients
	- Subject of the message
	- Text of the message

- Add On Sends this information as an API call to a backend server.

- In Response to the above API call(s) Add On receives a JSON payload with text to display to the user.
- Display this text in the gmail interface to the user as a card

## Deliverables
- Complete code for the plugin

- Written instructions to set up the plugin in dev mode on the testers machine

## Desired Results:
- Successfully execute the desired functionality


## Instructions

Download the git repo https://github.com/vivekuppal/gmail-add-on-takehome.git locally

```
python -m venv venv
```
activate the venv - This instruction is specific to win or linux or mac

```
pip install -r requirements.txt
```

Run the server hosting the API

```
uvicorn app.main:app --reload --port 8080
```

Sample request to API

```
curl -X POST "http://127.0.0.1:8080/analyze_simple" -H "Content-Type: application/json" -H "X-API-Key: dev-secret" --data-binary "@payload.json"
```

You will have to use ngrok (or something similar) to expose the localservice to public internet through a secure tunnel. Without this gmail servers would not be able to see you service running locally.
```
ngrok http 8080
```

For your submission, please zip a copy of the folder with changes and send that over. Do not include the virtual env files in the submission.
