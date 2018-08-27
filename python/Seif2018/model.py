#!/usr/bin/env python

"""
Sets:

Machines
Maintenance types
Operations
Stations
Time periods

Constraints:

1. Guarantee all demand hours for each operation.
2. Each station has a max capacity.
3. Each maintenance has a min duration (an exact duration in our case).
4. There is a max usage between two maintenance of the same type
5. There is a global maximum in maintenance capacity, regardless of the station.

Params:

"""

