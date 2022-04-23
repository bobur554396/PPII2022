create database pp2demo;

create role pp2demo_user with password 'passw0rd' LOGIN;

-- alter role pp2demo_user LOGIN;

grant all privileges on database pp2demo to pp2demo_user;

-- Creating the table
create table students
(
    id    int,
    name  varchar(255) not null,
    email varchar(255),
    gpa   numeric      not null
);


-- Adding data to our table
insert into students (id, name, email, gpa)
values (1, 'student 1', 's1@gmail.com', 3.8);

insert into students (id, name, email, gpa)
values (2, 'student 2', 's2@gmail.com', 3.5),
       (3, 'student 3', 's3@gmail.com', 3.2),
       (4, 'student 4', 's4@gmail.com', 3.7);


insert into students (id, name, email, gpa)
values (5, 'student 5', 's5@gmail.com', 3.5),
       (6, 'student 6', 's6@gmail.com', 3.7);


-- adding new columns to existing table
alter table students
    add column faculty varchar(255),
    add column age     int;


-- Update the data in table
update students
set faculty = 'FIT',
    age     = 20
where id in (5, 6);

update students
set faculty = 'FOGI'
where id > 2;

update students
set age = 18
where id = 1
   or id = 2;

update students
set age = 19
where id = 3
   or id = 4
   or id = 5
   or id = 6;

update students
set age = 19
where id in (3, 4, 5, 6);

update students
set faculty = 'BS'
where id = 2;


-- Read the data from table

select 2 + 3 * 2 as val1, 4 + 5 as val2;

select id, name, email, age, faculty, gpa
from students;

select *
from students;

select *
from students
where id > 2;

select *
from students
where id > 2
  and id < 4;

select *
from students
where gpa between 3.5 and 3.7;

select t.*
from students t
where gpa between 3.5 and 3.7;

select *
from students
where gpa > 3.5
  and students.faculty = 'FIT';

select id, name, gpa
from students;


select *
from students
where gpa > 3.2
order by gpa desc;

-- select top 3 big GPA students which are more then 3.2
select *
from students
where gpa > 3.2
order by gpa desc limit 3;


-- Delete items from table
delete
from students
where id = 4;

delete
from students
where faculty = 'BS';

select *
from students
where name = 'student 1';


alter table students
add column score int default 0;


-- DDL - Data definition language (create database, create table, create ....)
-- DML - Data manipulation language (insert, update, select, delete..)
