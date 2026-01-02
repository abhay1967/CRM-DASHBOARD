create database crm_db;
use crm_db;
-- Top 100 High-Value Leads
SELECT 
    l.lead_id,
    l.lead_name,
    l.industry,
    d.deal_size
FROM leads l
JOIN deals d ON l.lead_id = d.lead_id
ORDER BY d.deal_size DESC
LIMIT 100;
-- Lead Aging (KPI)
SELECT 
    lead_id,
    lead_name,
    DATEDIFF(CURDATE(), created_date) AS lead_age_days
FROM leads;
-- Conversion Rate
SELECT 
    COUNT(CASE WHEN status = 'Converted' THEN 1 END) * 100.0 / COUNT(*) 
    AS conversion_rate_percentage
FROM leads;

-- Source Effectiveness
SELECT 
    source,
    COUNT(*) AS total_leads
FROM leads
GROUP BY source
ORDER BY total_leads DESC;

-- Industry-wise Deal Value
SELECT 
    l.industry,
    SUM(d.deal_size) AS total_deal_value
FROM leads l
JOIN deals d ON l.lead_id = d.lead_id
GROUP BY l.industry;

-- Engagement Count per Lead
SELECT 
    lead_id,
    COUNT(*) AS total_activities
FROM activities
GROUP BY lead_id;











