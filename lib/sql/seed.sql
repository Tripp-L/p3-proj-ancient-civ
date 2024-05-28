INSERT INTO cultures (name, region, era) VALUES
('Ancient Greece', 'Europe', 'Classical Antiquity'),
('Ancient Egypt', 'Africa', 'Bronze Age'),
('Ancient Rome', 'Europe', 'Classical Antiquity'),
('Norse Mythology', 'Scandinavia', 'Viking Age'),
('Ancient Mesopotamia', 'Middle East', 'Ancient Near East'),
('Ancient China', 'East Asia', 'Imperial China'),
('Inca Civilization', 'South America', 'Pre-Columbian'),
('Celtic Civilization', 'Europe', 'Iron Age'),
('Maya Civilization', 'Mesoamerica', 'Pre-Columbian'),
('Ancient Japan', 'East Asia', 'Feudal Japan');

INSERT INTO deities (name, domain, attributes, culture_id) VALUES
('Zeus', 'Sky', 'Thunderbolt,Eagle', 1),
('Ra', 'Sun', 'Sun disk,Falcon', 2),
('Mars', 'War', 'Sword,Helmet', 3),
('Odin', 'Wisdom', 'One-eyed,Ravens', 4),
('Enlil', 'Air', 'Storms,Wind', 5),
('Tao', 'Nature', 'Yin-Yang,Harmony', 6),
('Inti', 'Sun', 'Sun God,Heat', 7),
('Dagda', 'Life and Death', 'Club,Cauldron', 8),
('Kukulkan', 'Wind', 'Feathered Serpent,Creator', 9),
('Amaterasu', 'Sun', 'Sun Goddess,Light', 10);

INSERT INTO artifacts (name, artifact_type, discovered_date, origin_date, culture_id) VALUES
('Parthenon Marbles', 'Statue', '1816', '5th century BC', 1),
('Tutankhamun''s Mask', 'Mask', '1925', '14th century BC', 2),
('Colosseum Ruins', 'Architecture', '1748', '1st century AD', 3),
('Mjolnir', 'Weapon', 'None', 'Norse Mythology', 4),
('Ishtar Gate', 'Gate', '1899', '6th century BC', 5),
('Great Wall of China', 'Structure', 'None', '7th century BC', 6),
('Machu Picchu', 'City', '1911', '15th century AD', 7),
('Stonehenge', 'Monument', 'None', 'Bronze Age', 8),
('Chichen Itza', 'Pyramid', 'None', '9th century AD', 9),
('Hiroshima Castle', 'Castle', 'None', '16th century AD', 10);

INSERT INTO myths (name, description, deity_id) VALUES
('The Birth of Zeus', 'Zeus was born in a cave on Mount Ida.', 1),
('The Journey of Ra', 'Ra travels through the underworld at night.', 2),
('The War of Mars', 'Mars fought many battles in the name of Rome.', 3),
('The Wisdom of Odin', 'Odin sacrificed his eye for wisdom.', 4),
('The Storms of Enlil', 'Enlil controls the winds and storms.', 5),
('The Balance of Tao', 'Tao maintains balance in nature and existence.', 6),
('The Sun God Inti', 'Inti is worshipped as the Sun God by the Inca civilization.', 7),
('The Club of Dagda', 'Dagda wields a mighty club that can both slay and resurrect.', 8),
('The Feathered Serpent', 'Kukulkan is a deity associated with creation and wind.', 9),
('The Radiance of Amaterasu', 'Amaterasu brings light and warmth to the world.', 10);