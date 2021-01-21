PARSING-
1 Переходим в корневой каталог с manage.py
2 Virtualenv (имя виртуального окружения)
3 (имя виртуального окружения)/scripts/activate
4 Pip install -r requirements.txt
5 python manage.py runserver
6 python runparser.py
___________________________________________________________________

SQL REQUEST

select
  p.internal_number as InternalNumber,
  CONCAT(e.name, '/', e.surname) as 'Name/Surname',
  p.position as Position,
  round(e.salary_year/12, 2) as 'Salary/Month',
  round(sum(r.taxe)/count(r.id), 2) as Tax,
  count(r.month) as Month
from
  employee e,
  position p,
  rate r
where
  p.employee_id = e.id
  and r.employee_id = e.id
group by e.id;