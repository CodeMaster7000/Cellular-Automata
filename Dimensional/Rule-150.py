import numpy as np
def cellular_automaton(rule_number, size, steps,
                       init_cond='random', impulse_pos='center'):
    assert 0 <= rule_number <= 255
    assert init_cond in ['random', 'impulse']
    assert impulse_pos in ['left', 'center', 'right']
    rule_binary_str = np.binary_repr(rule_number, width=8)
    rule_binary = np.array([int(ch) for ch in rule_binary_str], dtype=np.int8)
    x = np.zeros((steps, size), dtype=np.int8)
    if init_cond == 'random':  
        x[0, :] = np.array(np.random.rand(size) < 0.5, dtype=np.int8)
    if init_cond == 'impulse':  
        if impulse_pos == 'left':
            x[0, 0] = 1
        elif impulse_pos == 'right':
            x[0, size - 1] = 1
        else:
            x[0, size // 2] = 1
    for i in range(steps - 1):
        x[i + 1, :] = step(x[i, :], rule_binary)
    return x
