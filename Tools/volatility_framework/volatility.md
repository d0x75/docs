Volatility Framework
---------------------


### Analisar um dump total, com Volatility


		volatility.exe -f C:\dump.dmp pslist ( ver os processos startados no momento do dump )

		volatility.exe -f C:\dump.dmp connections

		volatility.exe -f C:\dump.dmp imageinfo

		volatility.exe -f C:\dump.dmp dlllist

		volatility.exe -f C:\dump.dmp dlllist -p 668 ( 668 = especificando o PID do processo )

		volatility.exe -f C:\dump.dmp dlldump -p 668 --dump-dir C:\temp



