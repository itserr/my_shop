# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nauth.proto\x12\x04shop\"\x1e\n\x0b\x41uthRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0c\x41uthResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2H\n\x15\x41uthenticationService\x12/\n\x04\x41uth\x12\x11.shop.AuthRequest\x1a\x12.shop.AuthResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_AUTHREQUEST']._serialized_start=20
  _globals['_AUTHREQUEST']._serialized_end=50
  _globals['_AUTHRESPONSE']._serialized_start=52
  _globals['_AUTHRESPONSE']._serialized_end=83
  _globals['_AUTHENTICATIONSERVICE']._serialized_start=85
  _globals['_AUTHENTICATIONSERVICE']._serialized_end=157
# @@protoc_insertion_point(module_scope)
