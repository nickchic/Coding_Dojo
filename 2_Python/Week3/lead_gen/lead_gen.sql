-- 1. What query would you run to get the total revenue for March of 2012?

SELECT SUM(amount)
FROM billing
WHERE MONTH(charged_datetime) = 3 AND YEAR(charged_datetime) = 2012
GROUP BY MONTH(charged_datetime);

-- 2. What query would you run to get total revenue collected from the client with an id of 2?

SELECT SUM(amount)
FROM billing
WHERE client_id = 2
GROUP BY client_id;

-- 3. What query would you run to get all the sites that client=10 owns?

SELECT domain_name
FROM sites
WHERE client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client 
-- with an id of 1? What about for client=20?

SELECT COUNT(site_id), MONTHNAME(created_datetime), YEAR(created_datetime)
FROM sites
WHERE client_id = 20
GROUP BY MONTH(created_datetime) AND YEAR(created_datetime);

-- 5. What query would you run to get the total # of leads generated for each of the sites between 
-- January 1, 2011 to February 15, 2011?

SELECT COUNT(leads_id), sites.domain_name
FROM sites
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= '2011/01/01' and leads.registered_datetime <= '2011/02/15'
GROUP BY sites.site_id;

-- 6. What query would you run to get a list of client names and the total # of leads we've generated 
-- for each of our clients between January 1, 2011 to December 31, 2011?

SELECT COUNT(leads_id), clients.first_name, clients.last_name
FROM sites
LEFT JOIN leads
ON sites.site_id = leads.site_id
LEFT JOIN clients
ON sites.client_id = clients.client_id
WHERE leads.registered_datetime >= '2011/01/01' and leads.registered_datetime <= '2011/12/31'
GROUP BY clients.client_id;

-- 7. What query would you run to get a list of client names and the total # of leads we've generated 
-- for each client each month between months 1 - 6 of Year 2011?

SELECT clients.first_name, clients.last_name, COUNT(leads_id), MONTHNAME(leads.registered_datetime)
FROM clients
LEFT JOIN sites
ON sites.client_id = clients.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE MONTH(leads.registered_datetime) >= 1 AND MONTH(leads.registered_datetime) <= 6 AND YEAR(leads.registered_datetime) = 2011
GROUP BY clients.client_id, leads.registered_datetime;

-- 8. What query would you run to get a list of client names and the total # of leads we've generated 
-- for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  
-- Come up with a second query that shows all the clients, the site name(s), and the total number of leads 
-- generated from each site for all time.

SELECT clients.client_id, clients.first_name, clients.last_name, sites.domain_name,COUNT(leads_id)
FROM clients
LEFT JOIN sites
ON sites.client_id = clients.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
WHERE leads.registered_datetime >= '2011/01/01' and leads.registered_datetime <= '2011/12/31'
GROUP BY clients.client_id, sites.site_id
ORDER BY clients.client_id;

SELECT clients.client_id, clients.first_name, clients.last_name, sites.domain_name,COUNT(leads_id)
FROM clients
LEFT JOIN sites
ON sites.client_id = clients.client_id
LEFT JOIN leads
ON sites.site_id = leads.site_id
GROUP BY clients.client_id, sites.site_id
ORDER BY clients.client_id;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of 
-- the year. Order it by client id.

SELECT clients.client_id, clients.first_name, clients.last_name, SUM(amount)
FROM billing
LEFT JOIN clients
ON billing.client_id = clients.client_id
GROUP BY clients.client_id, MONTH(billing.charged_datetime), YEAR(billing.charged_datetime)
ORDER BY clients.client_id;

-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so 
-- that each row shows a new client. It will become clearer when you add a new field called 'sites' that 
-- has all the sites that the client owns. (HINT: use GROUP_CONCAT)

SELECT clients.client_id, clients.first_name, clients.last_name, GROUP_CONCAT(' ', sites.domain_name)
FROM clients
LEFT JOIN sites
ON sites.client_id = clients.client_id
GROUP BY clients.client_id
ORDER BY clients.client_id;