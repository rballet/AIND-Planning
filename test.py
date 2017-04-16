from itertools import permutations, product

def expr(a):
    return a

A = ['A1','A2','A3']
A2 = []
B = ['B1','B2','B3']
C = ['C1','C2','C3']

#R = list(product(A,B,C))

#perm = list(permutations(A,2))

#action_list = []
#var_prod = list(product(A,B,C))
#action_list += ['Load({},{},{})'.format(var[0], var[1], var[2]) for var in var_prod]
#action_list += ['Unload({},{},{})'.format(var[0], var[1], var[2]) for var in var_prod]

#fly_temp = list(product(B, permutations(A,2)))
#action_list += ['Fly({},{},{})'.format(var[0], var[1][0], var[1][1]) for var in fly_temp]
cargos = ['C1', 'C2', 'C3']
planes = ['P1', 'P2', 'P3']
airports = ['JFK', 'SFO', 'ATL']

fluent_c_at = [expr('At({}, {})'.format(var[0],var[1]))
                    for var in product(cargos,airports)]
fluent_in = [expr('In({}, {})'.format(var[0],var[1]))
                  for var in product(cargos,planes)]
fluent_p_at = [expr('At({}, {})'.format(var[0], var[1]))
                    for var in product(planes, airports)]
fluent_set = set(fluent_c_at + fluent_in + fluent_p_at)

pos = [expr('At(C1, SFO)'),
       expr('At(C2, JFK)'),
       expr('At(C3, ATL)'),
       expr('At(P1, SFO)'),
       expr('At(P2, JFK)'),
       expr('At(P3, ATL)'),
       ]
neg = list(fluent_set - set(pos))

goal = [expr('At(C1, JFK)'),
        expr('At(C2, SFO)'),
        expr('At(C3, SFO)'),
        ]

neg2 = ['At(C3, SFO)',
        'At(C3, JFK)',
        'In(C3, P1)',
        'In(C3, P2)',
        'In(C3, P3)',
        'At(C2, SFO)',
        'At(C2, ATL)',
        'In(C2, P1)',
        'In(C2, P2)',
        'In(C2, P3)',
        'At(C1, JFK)',
        'At(C1, ATL)',
        'In(C1, P1)',
        'In(C1, P2)',
        'In(C1, P3)',
        'At(P1, JFK)',
        'At(P1, ATL)',
        'At(P2, SFO)',
        'At(P2, ATL)',
        'At(P3, SFO)',
        'At(P3, JFK)',
         ]
print(neg)
print(all(n in neg2 for n in neg))