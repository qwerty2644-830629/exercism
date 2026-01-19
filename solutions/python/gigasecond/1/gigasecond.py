from datetime import datetime, timedelta

def add(birth_date):
    # 定義十億秒 (1,000,000,000)
    # 使用底線增加可讀性，或使用 1e9
    GIGASECOND = 1_000_000_000
    
    # 使用 timedelta 進行時間位移
    # timedelta 支持 weeks, days, hours, minutes, seconds 等參數
    return birth_date + timedelta(seconds=GIGASECOND)