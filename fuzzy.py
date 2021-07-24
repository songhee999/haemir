def fuzzy_control():

    distance = ctrl.Antecedent(np.arange(0, 6, 0.1), 'distance')
    angle = ctrl.Antecedent(np.arange(-50, 50, 1), 'angle')
    target_angle = ctrl.Consequent(np.arange(-80, 80, 1), 'target_angle')

    distance['ED'] = fuzz.trimf(distance.universe, [0, 1, 2])
    distance['D'] = fuzz.trimf(distance.universe, [1, 2, 3])
    distance['W'] = fuzz.trimf(distance.universe, [2, 3, 4])
    distance['B'] = fuzz.trimf(distance.universe, [3, 4, 5]) 
    distance['S'] = fuzz.trimf(distance.universe, [4, 5, 6])
    distance['ES'] = fuzz.trimf(distance.universe, [5, 6, 6])

    angle['NL'] = fuzz.trimf(angle.universe, [-50, -50, -30])
    angle['NM'] = fuzz.trimf(angle.universe, [-50, -30, -10])
    angle['NS'] = fuzz.trimf(angle.universe, [-30, -10, 10])
    angle['PS'] = fuzz.trimf(angle.universe, [-10, 10, 30])
    angle['PM'] = fuzz.trimf(angle.universe, [10, 30, 50])
    angle['PL'] = fuzz.trimf(angle.universe, [30, 50, 50])

    print('target_angle universe :' , target_angle.universe)

    target_angle['LLL'] = fuzz.trimf(target_angle.universe, [-15, -15, -10])
    target_angle['LL'] = fuzz.trimf(target_angle.universe, [-15, -10, -5])
    target_angle['L'] = fuzz.trimf(target_angle.universe, [-10, -5, 0])
    target_angle['N'] = fuzz.trimf(target_angle.universe, [-5, 0, 5])
    target_angle['R'] = fuzz.trimf(target_angle.universe, [0, 5, 10])
    target_angle['RR'] = fuzz.trimf(target_angle.universe, [5, 10, 15])
    target_angle['RRR'] = fuzz.trimf(target_angle.universe, [10, 15, 15])

    rule_ED_NL = ctrl.Rule(distance['ED'] & angle['NL'], target_angle['LLL'])
    rule_ED_NM = ctrl.Rule(distance['ED'] & angle['NM'], target_angle['LLL'])
    rule_ED_NS = ctrl.Rule(distance['ED'] & angle['NS'], target_angle['LLL'])
    rule_ED_PS = ctrl.Rule(distance['ED'] & angle['PS'], target_angle['RRR'])
    rule_ED_PM = ctrl.Rule(distance['ED'] & angle['PM'], target_angle['RRR'])
    rule_ED_PL = ctrl.Rule(distance['ED'] & angle['PL'], target_angle['RRR'])

    rule_ED_NL = ctrl.Rule(distance['D'] & angle['NL'], target_angle['LL'])
    rule_ED_NM = ctrl.Rule(distance['D'] & angle['NM'], target_angle['LLL'])
    rule_ED_NS = ctrl.Rule(distance['D'] & angle['NS'], target_angle['LLL'])
    rule_ED_PS = ctrl.Rule(distance['D'] & angle['PS'], target_angle['RRR'])
    rule_ED_PM = ctrl.Rule(distance['D'] & angle['PM'], target_angle['RRR'])
    rule_ED_PL = ctrl.Rule(distance['D'] & angle['PL'], target_angle['RR'])
