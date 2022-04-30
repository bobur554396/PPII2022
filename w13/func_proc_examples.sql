select *
from students;

---- PSQL Functions ----
------------------------------------------------

create or replace function test1()
    returns integer
AS
$$
begin
    return 11;
end
$$ language plpgsql;

select test1();

------------------------------------------------

create or replace function inc(num integer)
    returns integer
as
$$
begin
    return num + 1;
end
$$ language plpgsql;

select inc(100);

------------------------------------------------

create or replace function inc2(num integer)
    returns integer
as
$$
declare
    inner_res integer;
begin
    inner_res := num + 1;
    return inner_res;
end
$$ language plpgsql;

select inc2(15);

------------------------------------------------

drop function sum(num1 integer, num2 integer);

create or replace function sum(num1 integer, num2 integer)
    returns integer
as
$$
declare
    res integer;
begin
    res := $1 + $2;
    return res;
end
$$ language plpgsql;

select sum(2, 3);


------------------------------------------------

create or replace function getStudentIdNameGpa()
    returns table
            (
                id   integer,
                name varchar,
                gpa  numeric
            )
as
$$
begin
    return query
        select s.id, s.name, s.gpa from students as s;
end
$$ language plpgsql;

select *
from getStudentIdNameGpa();


------------------------------------------------

create or replace function getTopNByGPA()
    returns table
            (
                id   integer,
                name varchar,
                gpa  numeric
            )
as
$$
begin
    return query
        select s.id, s.name, s.gpa
        from students as s
        order by s.gpa desc
        limit 5;
end
$$ language plpgsql;

select *
from getTopNByGPA();


------------------------------------------------

create or replace function getAboveGPA(_gpa numeric)
    returns table
            (
                id   integer,
                name varchar,
                gpa  numeric
            )
as
$$
begin
    return query
        select s.id, s.name, s.gpa
        from students as s
        where s.gpa >= $1;
end
$$ language plpgsql;

select *
from getAboveGPA(3.2);

------------------------------------------------

create or replace function getGPABetween(_gpa1 numeric, _gpa2 numeric)
    returns table
            (
                id   integer,
                name varchar,
                gpa  numeric
            )
as
$$
begin
    return query
        select s.id, s.name, s.gpa
        from students as s
        where s.gpa between $1 and $2;
end
$$ language plpgsql;

select *
from getGPABetween(3.7, 3.9);


------------------------------------------------

create or replace function getStudent(_id integer)
    returns record
as
$$
declare
    student record;
begin
    select * into student from students where id = $1;
    return student;
end;
$$ language plpgsql;

------------------------------------------------

create or replace function getStudentName(_id integer)
    returns varchar
as
$$
declare
    student_name varchar;
begin
    select name into student_name from students where id = $1;
    return student_name;
end;
$$ language plpgsql;

select getStudentName(2) as name;

------------------------------------------------

create or replace function getAllStudents()
    returns setof students
as
$$
begin
    return query
        select * from students;
end;
$$ language plpgsql;

select *
from getAllStudents();


---- PSQL Procedure ----
------------------------------------------------
create or replace procedure hello_world()
as
$$
begin
    raise notice 'hello world!';
end;
$$
    LANGUAGE plpgsql;

call hello_world();

------------------------------------------------

create or replace procedure addStudent(id integer, name varchar, gpa numeric)
as
$$
begin
    insert into students(id, name, gpa) values ($1, $2, $3);
end;
$$
    LANGUAGE plpgsql;

call addStudent(1001, 'test student', 3.8);
call addStudent(1002, 'test student 2', 3.8);

select getStudent(1002);

------------------------------------------------

create or replace procedure updateStudent(id integer, name varchar)
as
$$
begin
    update students
    set name = $2
    where students.id = $1;
end;
$$
    LANGUAGE plpgsql;

call updateStudent(1001, 'test student updated');
select getStudent(1001);

------------------------------------------------

create or replace procedure deleteStudent(id integer)
as
$$
begin
    delete
    from students s
    where s.id = $1;
end;
$$
    LANGUAGE plpgsql;

call deleteStudent(1002);
select getStudent(1002);


---- Loop in PLSQL ----
------------------------------------------------

do
$$
    begin
        for cnt in 1..10
            loop
                raise notice 'cnt: %', cnt;
            end loop;
    end
$$;

------------------------------------------------

do
$$
    begin
        for i in reverse 10..1
            loop
                raise notice 'cnt: %', i;
            end loop;
    end
$$;


------------------------------------------------
select * from getGPABetween(3.7, 3.9);

do
$$
    declare
        student record;
    begin
        for student in select * from students limit 5
            loop
                raise notice 'id=%, name=%, gpa=%', student.id, student.name, student.gpa;
            end loop;
    end
$$;


------------------------------------------------
select * from getGPABetween(3.7, 3.9);

do
$$
    declare
        student record;
    begin
        for student in select * from getGPABetween(3.7, 3.9)
            loop
                raise notice 'id=%, name=%, gpa=%', student.id, student.name, student.gpa;
            end loop;
    end
$$;


