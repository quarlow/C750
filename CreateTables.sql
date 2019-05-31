-- I made some changes to the samle schema file, these were due to errors or issues when I tried to run this script.
-- I updated all the id fields to bigint intead of integter becasuse my data contained values outside the range of integer.
-- I changed the key column to key2, because key was a protected value and was not allowed in MySQL.

CREATE TABLE osm.nodes (
    id bigint PRIMARY KEY NOT NULL,
    lat REAL,
    lon REAL,
    user TEXT,
    uid bigint,
    version bigint,
    changeset bigint,
    timestamp TEXT
);

CREATE TABLE osm.nodes_tags (
    id bigint,
    key2 TEXT,
    value TEXT,
    category TEXT,
    FOREIGN KEY (id) REFERENCES nodes(id)
);

CREATE TABLE osm.ways (
    id bigint PRIMARY KEY NOT NULL,
    user TEXT,
    uid bigint,
    version TEXT,
    changeset bigint,
    timestamp TEXT
);

CREATE TABLE osm.ways_tags (
    id bigint NOT NULL,
    key2 TEXT NOT NULL,
    value TEXT NOT NULL,
    category TEXT,
    FOREIGN KEY (id) REFERENCES ways(id)
);

CREATE TABLE osm.ways_nodes (
    id bigint NOT NULL,
    node_id bigint NOT NULL,
    position bigint NOT NULL,
    FOREIGN KEY (id) REFERENCES ways(id),
    FOREIGN KEY (node_id) REFERENCES nodes(id)
);
