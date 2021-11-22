# Custom Search JSON API
Utilizando API da google.  
https://developers.google.com/custom-search/v1/overview

# Credential
Create credential
- https://console.cloud.google.com/
- Left menu
- APIs and services
- Credentials
- Create credentials
- API key

Edit credential
- Click on pencil icon (Edit API key button)
- Restrict key
- Custom search API
- Save

I am going to put my API key on `.env` file from VSCode:  
`API_KEY=xxxxxxxxx`  

# Enable
Enable API
- https://console.cloud.google.com/
- Search "custom search"
- Select "Custom Search API" option
- Click "enable"

# Engine
Create an engine
- https://programmablesearchengine.google.com/cse/all
- Add

I am going to put my engine ID on `.env` file from VSCode:  
`ENGINE_ID=xxxxxxxxx`  

# example00 requirements
`pip install requests`  

# example01 requirements
`pip install google-api-python-client`  