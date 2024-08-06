# 创建交易时间字典
trading_hours = {
    'CU': ['15:00', '01:00'],
    'CU-C/P': ['15:00', '01:00'],
    'AL': ['15:00', '01:00'],
    'AL-C/P': ['15:00', '01:00'],
    'PB': ['15:00', '01:00'],
    'ZN': ['15:00', '01:00'],
    'ZN-C/P': ['15:00', '01:00'],
    'SN': ['15:00', '01:00'],
    'NI': ['15:00', '01:00'],
    'SS': ['15:00', '01:00'],
    'AU': ['15:00', '02:30'],
    'AG': ['15:00', '02:30'],
    'AU-C/P': ['15:00', '02:30'],
    'RB': ['15:00', '23:00'],
    'HC': ['15:00', '23:00'],
    'BU': ['15:00', '23:00'],
    'RU': ['15:00', '23:00'],
    'FU': ['15:00', '23:00'],
    'SP': ['15:00', '23:00'],
    'RU-C/P': ['15:00', '23:00'],
    'WR': ['15:00', None],  # 无夜盘交易
    'A': ['15:00', '23:00'],
    'B': ['15:00', '23:00'],
    'M': ['15:00', '23:00'],
    'M-C/P': ['15:00', '23:00'],
    'Y': ['15:00', '23:00'],
    'P': ['15:00', '23:00'],
    'I': ['15:00', '23:00'],
    'J': ['15:00', '23:00'],
    'JM': ['15:00', '23:00'],
    'C': ['15:00', '23:00'],
    'CS': ['15:00', '23:00'],
    'L': ['15:00', '23:00'],
    'V': ['15:00', '23:00'],
    'PP': ['15:00', '23:00'],
    'EG': ['15:00', '23:00'],
    'C-C/P': ['15:00', '23:00'],
    'RR': ['15:00', '23:00'],
    'EB': ['15:00', '23:00'],
    'I-C/P': ['15:00', '23:00'],
    'PG': ['15:00', '23:00'],
    'PG-CP': ['15:00', '23:00'],
    'L-C/P': ['15:00', '23:00'],
    'V-C/P': ['15:00', '23:00'],
    'PP-C/P': ['15:00', '23:00'],
    'P-C/P': ['15:00', '23:00'],
    'JD': ['15:00', None],  # 无夜盘交易
    'FB': ['15:00', None],  # 无夜盘交易
    'BB': ['15:00', None],  # 无夜盘交易
    'LH': ['15:00', None],  # 无夜盘交易
    'RM': ['15:00', '23:00'],
    'OI': ['15:00', '23:00'],
    'CF': ['15:00', '23:00'],
    'TA': ['15:00', '23:00'],
    'SR': ['15:00', '23:00'],
    'SR-C/P': ['15:00', '23:00'],
    'MA': ['15:00', '23:00'],
    'FG': ['15:00', '23:00'],
    'ZC': ['15:00', '23:00'],
    'CY': ['15:00', '23:00'],
    'CF-C/P': ['15:00', '23:00'],
    'SA': ['15:00', '23:00'],
    'TA-C/P': ['15:00', '23:00'],
    'MA-C/P': ['15:00', '23:00'],
    'RM-C/P': ['15:00', '23:00'],
    'ZC-C/P': ['15:00', '23:00'],
    'PF': ['15:00', '23:00'],
    'JR': ['15:00', None],  # 无夜盘交易
    'RS': ['15:00', None],  # 无夜盘交易
    'PM': ['15:00', None],  # 无夜盘交易
    'WH': ['15:00', None],  # 无夜盘交易
    'RI': ['15:00', None],  # 无夜盘交易
    'LR': ['15:00', None],  # 无夜盘交易
    'SF': ['15:00', None],  # 无夜盘交易
    'SM': ['15:00', None],  # 无夜盘交易
    'AP': ['15:00', None],  # 无夜盘交易
    'CJ': ['15:00', None],  # 无夜盘交易
    'UR': ['15:00', None],  # 无夜盘交易
    'PK': ['15:00', None],  # 无夜盘交易
    'PX': ['15:00', None],  # 无夜盘交易
    'SH': ['15:00', None],  # 无夜盘交易
    'IF': ['15:00', None],  # 无夜盘交易
    'IH': ['15:00', None],  # 无夜盘交易
    'IC': ['15:00', None],  # 无夜盘交易
    'IO-C/P': ['15:00', None],  # 无夜盘交易
    'TF': ['15:15', None],  # 无夜盘交易
    'T': ['15:15', None],  # 无夜盘交易
    'TS': ['15:15', None],  # 无夜盘交易
    'SC': ['15:00', '02:30'],
    'SC-C/P': ['15:00', '02:30'],
    'NR': ['15:00', '23:00'],
    'LU': ['15:00', '23:00'],
    'BC': ['15:00', '01:00'],
    'SI': ['15:00', None],  # 无夜盘交易
    'LC': ['15:00', None],  # 无夜盘交易
}

# 查询函数
def get_trading_end_time(code, session):
  if code in trading_hours:
    if session == 'day':
      return trading_hours[code][0]
    elif session == 'night':
      return trading_hours[code][1]
    else:
      return "无效的交易时段。请选择 'day' 或 'night'"
  else:
    return "合约代码不存在"