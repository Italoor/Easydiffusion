from easydiffusion import model_manager, app, server
from easydiffusion.server import server_api, flask # required for uvicorn

# Init the app
model_manager.init()
app.init()
server.init()
flask.run()

# start the browser ui
app.open_browser()
