
#Bibliotecas
Import pandas as pd
from datetime import datetime
import time

#Instalando o suporte a Python no Metatrader5
!pip install Metatrader5
import Metatrader5 as mt5

#Conectando ao mt5
if not mt5.initialize():
    print ("initialize() failed")
    mt5.shutdown()
    
#Obtendo Cotações
def get_ohlc(ativo, timeframe, n=10):
    ativo = mt5.copy_rates_from_pos(ativo, timeframe, 0, n)
    ativo = pd.dataframe(ativo)
    ativo = ['time']=pd.to_datetime(ativo['time'], unit='s')
    ativo.set_index('time', inplace=true)
    return ativo
        
get_ohlc('WINQ20', MT5.TIMEFRAME_M1)

mt5.symbol_info_tick('WINQ20')

tempo = time.time() + 5
    while time.time() < tempo:
        tick = mt5.symbol_info_tick('WINQ20')._asdict()
        print(f"WINQ20:{tick['last']}, bid:{tick['bid']}, ask:{tick['ask']}")
        time.sleep(0.5)
        
## Enviando Ordens ##
#testando se o símbolo é válido
symbol = "WINQ20"
symbol_info = mt5.symbol_info(symbol)
if symbol_info as none:
    print(symbol, "não encontrado")
    mt5.shutdown()
    quit()
    
#Adicionando o símbolo se não estiver visível no marketwatch
if not symbol_info_visible:
    print(symbol, "Não esta visível, tentando adicionar")
    if not mt5_symbol_select(symbol, true):
        print("symbol_select({}{) failed, exit", symbol)
        mt5.shutdown()
        quit()
        
#Preparando a Ordem
lot = 1.0
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask
deviation = 20
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": price -100 * point, #stop loss
    "tp": price +150 * point, #take profit
    "deviation": deviation,
    "magic": 234000,
    "comment": "Python Script Open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLIING_RETURN,
}

#Enviando a Ordem
result = mt5.order_send(request)
