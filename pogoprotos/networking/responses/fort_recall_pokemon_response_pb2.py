# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/fort_recall_pokemon_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.networking.responses import fort_details_response_pb2 as pogoprotos_dot_networking_dot_responses_dot_fort__details__response__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/fort_recall_pokemon_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nBpogoprotos/networking/responses/fort_recall_pokemon_response.proto\x12\x1fpogoprotos.networking.responses\x1a;pogoprotos/networking/responses/fort_details_response.proto\"\xb0\x02\n\x19\x46ortRecallPokemonResponse\x12Q\n\x06result\x18\x01 \x01(\x0e\x32\x41.pogoprotos.networking.responses.FortRecallPokemonResponse.Result\x12J\n\x0c\x66ort_details\x18\x02 \x01(\x0b\x32\x34.pogoprotos.networking.responses.FortDetailsResponse\"t\n\x06Result\x12\x11\n\rNO_RESULT_SET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x16\n\x12\x45RROR_NOT_IN_RANGE\x10\x02\x12\x1d\n\x19\x45RROR_POKEMON_NOT_ON_FORT\x10\x03\x12\x13\n\x0f\x45RROR_NO_PLAYER\x10\x04\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_networking_dot_responses_dot_fort__details__response__pb2.DESCRIPTOR,])



_FORTRECALLPOKEMONRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.FortRecallPokemonResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_RESULT_SET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NOT_IN_RANGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_POKEMON_NOT_ON_FORT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR_NO_PLAYER', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=353,
  serialized_end=469,
)
_sym_db.RegisterEnumDescriptor(_FORTRECALLPOKEMONRESPONSE_RESULT)


_FORTRECALLPOKEMONRESPONSE = _descriptor.Descriptor(
  name='FortRecallPokemonResponse',
  full_name='pogoprotos.networking.responses.FortRecallPokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.FortRecallPokemonResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_details', full_name='pogoprotos.networking.responses.FortRecallPokemonResponse.fort_details', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FORTRECALLPOKEMONRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=165,
  serialized_end=469,
)

_FORTRECALLPOKEMONRESPONSE.fields_by_name['result'].enum_type = _FORTRECALLPOKEMONRESPONSE_RESULT
_FORTRECALLPOKEMONRESPONSE.fields_by_name['fort_details'].message_type = pogoprotos_dot_networking_dot_responses_dot_fort__details__response__pb2._FORTDETAILSRESPONSE
_FORTRECALLPOKEMONRESPONSE_RESULT.containing_type = _FORTRECALLPOKEMONRESPONSE
DESCRIPTOR.message_types_by_name['FortRecallPokemonResponse'] = _FORTRECALLPOKEMONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FortRecallPokemonResponse = _reflection.GeneratedProtocolMessageType('FortRecallPokemonResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORTRECALLPOKEMONRESPONSE,
  __module__ = 'pogoprotos.networking.responses.fort_recall_pokemon_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.FortRecallPokemonResponse)
  ))
_sym_db.RegisterMessage(FortRecallPokemonResponse)


# @@protoc_insertion_point(module_scope)