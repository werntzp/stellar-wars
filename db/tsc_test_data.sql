/*------------------------
-- switch to tsc database
------------------------*/
use tsc;

/*------------------------
-- add a test ship
------------------------*/

insert into t_ship (ship_id, type_id, ship_name, ship_creator, ship_description, ship_engine, ship_hull, ship_reactor, ship_top_speed) values (1, 3, 'Pillar of Autumn', 'werntzp@hotmail.com', 'Halcyon-class light cruiser, survived the fall of Reach and crashed onto Installation 04 under command of Captain Keyes', 5, 4, 3, 8);

/*------------------------
-- add some weapons 
------------------------*/

/*-- add shields --*/
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (1, 1, 1, 2, 5, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (2, 1, 2, 2, 5, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (3, 1, 6, 2, 5, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (4, 1, 3, 2, 2, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (5, 1, 4, 2, 2, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (6, 1, 5, 2, 2, null);

/*-- add self-destruct --*/
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (7, 1, 1, 9, null, null);

/*-- add armor --*/
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (8, 1, 1, 1, 1, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (9, 1, 2, 1, 1, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (10, 1, 3, 1, 1, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (11, 1, 4, 1, 1, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (12, 1, 5, 1, 1, null);
insert into t_ship_system (ship_system_id, ship_id, side_id, system_id, system_value, extra_use) values (13, 1, 6, 1, 1, null);

/*-- add plasma cannon --*/
insert into t_ship_weapon (ship_weapon_id, ship_id, side_id, weapon_id, extra_hit, extra_damage) values (1, 1, 1, 6, null, null);

/*-- add guns (with --*/
insert into t_ship_weapon (ship_weapon_id, ship_id, side_id, weapon_id, extra_hit, extra_damage) values (2, 1, 2, 5, null, 2);
insert into t_ship_weapon (ship_weapon_id, ship_id, side_id, weapon_id, extra_hit, extra_damage) values (3, 1, 2, 5, null, 2);
insert into t_ship_weapon (ship_weapon_id, ship_id, side_id, weapon_id, extra_hit, extra_damage) values (4, 1, 3, 5, null, 2);
insert into t_ship_weapon (ship_weapon_id, ship_id, side_id, weapon_id, extra_hit, extra_damage) values (5, 1, 5, 5, null, 2);
insert into t_ship_weapon (ship_weapon_id, ship_id, side_id, weapon_id, extra_hit, extra_damage) values (6, 1, 1, 5, null, 2);
