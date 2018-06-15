# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/quests/quest_reward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import pokemon_display_pb2 as pogoprotos_dot_data_dot_pokemon__display__pb2
from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/quests/quest_reward.proto',
  package='pogoprotos.data.quests',
  syntax='proto3',
  serialized_pb=_b('\n)pogoprotos/data/quests/quest_reward.proto\x12\x16pogoprotos.data.quests\x1a%pogoprotos/data/pokemon_display.proto\x1a!pogoprotos/enums/pokemon_id.proto\x1a\'pogoprotos/inventory/item/item_id.proto\"\xd3\x06\n\x0bQuestReward\x12\x36\n\x04type\x18\x01 \x01(\x0e\x32(.pogoprotos.data.quests.QuestReward.Type\x12\x0b\n\x03\x65xp\x18\x02 \x01(\x05\x12<\n\x04item\x18\x03 \x01(\x0b\x32..pogoprotos.data.quests.QuestReward.ItemReward\x12\x10\n\x08stardust\x18\x04 \x01(\x05\x12\x45\n\x05\x63\x61ndy\x18\x05 \x01(\x0b\x32\x36.pogoprotos.data.quests.QuestReward.PokemonCandyReward\x12\x1a\n\x12\x61vatar_template_id\x18\x06 \x01(\t\x12\x19\n\x11quest_template_id\x18\x07 \x01(\t\x12U\n\x11pokemon_encounter\x18\x08 \x01(\x0b\x32:.pogoprotos.data.quests.QuestReward.PokemonEncounterReward\x1aM\n\nItemReward\x12/\n\x04item\x18\x01 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x1aU\n\x12PokemonCandyReward\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\x1a\xb6\x01\n\x16PokemonEncounterReward\x12/\n\npokemon_id\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x31\n)use_quest_pokemon_encounter_distribuition\x18\x02 \x01(\x08\x12\x38\n\x0fpokemon_display\x18\x03 \x01(\x0b\x32\x1f.pogoprotos.data.PokemonDisplay\"{\n\x04Type\x12\t\n\x05UNSET\x10\x00\x12\x0e\n\nEXPERIENCE\x10\x01\x12\x08\n\x04ITEM\x10\x02\x12\x0c\n\x08STARDUST\x10\x03\x12\t\n\x05\x43\x41NDY\x10\x04\x12\x13\n\x0f\x41VATAR_CLOTHING\x10\x05\x12\t\n\x05QUEST\x10\x06\x12\x15\n\x11POKEMON_ENCOUNTER\x10\x07\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_pokemon__display__pb2.DESCRIPTOR,pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])



_QUESTREWARD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='pogoprotos.data.quests.QuestReward.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPERIENCE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STARDUST', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANDY', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AVATAR_CLOTHING', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUEST', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_ENCOUNTER', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=913,
  serialized_end=1036,
)
_sym_db.RegisterEnumDescriptor(_QUESTREWARD_TYPE)


_QUESTREWARD_ITEMREWARD = _descriptor.Descriptor(
  name='ItemReward',
  full_name='pogoprotos.data.quests.QuestReward.ItemReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.data.quests.QuestReward.ItemReward.item', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='pogoprotos.data.quests.QuestReward.ItemReward.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=562,
  serialized_end=639,
)

_QUESTREWARD_POKEMONCANDYREWARD = _descriptor.Descriptor(
  name='PokemonCandyReward',
  full_name='pogoprotos.data.quests.QuestReward.PokemonCandyReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.quests.QuestReward.PokemonCandyReward.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='pogoprotos.data.quests.QuestReward.PokemonCandyReward.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=641,
  serialized_end=726,
)

_QUESTREWARD_POKEMONENCOUNTERREWARD = _descriptor.Descriptor(
  name='PokemonEncounterReward',
  full_name='pogoprotos.data.quests.QuestReward.PokemonEncounterReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.quests.QuestReward.PokemonEncounterReward.pokemon_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_quest_pokemon_encounter_distribuition', full_name='pogoprotos.data.quests.QuestReward.PokemonEncounterReward.use_quest_pokemon_encounter_distribuition', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_display', full_name='pogoprotos.data.quests.QuestReward.PokemonEncounterReward.pokemon_display', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=729,
  serialized_end=911,
)

