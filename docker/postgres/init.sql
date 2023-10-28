-- Connect to the 'verser' database.
\c verser;

-- Create the table if it doesn't exist.
CREATE TABLE IF NOT EXISTS policies (
    id SERIAL PRIMARY KEY,
    policy_number VARCHAR(255) NOT NULL,
    policy_name VARCHAR(255) NOT NULL,
    policy_branch VARCHAR(255) NOT NULL,
    policy_type VARCHAR(255) NOT NULL,
    policy_text TEXT NOT NULL,
    policy_date_published DATE NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
