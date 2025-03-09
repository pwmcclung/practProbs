SELECT
    e.employee_id,
    e.full_name,
    e.team,
    e.birth_date
FROM
    employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e2
    WHERE e2.team = e.team AND e2.birth_date > e.birth_date
)
ORDER BY team ASC;