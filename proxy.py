from __future__ import print_function
import sys, os
from tempodb.client import Client
from flask import Flask, request, Response
app = Flask(__name__)

for k in ['TEMPODB_DATABASE_ID', 'TEMPODB_API_KEY',
          'TEMPODB_API_SECRET']:
    if k not in os.environ:
        print("Missing environment variable: {}".format(k),
              file=sys.stderr)
        sys.exit(1)

client = Client(os.environ['TEMPODB_DATABASE_ID'],
                os.environ['TEMPODB_API_KEY'],
                os.environ['TEMPODB_API_SECRET'])

# From http://gear11.com/2013/12/python-proxy-server/
CHUNK_SIZE = 1024
def convert_response(r):
    headers = dict(r.headers)
    def generate():
        for chunk in r.iter_content(CHUNK_SIZE):
            yield chunk
    return Response(generate(), headers=headers)

@app.route('/tempodb/<path:path>')
def proxy_get(path):
    response = client.session.get(path + '?' + request.query_string)
    return convert_response(response)

if __name__ == '__main__':
    app.run()
