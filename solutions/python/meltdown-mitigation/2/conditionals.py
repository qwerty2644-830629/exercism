def is_criticality_balanced(temperature, neutrons_emitted): # temperature(溫度(K))
    # neutrons_emitted(每秒發射的中子)
    
    flag = False
    if (temperature < 800) and (neutrons_emitted > 500) and (temperature * neutrons_emitted < 500000):
        # 溫度 <= 800K ， 每秒發射的中子 > 500顆 ，溫度 * 每秒發射中子 < 50萬
        flag = True        
    return flag
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    # voltage value(電壓值) current value(電流值) 電壓值theoretical_max_power(最大功率)
    efficiency_state = ["green", "orange", "red", "black"] # 效率狀態階段
    efficiency = (voltage * current) / theoretical_max_power * 100 #目前效率
    state = None # 狀態碼
    
    if efficiency >= 80:
        state = efficiency_state[0]
    elif efficiency >= 60:
        state = efficiency_state[1]
    elif efficiency >= 30:
        state = efficiency_state[2]
    else:
        state = efficiency_state[3]
    return state

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    # temperature(溫度(K)) neutrons_produced_per_second(每秒產生的中子數量) threshold(臨界值)
    reaction_rate = temperature * neutrons_produced_per_second  # 反應速率
    state = None
    
    if reaction_rate < (0.9 * threshold): # >90% LOW
        state = "LOW"
    elif reaction_rate <= 1.1 * threshold: # 90% ~ 110% NORMAL
        state = "NORMAL"
    else:
        state = "DANGER"
    return state
