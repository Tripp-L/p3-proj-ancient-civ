INSERT INTO cultures (name, region, era) VALUES
('Ancient Greece', 'Europe', 'Classical Antiquity'),
('Ancient Egypt', 'Africa', 'Bronze Age');

INSERT INTO deities (name, domain, attributes, culture_id) VALUES
('Zeus', 'Sky', 'Thunderbolt,Eagle', 1),
('Ra', 'Sun', 'Sun disk,Falcon', 2);

INSERT INTO artifacts (name, artifact_type, discovered_date, origin_date, culture_id) VALUES
('Parthenon Marbles', 'Statue', '1816', '5th century BC', 1),
('Tutankhamun''s Mask', 'Mask', '1925', '14th century BC', 2);

INSERT INTO myths (name, description, deity_id) VALUES
('The Birth of Zeus', 'Zeus was born in a cave on Mount Ida.', 1),
('The Journey of Ra', 'Ra travels through the underworld at night.', 2);