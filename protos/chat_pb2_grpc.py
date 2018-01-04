# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protos import chat_pb2 as protos_dot_chat__pb2


class ChatStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Login = channel.unary_unary(
        '/chat.Chat/Login',
        request_serializer=protos_dot_chat__pb2.LoginRequest.SerializeToString,
        response_deserializer=protos_dot_chat__pb2.LoginResponse.FromString,
        )
    self.Logout = channel.unary_unary(
        '/chat.Chat/Logout',
        request_serializer=protos_dot_chat__pb2.LogoutRequest.SerializeToString,
        response_deserializer=protos_dot_chat__pb2.LogoutResponse.FromString,
        )
    self.Stream = channel.stream_stream(
        '/chat.Chat/Stream',
        request_serializer=protos_dot_chat__pb2.StreamRequest.SerializeToString,
        response_deserializer=protos_dot_chat__pb2.StreamResponse.FromString,
        )


class ChatServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Login(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Logout(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Login': grpc.unary_unary_rpc_method_handler(
          servicer.Login,
          request_deserializer=protos_dot_chat__pb2.LoginRequest.FromString,
          response_serializer=protos_dot_chat__pb2.LoginResponse.SerializeToString,
      ),
      'Logout': grpc.unary_unary_rpc_method_handler(
          servicer.Logout,
          request_deserializer=protos_dot_chat__pb2.LogoutRequest.FromString,
          response_serializer=protos_dot_chat__pb2.LogoutResponse.SerializeToString,
      ),
      'Stream': grpc.stream_stream_rpc_method_handler(
          servicer.Stream,
          request_deserializer=protos_dot_chat__pb2.StreamRequest.FromString,
          response_serializer=protos_dot_chat__pb2.StreamResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'chat.Chat', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))