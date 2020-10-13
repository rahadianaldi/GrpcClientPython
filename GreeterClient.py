import grpc
import greet_pb2_grpc as pb2_grpc
import greet_pb2 as pb2
# import socket
# import ssl


class GreetClient(object):
    """
    Client for gRPC functionality
    """
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 5001

        # with open("MyCertificate.crt", "rb") as file:
        #     cert = file.read()
        # credentials = grpc.ssl_channel_credentials(cert)

        # instantiate a channel
        self.channel = grpc.insecure_channel("localhost:5001")

        # bind the client and the server
        self.stub = pb2_grpc.GreeterStub(self.channel)

    def get_list_mahasiswa(self):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.empty()
        print(f'{message}')
        res = {}
        lst = []
        rslt = self.stub.GetListMahasiswa(message)
        for mhs in rslt.mahasiswa:
            ls = {'nama': mhs.nama, 'nim': mhs.nim,
                  'asal': mhs.asal, 'datebirth': mhs.datebirth}

            lst.append(ls)
        res["result"] = lst
        return res

    def get_detail_mahasiswa(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.ID(id=message)
        print(f'{message}')
        mhs = self.stub.DetailMahasiswa(message)
        res = {'nama': mhs.nama, 'nim': mhs.nim,
               'asal': mhs.asal, 'datebirth': mhs.datebirth}
        return res

    def insert_mahasiswa(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Mahasiswa(nama=message["nama"], nim=message["nim"],
                                asal=message["asal"], datebirth=message["datebirth"])
        print(f'{message}')
        mhs = self.stub.InsertMahasiswa(message)
        res = mhs.txt
        return res

    def edit_mahasiswa(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Mahasiswa(nama=message["nama"], nim=message["nim"],
                                asal=message["asal"], datebirth=message["datebirth"])
        print(f'{message}')
        mhs = self.stub.EditMahasiswa(message)
        res = mhs.txt
        return res

    def delete_mahasiswa(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.ID(id=message)
        print(f'{message}')
        mhs = self.stub.DeleteMahasiswa(message)
        res = mhs.txt
        return res


# if __name__ == '__main__':
#     # context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#     # context.load_cert_chain('cert.pem', 'key.pem')
#     #
#     # with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
#     #     sock.bind(('127.0.0.1', 8443))
#     #     sock.listen(5)
#     #     with context.wrap_socket(sock, server_side=True) as ssock:
#     #         conn, addr = ssock.accept()
#
#     client = GreetClient()
#     result = client.get_list_mahasiswa()
#     print(f'{result}')
