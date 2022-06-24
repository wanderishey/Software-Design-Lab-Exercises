-- SQLite
CREATE TABLE ADVENTURE_TRIP (
    TRIP_ID int,
    TRIP_NAME varchar(75),
    START_LOCATION varchar(50),
    STATE varchar(2),
    DISTANCE int,
    MAX_GRP_SIZE int,
    TYPE varchar(20),
    SEASON varchar(20)
    );

select *from ADVENTURE_TRIP;
DELETE FROM ADVENTURE_TRIP WHERE TRIP_ID=27;

INSERT INTO ADVENTURE_TRIP VALUES ( 45,
            'Jay Peak',
            'Jay',
            'VT',
            8,
            8,
            'Hiking',
            'Summer'
            );
INSERT INTO ADVENTURE_TRIP VALUES ( 24,
            'mermaid',
            'shell',
            'LA',
            10,
            11,
            'Swimming',
            'Summer'
            );

INSERT INTO ADVENTURE_TRIP VALUES ( 27,
            'sherck',
            'fiona',
            'CC',
            7,
            8,
            'Vacation',
            'Winter'
            );


select *from MUSIC_TRIP;




