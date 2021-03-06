# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/use_item_rare_candy_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/use_item_rare_candy_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\nBpogoprotos/networking/responses/use_item_rare_candy_response.proto\x12\x1fpogoprotos.networking.responses\x1a!pogoprotos/enums/pokemon_id.proto\"\xca\x02\n\x18UseItemRareCandyResponse\x12P\n\x06result\x18\x01 \x01(\x0e\x32@.pogoprotos.networking.responses.UseItemRareCandyResponse.Result\x12/\n\npokemon_id\x18\x02 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x1b\n\x13updated_candy_count\x18\x03 \x01(\x05\"\x8d\x01\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x16\n\x12INVALID_POKEMON_ID\x10\x02\x12\r\n\tNO_PLAYER\x10\x03\x12\x13\n\x0fWRONG_ITEM_TYPE\x10\x04\x12\x19\n\x15ITEM_NOT_IN_INVENTORY\x10\x05\x12\x14\n\x10NOT_ENOUGH_ITEMS\x10\x06\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])



_USEITEMRARECANDYRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.UseItemRareCandyResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_POKEMON_ID', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_PLAYER', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_ITEM_TYPE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_NOT_IN_INVENTORY', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_ENOUGH_ITEMS', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=328,
  serialized_end=469,
)
_sym_db.RegisterEnumDescriptor(_USEITEMRARECANDYRESPONSE_RESULT)


_USEITEMRARECANDYRESPONSE = _descriptor.Descriptor(
  name='UseItemRareCandyResponse',
  full_name='pogoprotos.networking.responses.UseItemRareCandyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.UseItemRareCandyResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.networking.responses.UseItemRareCandyResponse.pokemon_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated_candy_count', full_name='pogoprotos.networking.responses.UseItemRareCandyResponse.updated_candy_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USEITEMRARECANDYRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=469,
)

_USEITEMRARECANDYRESPONSE.fields_by_name['result'].enum_type = _USEITEMRARECANDYRESPONSE_RESULT
_USEITEMRARECANDYRESPONSE.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_USEITEMRARECANDYRESPONSE_RESULT.containing_type = _USEITEMRARECANDYRESPONSE
DESCRIPTOR.message_types_by_name['UseItemRareCandyResponse'] = _USEITEMRARECANDYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UseItemRareCandyResponse = _reflection.GeneratedProtocolMessageType('UseItemRareCandyResponse', (_message.Message,), dict(
  DESCRIPTOR = _USEITEMRARECANDYRESPONSE,
  __module__ = 'pogoprotos.networking.responses.use_item_rare_candy_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.UseItemRareCandyResponse)
  ))
_sym_db.RegisterMessage(UseItemRareCandyResponse)


# @@protoc_insertion_point(module_scope)
