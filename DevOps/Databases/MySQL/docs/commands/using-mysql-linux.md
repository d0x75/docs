Backup Mysql Linux
---------------------

``
mysqldump -u root -p -x -e --routines -B erp_name | sed -e 's/DEFINER=`.*`@`.*`\ //g' | gzip > local.sql.gz
``

