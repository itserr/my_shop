# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cart.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncart.proto\x12\x04shop\"\x1e\n\x0b\x43\x61rtRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1f\n\x0c\x43\x61rtResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2>\n\x0b\x43\x61rtService\x12/\n\x04\x43\x61rt\x12\x11.shop.CartRequest\x1a\x12.shop.CartResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cart_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CARTREQUEST']._serialized_start=20
  _globals['_CARTREQUEST']._serialized_end=50
  _globals['_CARTRESPONSE']._serialized_start=52
  _globals['_CARTRESPONSE']._serialized_end=83
  _globals['_CARTSERVICE']._serialized_start=85
  _globals['_CARTSERVICE']._serialized_end=147
# @@protoc_insertion_point(module_scope)
