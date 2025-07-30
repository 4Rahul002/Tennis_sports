
#Queries for Rankings and Competitors

# Get all competitors with their rank and points:

SELECT c.name, cr.rank, cr.points
FROM Competitor c
JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id;

#Find competitors ranked in the top 5:

SELECT c.name, cr.rank, cr.points
FROM Competitor c
JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
WHERE cr.rank <= 5;

# List competitors with no rank movement (stable rank):

SELECT c.name, cr.rank
FROM Competitor c
JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
WHERE cr.movement = 0;

# Get the total points of competitors from a specific country (e.g., Croatia):

SELECT SUM(cr.points) AS total_points
FROM Competitor c
JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
WHERE c.country = 'Croatia';

# Count the number of competitors per country:

SELECT c.country, COUNT(*) AS number_of_competitors
FROM Competitor c
GROUP BY c.country;

# Find competitors with the highest points in the current week:
#To find competitors with the highest points, you can use a subquery to determine the maximum points 
#and then find competitors with those points:


SELECT c.name, cr.points
FROM Competitor c
JOIN Competitor_Rankings cr ON c.competitor_id = cr.competitor_id
WHERE cr.points = (SELECT MAX(points) FROM Competitor_Rankings);