


@echo off

set pis_root=%1
set ai1=%2
set ai2=%3


set out_file=%4
set opening_idx=%5




echo outfile: %out_file%
echo opening_idx: %opening_idx%

%pis_root%\piskvork.exe -p %ai1% %ai2% -outfile %out_file% -outfileformat 2 -opening %opening_idx%
