CREATE TABLE IF NOT EXISTS policies (
    id serial PRIMARY KEY,
    policy_id VARCHAR(50),
    policy_name VARCHAR(100),
    policy_branch VARCHAR(100),
    policy_type VARCHAR(100),
    policy_url VARCHAR(1000),
    policy_text text
    )
;