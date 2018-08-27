#!/usr/bin/env python

import random as rn
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


def generate_data(num_machines, num_operations, num_stations):
    input_data = empty_data()
    maint_intervals = [125, 300, 500]
    maintenances = range(len(maint_intervals))
    hour_dispo = [329, 348, 354, 344, 326, 335]
    periods = range(len(hour_dispo))
    operations = range(num_operations)
    stations = range(num_stations)
    machines = range(num_machines)

    d_params = input_data['parameters'] = {'max_hours': 60, 'min_rem_usage': 0.1, 'min_rem_maint': 0.1}
    d_maints = input_data['maintenances'] = {p: {'usage': val} for p, val in enumerate(maint_intervals)}
    input_data['machines'] = {
        m: {
            'maintenances': {
                p: {
                    'maint_duration': 0  # TODO
                    , 'remaining_maint': rn.randrange(
                        d_params['min_rem_maint'], 0  # TODO
                    )
                    , 'remaining_usage': rn.randrange(
                        d_params['min_rem_usage'], d_maints[p]['usage']
                    )
                } for p in maintenances
            }
            , 'station': rn.choice(stations)
            , 'operations': rn.sample(operations)

        } for m in machines
    }

    input_data['operations'] = {
        o: {
            'time': {
                t: {'demand': rn.randint(20, 40)} for t in periods
            }
        } for o in operations
    }
    input_data['time'] = {t: val for t, val in enumerate(hour_dispo)}
    input_data['stations'] = {
        st: {'capacity': 0} for st in stations
    }
    # num_machines

    return {}