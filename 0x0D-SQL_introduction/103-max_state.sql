-- gives the max tmp for a state ordered by the name
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state
