 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:03:00 2023

@author: bruno parente
"""


def check_conformidade(inst, v_nom, v_s, err, sist):
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
        if sist:
            if err > evs_s:
                conf = False
            else:
                conf = True
        else:
            if err > evs_a:
                conf = False
            else:
                conf = True
        return conf
