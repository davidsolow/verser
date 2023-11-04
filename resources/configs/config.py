import os

# Define the root directory of your project (i.e., where the Airflow DAGs are located)
# This moves up two directories from config.py, which should put you in /opt/airflow/
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Function to easily construct paths relative to the project root
def get_project_root_relative_path(*args):
    """Construct a path relative to the project root."""
    return os.path.join(PROJECT_ROOT, *args)

# Define paths to various resources
SQL_DIRECTORY = get_project_root_relative_path('resources', 'sql')
CONFIGS_DIRECTORY = get_project_root_relative_path('resources', 'configs')
SCRIPTS_DIRECTORY = get_project_root_relative_path('resources', 'scripts')
