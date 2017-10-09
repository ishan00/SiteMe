set datafile separator ','
stats 'XXXXX' u 2 noout      # get STATS_sum (sum of column 2)

ang(x)=x*360.0/STATS_sum        # get angle (grades)
perc(x)=x*100.0/STATS_sum       # get percentage

set size square                 # square canvas
set xrange [-1:1.5]
set yrange [-1.25:1.25]
set style fill solid 1
set term png
set output 'YYYYY'

unset border
unset tics
unset key

Ai = 0.0; Bi = 0.0;             # init angle
mid = 0.0;                      # mid angle
i = 0; j = 0;                   # color
yi  = 1.3; yi2 = 1.3;           # label position

plot 'XXXXX' u (0):(0):(1):(Ai):(Ai=Ai+ang($2)):(i=i+1) with circle linecolor var,\
     'XXXXX' u (1):(yi=yi-0.6/STATS_records):($1) w labels left,\
     'XXXXX' u (0.9):(yi2=yi2-0.6/STATS_records):(j=j+1) w p pt 5 ps 2 linecolor var,\
     'XXXXX' u (mid=Bi+ang($2)*pi/360.0, Bi=2.0*mid-Bi, 0.5*cos(mid)):(0.5*sin(mid)):(sprintf('%.0f (%.1f\%)', $2, perc($2))) w labels


