SELECT kurtosis(inflation_rate)as k_inflation,
skewness(inflation_rate)as s_inflation_rate,
count(*) as count_rows,
max(inflation_rate) as max_rate,
min(inflation_rate) as min_rate,
avg(inflation_rate)as avg_rate,
quantile_cont(inflation_rate,0.25) as QT1,
quantile_cont(inflation_rate,0.50) as Median,
quantile_cont(inflation_rate,0.75) as QT3,
quantile_cont(inflation_rate,0.75) - quantile_cont(inflation_rate,0.25) as IQR
FROM fred;
