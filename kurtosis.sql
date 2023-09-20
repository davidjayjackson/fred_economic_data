 SELECT -- kurtosis(inflation_rate)as k_inflation,
 -- kurtosis(treasury_rate)as k_treasury,
 --  kurtosis(mortgage_rate)as k_mortgage,
 -- kurtosis(umployment_rate)as k_umployment,
 -- skewness(inflation_rate)as s_inflation,
 skewness(treasury_rate)as s_treasury,
 skewness(mortgage_rate)as s_mortgage,
 skewness(umployment_rate)as s_umployment
 FROM fred;