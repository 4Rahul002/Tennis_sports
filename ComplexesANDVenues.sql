# Queries for Complexes and Venues
# List all venues along with their associated complex name:

SELECT v.venue_name, c.complex_name
FROM Venues v
JOIN Complexes c ON v.complex_id = c.complex_id;

# Count the number of venues in each complex:

SELECT c.complex_name, COUNT(v.venue_id) AS number_of_venues
FROM Complexes c
LEFT JOIN Venues v ON c.complex_id = v.complex_id
GROUP BY c.complex_name;

# Get details of venues in a specific country (e.g., Chile):

SELECT v.venue_name, v.timezone
FROM Venues v
WHERE v.country_name = 'Chile';

# Identify all venues and their timezones:
 
SELECT venue_name, timezone
FROM Venues;

# Find complexes that have more than one venue:
 
SELECT c.complex_name, COUNT(v.venue_id) AS number_of_venues
FROM Complexes c
LEFT JOIN Venues v ON c.complex_id = v.complex_id
GROUP BY c.complex_name
HAVING COUNT(v.venue_id) > 1;

# List venues grouped by country:
 
SELECT country_name, GROUP_CONCAT(venue_name) AS venues
FROM Venues
GROUP BY country_name;

# Find all venues for a specific complex (e.g., Nacional):
 
SELECT v.venue_name
FROM Venues v
JOIN Complexes c ON v.complex_id = c.complex_id
WHERE c.complex_name = 'Nacional';