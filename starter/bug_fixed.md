
# Bugs and Error Resolution
## Task 2
1. Import error: from models OrbitPath, NearEarthObject

Reslolution: from .models import Orbith, NearEarthObject

## Task 3 

1. Failed test cases

- ERROR: test_find_unique_number_between_dates_with_diameter (tests.test_neo_database.TestNEOSearchUseCases)
AttributeError: 'NearEarthObject' object has no attribute 'diameter_min_km'

- Resolution: Rename attribute in NearEarthObject model to `diameter_min_km`

2. 
- ERROR: test_find_unique_number_between_dates_with_diameter_and_hazardous_and_distance (tests.test_neo_database.TestNEOSearchUseCases)

AttributeError: 'OrbitPath' object has no attribute 'neo_name'

- Resolution: Rename an attribute `name` in OrbitPath to `neo_name`