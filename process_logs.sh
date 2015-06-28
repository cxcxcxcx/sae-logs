cat acc*/* | goaccess  --log-format='%^ %h %^ %T [%d:%t %^] %^ %^ %^ %m %U %H %s %b "%R" "%u" %^' --date-format='%d/%b/%Y' --time-format='%H:%M:%S' -a > summary.html
