import os
import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application

from motor import motor_tornado

from views import BaseView, RolesHandler

PORT = int(os.environ.get("PORT", 80))


class MainHandler(BaseView):
    def get(self):
        self.write(
            json.dumps(
                "Olá galera da Python Brasil 2019! "
                "Para ver os rolês faça requisições para '/roles'"
            )
        )


def main():
    MONGO_URL = os.environ.get("MONGO_URL")

    client = motor_tornado.MotorClient(MONGO_URL, retryWrites=False)
    db = client.test

    app = Application([("/", MainHandler), ("/roles", RolesHandler)], db=db)

    http_server = HTTPServer(app)
    http_server.listen(PORT)
    IOLoop.current().start()


if __name__ == "__main__":
    main()