_QUESTREWARD = _descriptor.Descriptor(
  name='QuestReward',
  full_name='pogoprotos.data.quests.QuestReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pogoprotos.data.quests.QuestReward.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='pogoprotos.data.quests.QuestReward.exp', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='pogoprotos.data.quests.QuestReward.item', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stardust', full_name='pogoprotos.data.quests.QuestReward.stardust', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy', full_name='pogoprotos.data.quests.QuestReward.candy', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar_template_id', full_name='pogoprotos.data.quests.QuestReward.avatar_template_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quest_template_id', full_name='pogoprotos.data.quests.QuestReward.quest_template_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_encounter', full_name='pogoprotos.data.quests.QuestReward.pokemon_encounter', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_QUESTREWARD_ITEMREWARD, _QUESTREWARD_POKEMONCANDYREWARD, _QUESTREWARD_POKEMONENCOUNTERREWARD, ],
  enum_types=[
    _QUESTREWARD_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=1036,
)

_QUESTREWARD_ITEMREWARD.fields_by_name['item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_QUESTREWARD_ITEMREWARD.containing_type = _QUESTREWARD
_QUESTREWARD_POKEMONCANDYREWARD.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_QUESTREWARD_POKEMONCANDYREWARD.containing_type = _QUESTREWARD
_QUESTREWARD_POKEMONENCOUNTERREWARD.fields_by_name['pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_QUESTREWARD_POKEMONENCOUNTERREWARD.fields_by_name['pokemon_display'].message_type = pogoprotos_dot_data_dot_pokemon__display__pb2._POKEMONDISPLAY
_QUESTREWARD_POKEMONENCOUNTERREWARD.containing_type = _QUESTREWARD
_QUESTREWARD.fields_by_name['type'].enum_type = _QUESTREWARD_TYPE
_QUESTREWARD.fields_by_name['item'].message_type = _QUESTREWARD_ITEMREWARD
_QUESTREWARD.fields_by_name['candy'].message_type = _QUESTREWARD_POKEMONCANDYREWARD
_QUESTREWARD.fields_by_name['pokemon_encounter'].message_type = _QUESTREWARD_POKEMONENCOUNTERREWARD
_QUESTREWARD_TYPE.containing_type = _QUESTREWARD
DESCRIPTOR.message_types_by_name['QuestReward'] = _QUESTREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestReward = _reflection.GeneratedProtocolMessageType('QuestReward', (_message.Message,), dict(

  ItemReward = _reflection.GeneratedProtocolMessageType('ItemReward', (_message.Message,), dict(
    DESCRIPTOR = _QUESTREWARD_ITEMREWARD,
    __module__ = 'pogoprotos.data.quests.quest_reward_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestReward.ItemReward)
    ))
  ,

  PokemonCandyReward = _reflection.GeneratedProtocolMessageType('PokemonCandyReward', (_message.Message,), dict(
    DESCRIPTOR = _QUESTREWARD_POKEMONCANDYREWARD,
    __module__ = 'pogoprotos.data.quests.quest_reward_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestReward.PokemonCandyReward)
    ))
  ,

  PokemonEncounterReward = _reflection.GeneratedProtocolMessageType('PokemonEncounterReward', (_message.Message,), dict(
    DESCRIPTOR = _QUESTREWARD_POKEMONENCOUNTERREWARD,
    __module__ = 'pogoprotos.data.quests.quest_reward_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestReward.PokemonEncounterReward)
    ))
  ,
  DESCRIPTOR = _QUESTREWARD,
  __module__ = 'pogoprotos.data.quests.quest_reward_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.quests.QuestReward)
  ))
_sym_db.RegisterMessage(QuestReward)
_sym_db.RegisterMessage(QuestReward.ItemReward)
_sym_db.RegisterMessage(QuestReward.PokemonCandyReward)
_sym_db.RegisterMessage(QuestReward.PokemonEncounterReward)


# @@protoc_insertion_point(module_scope)
