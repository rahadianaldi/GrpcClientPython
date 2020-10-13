import json
from flask import Flask, request
from GreeterClient import GreetClient as obj

app = Flask(__name__)


@app.route('/ListMahasiswa', methods=['POST'])
def list_mhs():
    client = obj()
    res = client.get_list_mahasiswa()
    return res


@app.route('/DetailMahasiswa', methods=['POST'])
def detail_mhs():
    nim = request.args.get('nim')
    client = obj()
    res = client.get_detail_mahasiswa(nim)
    return res


@app.route('/InsertMahasiswa', methods=['POST'])
def insert_mhs():
    strjson = json.dumps(request.get_json())
    mhs = json.loads(strjson)
    print(mhs)
    client = obj()
    res = client.insert_mahasiswa(mhs)
    return res


@app.route('/EditMahasiswa', methods=['POST'])
def edit_mhs():
    strjson = json.dumps(request.get_json())
    mhs = json.loads(strjson)
    print(mhs)
    client = obj()
    res = client.edit_mahasiswa(mhs)
    return res


@app.route('/DeleteMahasiswa', methods=['POST'])
def delete_mhs():
    nim = request.args.get('nim')
    client = obj()
    res = client.delete_mahasiswa(nim)
    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
