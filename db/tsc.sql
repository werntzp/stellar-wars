/*------------------------
-- switch to tsc database
------------------------*/
use tsc;

/*------------------------
-- drop all the tables
------------------------*/
drop table if exists t_ship_review;
drop table if exists t_ship_system;
drop table if exists t_ship_weapon;
drop table if exists t_ship;
drop table if exists t_type_dict;
drop table if exists t_side_dict;
drop table if exists t_weapon_dict;
drop table if exists t_system_dict;

/*------------------------
-- ship type dictionary
------------------------*/
create table t_type_dict (type_id int not null, type_name varchar(15) not null, type_abbrev char(2) not null, primary key (type_id));
insert into t_type_dict (type_id, type_name, type_abbrev) values (1, 'Dreadnought', 'DN');
insert into t_type_dict (type_id, type_name, type_abbrev) values (2, 'Battleship', 'BB');
insert into t_type_dict (type_id, type_name, type_abbrev) values (3, 'Cruiser', 'CA');
insert into t_type_dict (type_id, type_name, type_abbrev) values (4, 'Destroyer', 'DD');
insert into t_type_dict (type_id, type_name, type_abbrev) values (5, 'Escort', 'ES');
insert into t_type_dict (type_id, type_name, type_abbrev) values (6, 'Scout', 'SC');
insert into t_type_dict (type_id, type_name, type_abbrev) values (7, 'Freighter', 'FR');

/*------------------------
-- ship side dictionary
------------------------*/
create table t_side_dict (side_id int not null, side_name varchar(12) not null, primary key (side_id));
insert into t_side_dict (side_id, side_name) values (1, 'Front');
insert into t_side_dict (side_id, side_name) values (2, 'Front-Right');
insert into t_side_dict (side_id, side_name) values (3, 'Rear-Right');
insert into t_side_dict (side_id, side_name) values (4, 'Rear');
insert into t_side_dict (side_id, side_name) values (5, 'Rear-Left');
insert into t_side_dict (side_id, side_name) values (6, 'Front-Left');

/*------------------------
-- ship weapon dictionary
------------------------*/
create table t_weapon_dict (weapon_id int not null, weapon_name varchar(15) not null, primary key (weapon_id));
insert into t_weapon_dict (weapon_id, weapon_name) values (1, 'Laser');
insert into t_weapon_dict (weapon_id, weapon_name) values (2, 'Force Beam');
insert into t_weapon_dict (weapon_id, weapon_name) values (3, 'Missile');
insert into t_weapon_dict (weapon_id, weapon_name) values (4, 'Beam');
insert into t_weapon_dict (weapon_id, weapon_name) values (5, 'Gun');
insert into t_weapon_dict (weapon_id, weapon_name) values (6, 'Plasma Cannon');

/*------------------------
-- ship system dictionary
------------------------*/
create table t_system_dict (system_id int not null, system_name varchar(15) not null, primary key (system_id));
insert into t_system_dict (system_id, system_name) values (1, 'Armor');
insert into t_system_dict (system_id, system_name) values (2, 'Shield');
insert into t_system_dict (system_id, system_name) values (3, 'Missile Rack');
insert into t_system_dict (system_id, system_name) values (4, 'Missile Defense');
insert into t_system_dict (system_id, system_name) values (5, 'Multi-Tracking');
insert into t_system_dict (system_id, system_name) values (6, 'Sensors');
insert into t_system_dict (system_id, system_name) values (7, 'Cloaking');
insert into t_system_dict (system_id, system_name) values (8, 'Mine');
insert into t_system_dict (system_id, system_name) values (9, 'Self-Destruct');

/*------------------------
-- ship 
------------------------*/
create table t_ship (ship_id int not null auto_increment, type_id int not null, ship_name varchar(75),  ship_creator varchar(75), ship_description varchar(1000), ship_engine int,  ship_hull int, ship_reactor int,  ship_top_speed int,  primary key (ship_id),  foreign key (type_id) references t_type_dict (type_id));

/*------------------------
-- ship weapon 
------------------------*/
create table t_ship_weapon (ship_weapon_id int not null auto_increment, ship_id int not null, side_id int not null, weapon_id int not null, extra_hit int, extra_damage int, primary key (ship_weapon_id), foreign key (ship_id) references t_ship (ship_id), foreign key (side_id) references t_side_dict (side_id), foreign key (weapon_id) references t_weapon_dict (weapon_id));

/*------------------------
-- ship system 
------------------------*/
create table t_ship_system (ship_system_id int not null auto_increment, ship_id int not null, side_id int not null, system_id int not null, system_value int, extra_use int, primary key (ship_system_id), foreign key (ship_id) references t_ship (ship_id), foreign key (side_id) references t_side_dict (side_id), foreign key (system_id) references t_system_dict (system_id));

/*------------------------
-- ship review 
------------------------*/
create table t_ship_review (ship_review_id int not null auto_increment, ship_id int not null, review_date datetime, review_stars int, review_text text, primary key (ship_review_id), foreign key (ship_id) references t_ship (ship_id));

/*------------------------
-- v_list_ships 
------------------------*/
create view v_list_ships as select s.ship_id, s.ship_name, t.type_name from t_ship s inner join t_ship_type_dict t on t.type_id = s.type_id;


