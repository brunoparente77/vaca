 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:03:00 2023

@author: bruno parente
"""


def check_conformidade(inst, v_nom, v_s, err):
    if inst == "msa":
        if v_nom > 5000:
            e_vnom = [0.6, 0.3]
        elif v_nom > 50:
            e_vnom = [0.8, 0.3]
        elif v_nom > 10:
            e_vnom = [1.0, 0.5]
        elif v_nom > 5:
            e_vnom = [1.2, 0.8]
        elif v_nom > 3:
            e_vnom = [2.5, 1.5]
        else:
            e_vnom = [2.5, 2.0]
        evs_s = v_nom / v_s * e_vnom[0]
        evs_a = v_nom / v_s * e_vnom[1]
        conf = []
        if res[0] > evs_s:
            conf[0] = False
        else:
            conf[0] = True
        if res[1] > evs_a:
            conf[1] = False
        else:
            conf[1] = True
        return conf
