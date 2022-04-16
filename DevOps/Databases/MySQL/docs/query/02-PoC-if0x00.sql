select if (exists ( select * from actor where first_name is not null and last_name = "GUINES" ), 'ESSE CARA EXIST', 'ESSE CARA NÃO EXITE';);
  