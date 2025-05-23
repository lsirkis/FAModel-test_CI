
from anchor_map import Anchor

# --- Define soil profile ---
profile_map = [
    {
        'name': 'CPT_D1',
        'x': 0.0, 'y': 0.0,
        'layers': [
            {'top':  1.0, 'bottom':  6.0, 'soil_type': 'clay', 'gamma_top':  9.0, 'gamma_bot': 10.0, 'Su_top': 45, 'Su_bot':  60},
            {'top':  6.0, 'bottom': 15.0, 'soil_type': 'clay', 'gamma_top': 10.0, 'gamma_bot': 10.0, 'Su_top': 60, 'Su_bot':  80},
            {'top': 15.0, 'bottom': 35.0, 'soil_type': 'clay', 'gamma_top': 10.0, 'gamma_bot': 10.5, 'Su_top': 80, 'Su_bot': 100}
        ]
    }
]

# --- Create driven pile anchor ---
anchor = Anchor(
    dd = {
        'type': 'driven',
        'design': {
            'L': 25.0,        # Embedded length
            'D': 2.0,         # Diameter
            'zlug': 10.0      # Padeye depth
        }
    },
    r = [0.0, 0.0, 0.0]
)

# Assign mooring loads
anchor.loads = {
    'Hm': 4.0e6,
    'Vm': 2.5e6
}
anchor.line_type = 'chain'
anchor.d = 0.16
anchor.w = 5000.0

# Assign local soil
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

# --- Step 2: Capacity ---
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
for key, val in anchor.capacity_results.items():
    print(f'{key}: {val:.2f}')
