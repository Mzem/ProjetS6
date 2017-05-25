#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys, os
import argparse
import webbrowser
from interface_web.gestionFlux import app

parser = argparse.ArgumentParser(description="Uploadr")
parser.add_argument(
    "--port", "-p",
    type=int,
    help="Port to listen on",
    default=2006,
)
args = parser.parse_args()

# Fonction main
if __name__ == '__main__':
    flask_options = dict(
        debug=False,
        port=args.port,
        threaded=True,
    )
    webbrowser.open_new('http://127.0.0.1:2006/')
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(**flask_options)

