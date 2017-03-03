from flask import Flask, request
import requests
import sys

app = Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/export', methods=['GET'])
def pkktranslate():
    pkkpath = 'http://pkk5.rosreestr.ru/arcgis/rest/services/Cadastre/Cadastre/MapServer/export'
    para = {
        'layers' : request.args.get('layers'),
        'FORMAT' : request.args.get('FORMAT'),
        'TRANSPARENT' : request.args.get('TRANSPARENT'),
        'DPI' : request.args.get('DPI'),
        'F' : request.args.get('F'),
        'SIZE' : request.args.get('SIZE'),
        'MAXZOOM' : request.args.get('MAXZOOM'),
        'OPACITY' : request.args.get('OPACITY'),
        'BBOXSR' : request.args.get('BBOXSR'),
        'IMAGESR' : request.args.get('IMAGESR'),
        'bbox' : request.args.get('bbox')
    }
    r = requests.get(pkkpath, params=para)
    print(r.text, file=sys.stderr)
    return r.text

if __name__ == '__main__':
    app.run()
