USE california_collisions;

-- DS QUESTION:
-- Are old vehicles more likely to be at fault for collisions?

SELECT * FROM parties LIMIT 10;

-- UPDATED DS QUESTION:
-- Are vehicles old for their vehicle make more likely to be at fault for collisions?

SELECT vehicle_make, COUNT(*) FROM parties GROUP BY vehicle_make;

CREATE OR REPLACE VIEW parties_vehicles_cleaned AS (
	SELECT
		case_id,
		party_number,
		at_fault,
		vehicle_make,
		vehicle_year
	FROM parties
	WHERE vehicle_year > 0 AND vehicle_make != '');

SELECT * FROM parties_vehicles_cleaned;

-- Solution Approach:
-- Add a column ind_old_vehicle to the above, which is 1 if the party's vehicle is old in comparison to other vehicles of its make
-- Group by at_fault and find average of ind_old_vehicle

-- Q1
-- Add a new column for each party, avg_vehicle_year_for_make
-- This column is the avg year for vehicles of that party's vehicle make


-- Q2
-- Add another column to parties_vehicles_cleaned, indicating if the party's vehicle is old in comparison to other vehicles of its make
-- This column (ind_old_vehicle) is 1 if vehicle_year < avg_vehicle_year_for_make, and 0 if it is not



-- Q3
-- Find out if at_fault vehicles are more likely to be old
-- Group above table by at_fault, find the average of the feature ind_old_vehicle
