/*------------------------
-- switch to tsc database
------------------------*/
use tsc;

/*------------------------
-- add a test ship
------------------------*/

insert into t_ship 



create table t_ship (ship_id int not null, type_id int not null, ship_name varchar(75),  ship_creator varchar(75), ship_description varchar(1000), ship_engine int,  ship_hull int, ship_reactor int,  ship_speed int,  primary key (ship_id),  foreign key (type_id) references t_type_dict (type_id));

/*------------------------
-- ship weapon 
------------------------*/
create table t_ship_weapon (ship_weapon_id int not null, ship_id int not null, side_id int not null, weapon_id int not null, extra_hit int, extra_damage int, primary key (ship_weapon_id), foreign key (ship_id) references t_ship (ship_id), foreign key (side_id) references t_side_dict (side_id), foreign key (weapon_id) references t_weapon_dict (weapon_id));

/*------------------------
-- ship system 
------------------------*/
create table t_ship_system (ship_system_id int not null, ship_id int not null, side_id int not null, system_id int not null, extra_use int, primary key (ship_system_id), foreign key (ship_id) references t_ship (ship_id), foreign key (side_id) references t_side_dict (side_id), foreign key (system_id) references t_system_dict (system_id));
