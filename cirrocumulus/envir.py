CIRRO_TEST = "CIRRO_TEST"  # whether running using pytest
# authentication/authorization
CIRRO_AUTH_CLIENT_ID = "CIRRO_AUTH_CLIENT_ID"
CIRRO_AUTH_ISSUER = "CIRRO_AUTH_ISSUER"
CIRRO_AUTH = "CIRRO_AUTH"  # python class to validate tokens (created based on CIRRO_AUTH_PROVIDER)
CIRRO_AUTH_PROVIDER = "CIRRO_AUTH_PROVIDER"  # okta, google

CIRRO_DB_URI = "CIRRO_DB_URI"
CIRRO_EMAIL = "CIRRO_EMAIL"
CIRRO_SERVE = "CIRRO_SERVE"
CIRRO_MAX_WORKERS = "CIRRO_MAX_WORKERS"
CIRRO_FOOTER = "CIRRO_FOOTER"
CIRRO_BRAND = "CIRRO_BRAND"
CIRRO_UPLOAD = "CIRRO_UPLOAD"

CIRRO_COMPRESS = "CIRRO_COMPRESS"
CIRRO_JOB_RESULTS = "CIRRO_JOB_RESULTS"  # job result storage location
CIRRO_DATABASE_CLASS = "CIRRO_DATABASE_CLASS"
CIRRO_DATABASE = "CIRRO_DATABASE"
CIRRO_DATASET_PROVIDERS = "CIRRO_DATASET_PROVIDERS"

CIRRO_MIXPANEL = "CIRRO_MIXPANEL"
# for mounting a bucket locally. Comma separated string of bucket:local_path. Example s3://foo/bar:/fsx
CIRRO_MOUNT = "CIRRO_MOUNT"
CIRRO_LOG_LEVEL = "CIRRO_LOG_LEVEL"
# columns to display to user
CIRRO_DATASET_SELECTOR_COLUMNS = "CIRRO_DATASET_SELECTOR_COLUMNS"
CIRRO_JOB_TYPE = "CIRRO_JOB_TYPE"

# path to JSON file for library list when adding new dataset
CIRRO_LIBRARY = "CIRRO_LIBRARY"

# path to JSON file for species list when adding new dataset
CIRRO_SPECIES = "CIRRO_SPECIES"
# path to OBO file
CIRRO_CELL_ONTOLOGY = "CIRRO_CELL_ONTOLOGY"

# comma separated list of paths to allow all logged in users to download from
CIRRO_STATIC_DIR = "CIRRO_STATIC_DIR"

# directory in server whose files can be available to user for direct selection
CIRRO_DATA_DIR = "CIRRO_DATA_DIR"

SERVER_CAPABILITY_RENAME_CATEGORIES = "SERVER_CAPABILITY_RENAME_CATEGORIES"
SERVER_CAPABILITY_JOBS = "SERVER_CAPABILITY_JOBS"
SERVER_CAPABILITY_FEATURE_SETS = "SERVER_CAPABILITY_FEATURE_SETS"
SERVER_CAPABILITY_LINKS = "SERVER_CAPABILITY_LINKS"
SERVER_CAPABILITY_EDIT_DATASET = "SERVER_CAPABILITY_EDIT_DATASET"
SERVER_CAPABILITY_ADD_DATASET = "SERVER_CAPABILITY_ADD_DATASET"
SERVER_CAPABILITY_DELETE_DATASET = "SERVER_CAPABILITY_DELETE_DATASET"
