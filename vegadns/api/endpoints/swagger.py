import os
import sys
import json

from flask import Flask

from vegadns.api import endpoint
from vegadns.api.endpoints import AbstractEndpoint


@endpoint
class Swagger(AbstractEndpoint):
    auth_required = False
    route = '/swagger'

    def get(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        swagger_file = this_dir + "/../../../swagger/vegadns.swagger.json"

        with open(swagger_file) as template:
            contents = template.read()

        body = json.loads(contents)

        return body