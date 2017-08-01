#!/usr/bin/env python
 encoding: utf-8
from app import generate_app , app
import sys

if __name__ == '__main__' :
    app = generate_app(app)
    port = input(">port(between 3001 and 9999):")
    if port not in  range(3001,10000) :
        print("Error:port should between 3001 and 9999!")
        sys.exit(0)
    app.run(port=port,host='0.0.0.0')
