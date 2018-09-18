#!/usr/bin/env python

import random as rn
import tools.superdict as sd
import math
import numpy as np
# Here we will simulate data for testing the model.


def empty_data():
    return {
        'machines': {
            m: {
                'maintenances': {
                    p: {
                        'maint_duration': 0 # G_np
                        , 'remaining_maint': 0  # G_np
                        , 'remaining_usage': 0  # Y_np
                    } for p in range(1)
                }
                , 'initial_state': 0  # unavailable (0) or available (1)
                , 'station': ''  # E_n
                , 'operations': []  # B_no
            } for m in range(1)
        }
        , 'maintenances': {
            p: {
                'usage': 0  # Y_p
            } for p in range(1)
        }
        , 'operations': {
            o: {
                'time': {
                    t: {
                        'demand': 0  # R_ot
                    } for t in range(1)
                }
            } for o in range(1)
        }
        , 'stations': {
            st: {
                'capacity': 0  # C_m
            } for st in range(1)
        }
        , 'time': {
            t: {
                'hours': 0  # H_t
            } for t in range(1)
        }
        , 'parameters': {
            'max_hours': 0  # X_max
            , 'min_rem_usage': 0  # Y_min
            , 'min_rem_maint': 0  # G_min
        }
    }


def generate_data(num_machines, num_operations=3, num_stations=3):
    num_operations = 3
    num_stations = 3
    num_machines = 50

    input_data = {}

    maint_intervals = [125, 300, 500]
    hour_dispo = [329, 348, 354, 344, 326, 335]

    maintenances = range(len(maint_intervals))
    periods = range(len(hour_dispo))
    operations = range(num_operations)
    stations = range(num_stations)
    machines = range(num_machines)

    maint_cap_perc_min = 0.20
    maint_cap_perc_max = 0.60

    prob_in_maint = 0.1

    min_init_rem_maint = 5
    min_init_rem_usage = 3

    input_data['stations'] = {
        st: {'capacity':
            rn.randrange(
                math.ceil(maint_cap_perc_min * num_machines),
                math.ceil(maint_cap_perc_max * num_machines)
            )
        } for st in stations
    }

    initially_working = {
        m: np.random.choice(2, p=[prob_in_maint, 1 - prob_in_maint])
        for m in machines
    }

    input_data['parameters'] = {'max_hours': 60, 'min_rem_usage': 0.1, 'min_rem_maint': 0.1}

    d_maints = input_data['maintenances'] = \
        {p: {'usage': val, 'maint': 50 * (p + 1)} for p, val in enumerate(maint_intervals)}

    init_rem_usage_0 = rn.randrange(min_init_rem_usage, d_maints[0]['usage'])


    d_machines = input_data['machines'] = {
        m: {
            'maintenances': {
                p: {
                    'maint_duration': 50 * (p + 1)
                    , 'remaining_maint': rn.randrange(
                        min_init_rem_maint, d_maints[p]['maint']
                    ) if not initially_working[m] else 0
                    , 'remaining_usage':
                        init_rem_usage_0
                        + d_maints[p]['usage'] - d_maints[0]['usage']
                        - rn.randrange(0, p + 1)*d_maints[0]['usage']
                        if initially_working[m] else 0
                } for p in maintenances
            }
            , 'initial_state': initially_working[m]
            , 'station': rn.choice(stations)
            # Each resource has at least one (random) task.
            # With 30% prob: the resource gets each of the other tasks.
            , 'operations': set(
                rn.sample(operations, 1) +
                [np.random.choice([None, o], p=[0.7, 0.3]) for o in operations]
            ).difference({None})

        } for m in machines
    }
    # station_len = \
    #     sd.SuperDict(d_machines). \
    #     index_by_property('station').\
    #     to_lendict()

    input_data['operations'] = {
        o: {
            'time': {
                t: {'demand': rn.randrange(20, 40)} for t in periods
            }
        } for o in operations
    }
    input_data['time'] = {t: val for t, val in enumerate(hour_dispo)}
    # input_data['stations'] = {
    #     st: {'capacity': math.ceil(maint_cap_perc * station_len[st])} for st in stations
    # }

    return input_data

