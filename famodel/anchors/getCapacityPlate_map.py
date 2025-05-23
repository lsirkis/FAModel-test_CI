
from anchor_map import Anchor
import numpy as np
from famodel.anchors.anchors_famodel_map.capacity_plots_map import plot_load

# --- Define soil profile ---
profile_map = [
    {
        'name': 'CPT_A1',
        'x': 0.0, 'y': 0.0,
        'layers': [
            {'top':  2.0, 'bottom':  4.0, 'soil_type': 'clay', 'gamma_top':  8.0, 'gamma_bot':  8.5, 'Su_top':  10, 'Su_bot':  25},
            {'top':  4.0, 'bottom':  6.0, 'soil_type': 'clay', 'gamma_top':  8.5, 'gamma_bot':  9.0, 'Su_top':  25, 'Su_bot':  50},
            {'top':  6.0, 'bottom': 16.0, 'soil_type': 'clay', 'gamma_top':  9.0, 'gamma_bot':  9.5, 'Su_top':  50, 'Su_bot': 100},
            {'top': 16.0, 'bottom': 25.0, 'soil_type': 'clay', 'gamma_top':  9.5, 'gamma_bot':  9.5, 'Su_top': 100, 'Su_bot': 100}
        ]
    }
]

# --- Create plate anchor ---
anchor = Anchor(
    dd = {'type': 'plate', 'design': {'B': 3.0, 'L': 6.0, 'zlug': 5.0, 'beta': 30.0}},
    r = [100.0, 100.0, 0.0]
)

# --- Assign load and mooring properties ---
anchor.loads = {
    'Hm': 2.5e6,
    'Vm': 1.5e6
}
anchor.line_type = 'chain'
anchor.d = 0.16
anchor.w = 5000.0

# --- Set soil profile based on anchor location ---
anchor.setSoilProfile(profile_map)

# --- Step 1: Lug Forces ---
layers, Ha, Va = anchor.getLugForces(
    Hm = anchor.loads['Hm'],
    Vm = anchor.loads['Vm'],
    zlug = anchor.dd['design']['zlug'],
    line_type = anchor.line_type,
    d = anchor.d,
    w = anchor.w,
    plot = True
)

print('\nLug Forces Computed:')
print(f'Ha = {Ha:.2f} N')
print(f'Va = {Va:.2f} N')

# --- Step 2: Capacity Evaluation ---
anchor.getCapacityAnchor(
    Hm = anchor.loads['Hm'],
    Vm = anchor.loads['Vm'],
    zlug = anchor.dd['design']['zlug'],
    line_type = anchor.line_type,
    d = anchor.d,
    w = anchor.w,
    plot = True
)

print('\nCapacity Results:')
for key, value in anchor.capacity_results.items():
    print(f'{key}: {value:.2f}')
