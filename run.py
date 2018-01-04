import grpc
from protos import chat_pb2
from protos import chat_pb2_grpc

# print(dir(chat_pb2))
channel = grpc.insecure_channel('52.166.241.153:6262')
stub = chat_pb2_grpc.ChatStub(channel)
login_resp = stub.Login(
    chat_pb2.LoginRequest(
        name='morse-bot',
        password='super-secret',
    )
)

print(login_resp.token)
# print(repr(login_resp))

print(dir(login_resp))

stream = stub.Stream(
    iter([chat_pb2.StreamRequest(
        message='message from morse-bot',
        # message=login_resp.token,
    )]),
    metadata=[
        ('tokenHeader', login_resp.token),
    ],
)

# print(dir(stream)

# for each in stream:
#     print(each)


# stream.
print(stream)
# for each in stream:
#     print(each)
# print(response)

