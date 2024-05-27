#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from cli import main
from models.culture import Culture
from models.deity import Deity
from models.artifact import Artifact
from models.myth import Myth


greek_culture = Culture(name='Ancient Greece', region='Europe', era='Classical Antiquity')
egyptian_culture = Culture(name='Ancient Egypt', region='Africa', era='Bronze Age')
roman_culture = Culture(name='Ancient Rome', region='Europe', era='Classical Antiquity')
norse_culture = Culture(name='Norse Mythology', region='Scandinavia', era='Viking Age')
mesopotamian_culture = Culture(name='Ancient Mesopotamia', region='Middle East', era='Ancient Near East')
chinese_culture = Culture(name='Ancient China', region='East Asia', era='Imperial China')
inca_culture = Culture(name='Inca Civilization', region='South America', era='Pre-Columbian')
celtic_culture = Culture(name='Celtic Civilization', region='Europe', era='Iron Age')
mayan_culture = Culture(name='Maya Civilization', region='Mesoamerica', era='Pre-Columbian')
japanese_culture = Culture(name='Ancient Japan', region='East Asia', era='Feudal Japan')

zeus = Deity(name='Zeus', domain='Sky', attributes=['Thunderbolt', 'Eagle'], culture=greek_culture)
ra = Deity(name='Ra', domain='Sun', attributes=['Sun disk', 'Falcon'], culture=egyptian_culture)
mars = Deity(name='Mars', domain='War', attributes=['Sword', 'Helmet'], culture=roman_culture)
odin = Deity(name='Odin', domain='Wisdom', attributes=['One-eyed', 'Ravens'], culture=norse_culture)
enlil = Deity(name='Enlil', domain='Air', attributes=['Storms', 'Wind'], culture=mesopotamian_culture)
tao = Deity(name='Tao', domain='Nature', attributes=['Yin-Yang', 'Harmony'], culture=chinese_culture)
inti = Deity(name='Inti', domain='Sun', attributes=['Sun God', 'Heat'], culture=inca_culture)
daghda = Deity(name='Dagda', domain='Life and Death', attributes=['Club', 'Cauldron'], culture=celtic_culture)
kukulkan = Deity(name='Kukulkan', domain='Wind', attributes=['Feathered Serpent', 'Creator'], culture=mayan_culture)
amaterasu = Deity(name='Amaterasu', domain='Sun', attributes=['Sun Goddess', 'Light'], culture=japanese_culture)

parthenon_marbles = Artifact(name='Parthenon Marbles', artifact_type='Statue', discovered_date='1816', origin_date='5th century BC', culture=greek_culture)
tutankhamun_mask = Artifact(name='Tutankhamun\'s Mask', artifact_type='Mask', discovered_date='1925', origin_date='14th century BC', culture=egyptian_culture)
colosseum_ruins = Artifact(name='Colosseum Ruins', artifact_type='Architecture', discovered_date='1748', origin_date='1st century AD', culture=roman_culture)
mjolnir = Artifact(name='Mjolnir', artifact_type='Weapon', discovered_date='None', origin_date='Norse Mythology', culture=norse_culture)
ishtar_gate = Artifact(name='Ishtar Gate', artifact_type='Gate', discovered_date='1899', origin_date='6th century BC', culture=mesopotamian_culture)
great_wall_of_china = Artifact(name='Great Wall of China', artifact_type='Structure', discovered_date='None', origin_date='7th century BC', culture=chinese_culture)
machu_picchu = Artifact(name='Machu Picchu', artifact_type='City', discovered_date='1911', origin_date='15th century AD', culture=inca_culture)
stonehenge = Artifact(name='Stonehenge', artifact_type='Monument', discovered_date='None', origin_date='Bronze Age', culture=celtic_culture)
chichen_itza = Artifact(name='Chichen Itza', artifact_type='Pyramid', discovered_date='None', origin_date='9th century AD', culture=mayan_culture)
hiroshima_castle = Artifact(name='Hiroshima Castle', artifact_type='Castle', discovered_date='None', origin_date='16th century AD', culture=japanese_culture)

zeus.add_myth(name='The Birth of Zeus', text='Zeus was born in a cave on Mount Ida.')
ra.add_myth(name='The Journey of Ra', text='Ra travels through the underworld at night.')
mars.add_myth(name='The War of Mars', text='Mars fought many battles in the name of Rome.')
odin.add_myth(name='The Wisdom of Odin', text='Odin sacrificed his eye for wisdom.')
enlil.add_myth(name='The Storms of Enlil', text='Enlil controls the winds and storms.')
tao.add_myth(name='The Balance of Tao', text='Tao maintains balance in nature and existence.')
inti.add_myth(name='The Sun God Inti', text='Inti is worshipped as the Sun God by the Inca civilization.')
daghda.add_myth(name='The Club of Dagda', text='Dagda wields a mighty club that can both slay and resurrect.')
kukulkan.add_myth(name='The Feathered Serpent', text='Kukulkan is a deity associated with creation and wind.')
amaterasu.add_myth(name='The Radiance of Amaterasu', text='Amaterasu brings light and warmth to the world.')

ipdb.set_trace()

if __name__ == "__main__":
