-- SQLite
create table adventure_trip (
        Column varchar,
        Type varchar,
        Length int,
        Decimal_places int,
        Nulls_allowed varchar,
        Description varchar
);

insert into adventure_trip values('TRIP_ID','DECIMAL',3,0,'No','Trip ID (primary key)');
insert into adventure_trip values('TRIP_NAME','VARCHAR',75,'','','Trip name');
insert into adventure_trip values('START_LOCATION','VARCHAR',50,'','','Start location for trip');
insert into adventure_trip values('STATE','CHAR',2,'','','Trip state');
insert into adventure_trip values('DISTANCE','NUMBER',4,0,'','Distance (length) of trip');
insert into adventure_trip values('MAX_GRP_SIZE','NUMBER',4,0,'','Maximum number of persons');
insert into adventure_trip values('TYPE','CHAR',20,'','','Trip type');
insert into adventure_trip values('SEASON','CHAR',20,'','','Trip season');

select * from adventure_trip;
