----------------------------------------------------------------------------------------------------
-----------WatchApp, Base de datos------------------------------------------------------------------
-----------2015-1-----------------------------------------------------------------------------------

----------------------------------------------------------------------------------------------------
-----------Inserts para UserProfile (completa el número de celular del usuario registrado-----------
----------------------------------------------------------------------------------------------------

-- INSERT INTO watchapp_userprofile (mobile_number, user_id) VALUES ('+573166537244', 1);

-- INSERT INTO watchapp_userprofile (mobile_number, user_id) VALUES ('+573002146240', 2);

-- INSERT INTO watchapp_userprofile (mobile_number, user_id) VALUES ('+573156016907', 3);

----------------------------------------------------------------------------------------------------
-----------Inserts para crear Grupos de usuarios-----------
----------------------------------------------------------------------------------------------------

-- INSERT INTO auth_group (name) VALUES ('usuarios');

-- INSERT INTO auth_group (name) VALUES ('constructoras');

----------------------------------------------------------------------------------------------------
-----------Inserts para relacionar usuarios en grupos de usuarios-----------
----------------------------------------------------------------------------------------------------

-- INSERT INTO auth_user_groups (user_id, group_id) VALUES (1, 1);

-- INSERT INTO auth_user_groups (user_id, group_id) VALUES (2, 1);

-- INSERT INTO auth_user_groups (user_id, group_id) VALUES (3, 1);

----------------------------------------------------------------------------------------------------
-----------Insert para completar la información de la constructora-----------
----------------------------------------------------------------------------------------------------

-- INSERT INTO watchapp_constructorcompany (nit, company_name, address, fixed_phone, fixed_phone_extension, mobile_number, email, contact_name, user_id) 
--	VALUES ('41014101-6', 'Constructora Andes', 'Calle 18A 3-12', '3363636', '4520', '+573202036599', 'gd.bernal10@uniandes.edu.co', 'German Bernal', 3);

----------------------------------------------------------------------------------------------------
-----------Inserts para crear propiedades-----------
----------------------------------------------------------------------------------------------------

-- INSERT INTO watchapp_property (name, address, fixed_phone, plan, constructor_company_id) 
-- 	VALUES ('Edificio Aja, Apto 305', 'Carrera 15 79-25', '5555555', 
-- 'http://grupocolviva.com/wp-content/uploads/2013/05/resized_2A1-e1381615727192.jpg', '1);

-- INSERT INTO watchapp_property (name, address, fixed_phone, plan, constructor_company_id) 
-- 	VALUES ('Edificio Aja, Apto 304', 'Carrera 15 79-25', '4444444', 
-- 'http://grupocolviva.com/wp-content/uploads/2013/05/resized_2A1-e1381615727192.jpg', '1);

-- INSERT INTO watchapp_property (name, address, fixed_phone, plan, constructor_company_id) 
-- 	VALUES ('Edificio Aja, Apto 303', 'Carrera 15 79-25', '3333333', 
-- 'http://grupocolviva.com/wp-content/uploads/2013/05/resized_2A1-e1381615727192.jpg', '1);

-- INSERT INTO watchapp_property (name, address, fixed_phone, plan, constructor_company_id) 
-- 	VALUES ('Edificio Aja, Apto 302', 'Carrera 15 79-25', '2222222', 
-- 'http://grupocolviva.com/wp-content/uploads/2013/05/resized_2A1-e1381615727192.jpg', '1);

-- INSERT INTO watchapp_property (name, address, fixed_phone, plan, constructor_company_id) 
-- 	VALUES ('Edificio Aja, Apto 301', 'Carrera 15 79-25', '1111111', 
-- 'http://grupocolviva.com/wp-content/uploads/2013/05/resized_2A1-e1381615727192.jpg', '1);

----------------------------------------------------------------------------------------------------
-----------Inserts para relacionar propiedades con propietarios-----------
----------------------------------------------------------------------------------------------------

-- INSERT INTO watchapp_userprofile_properties_as_owner (userprofile_id, property_id) 
-- 	VALUES (1, 1);

-- INSERT INTO watchapp_userprofile_properties_as_owner (userprofile_id, property_id) 
-- 	VALUES (1, 3);

-- INSERT INTO watchapp_userprofile_properties_as_owner (userprofile_id, property_id) 
-- 	VALUES (2, 2);

-- INSERT INTO watchapp_userprofile_properties_as_owner (userprofile_id, property_id) 
-- 	VALUES (2, 3);

-- INSERT INTO watchapp_userprofile_properties_as_owner (userprofile_id, property_id) 
-- 	VALUES (2, 4);

-- INSERT INTO watchapp_userprofile_properties_as_owner (userprofile_id, property_id) 
--  VALUES (2, 5);

----------------------------------------------------------------------------------------------------
-----------Inserts para relacionar propiedades con residentes-----------
----------------------------------------------------------------------------------------------------

-- INSERT INTO watchapp_userprofile_properties_as_resident (userprofile_id, property_id) 
-- 	VALUES (1, 5);

-- INSERT INTO watchapp_userprofile_properties_as_resident (userprofile_id, property_id) 
-- 	VALUES (1, 3);

-- INSERT INTO watchapp_userprofile_properties_as_resident (userprofile_id, property_id) 
-- 	VALUES (2, 4);

-- INSERT INTO watchapp_userprofile_properties_as_resident (userprofile_id, property_id) 
-- 	VALUES (2, 2);

-- INSERT INTO watchapp_userprofile_properties_as_resident (userprofile_id, property_id) 
-- 	VALUES (2, 1);

-- select * from watchapp_property;
-- select * from watchapp_userprofile_properties_as_owner;
-- select * from watchapp_userprofile_properties_as_resident;
-- select * from watchapp_constructorcompany;
-- select * from auth_user;
-- select * from auth_group;
-- select * from watchapp_userprofile;
-- select * from auth_user_groups;
select * from watchapp_event;
-- select * from watchapp_sensor;