import pandas as pd
from binance.client import Client
import streamlit as st
client = Client()

# Define ticker symbols
tickers = ['BTCUSDT','XRPUSDT','TRXUSDT','WAVESUSDT','ZILUSDT', 'ONEUSDT', 'COTIUSDT', 'SOLUSDT', 'EGLDUSDT',
           'AVAXUSDT', 'NEARUSDT', 'FILUSDT', 'AXSUSDT', 'ROSEUSDT', 'ARUSDT', 'MBOXUSDT', 'YGGUSDT', 'BETAUSDT',
           'PEOPLEUSDT', 'EOSUSDT', 'ATOMUSDT', 'FTMUSDT', 'DUSKUSDT', 'IOTXUSDT', 'OGNUSDT', 'CHRUSDT', 'MANAUSDT',
           'XEMUSDT', 'SKLUSDT', 'ICPUSDT', 'FLOWUSDT', 'WAXPUSDT', 'FIDAUSDT', 'ENSUSDT', 'SPELLUSDT', 'LTCUSDT', 
           'IOTAUSDT', 'LINKUSDT', 'XMRUSDT', 'DASHUSDT', 'MATICUSDT', 'ALGOUSDT', 'ANKRUSDT', 'COSUSDT', 'KEYUSDT',
           'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT', 'BCHUSDT', 'COMPUSDT', 'ZENUSDT', 'SNXUSDT', 'SXPUSDT',
           'SRMUSDT', 'SANDUSDT', 'SUSHIUSDT', 'YFIIUSDT', 'KSMUSDT', 'DIAUSDT', 'RUNEUSDT', 'AAVEUSDT', 
           '1INCHUSDT', 'ALICEUSDT', 'FARMUSDT', 'REQUSDT', 'GALAUSDT', 'POWRUSDT', 'OMGUSDT', 'DOGEUSDT', 
           'SCUSDT', 'XVSUSDT', 'ASRUSDT', 'CELOUSDT', 'RAREUSDT', 'ADXUSDT', 'CVXUSDT', 'WINUSDT', 'C98USDT', 
           'FLUXUSDT', 'ENJUSDT', 'FUNUSDT', 'KP3RUSDT', 'ALCXUSDT', 'ETCUSDT', 'THETAUSDT', 'CVCUSDT', 'STXUSDT', 
           'CRVUSDT', 'MDXUSDT', 'DYDXUSDT', 'OOKIUSDT', 'CELRUSDT', 'RSRUSDT', 'ATMUSDT', 'LINAUSDT', 'POLSUSDT', 
           'ATAUSDT', 'RNDRUSDT', 'NEOUSDT', 'ALPHAUSDT', 'XVGUSDT', 'KLAYUSDT', 'DFUSDT', 'VOXELUSDT', 'LSKUSDT', 
           'KNCUSDT', 'NMRUSDT', 'MOVRUSDT', 'PYRUSDT', 'ZECUSDT', 'CAKEUSDT', 'HIVEUSDT', 'UNIUSDT', 'SYSUSDT', 
           'BNXUSDT', 'GLMRUSDT', 'LOKAUSDT', 'CTSIUSDT', 'REEFUSDT', 'AGLDUSDT', 'MCUSDT', 'ICXUSDT', 'TLMUSDT', 
           'MASKUSDT', 'IMXUSDT', 'XLMUSDT', 'BELUSDT', 'HARDUSDT', 'NULSUSDT', 'TOMOUSDT', 'NKNUSDT', 'BTSUSDT', 
           'LTOUSDT', 'STORJUSDT', 'ERNUSDT', 'XECUSDT', 'ILVUSDT', 'JOEUSDT', 'SUNUSDT', 'ACHUSDT', 'TROYUSDT', 
           'YFIUSDT', 'CTKUSDT', 'BANDUSDT', 'RLCUSDT', 'TRUUSDT', 'MITHUSDT', 'AIONUSDT', 'ORNUSDT', 'WRXUSDT', 
           'WANUSDT', 'CHZUSDT', 'ARPAUSDT', 'LRCUSDT', 'IRISUSDT', 'UTKUSDT', 'QTUMUSDT', 'GTOUSDT', 'MTLUSDT', 
           'KAVAUSDT', 'DREPUSDT', 'OCEANUSDT', 'UMAUSDT', 'FLMUSDT', 'UNFIUSDT', 'BADGERUSDT', 'PONDUSDT', 
           'PERPUSDT', 'TKOUSDT', 'GTCUSDT', 'TVKUSDT', 'MINAUSDT', 'RAYUSDT', 'LAZIOUSDT', 'AMPUSDT', 'BICOUSDT', 
           'CTXCUSDT', 'FISUSDT', 'BTGUSDT', 'TRIBEUSDT', 'QIUSDT', 'PORTOUSDT', 'DATAUSDT', 'NBSUSDT', 'EPSUSDT', 
           'TFUELUSDT', 'BEAMUSDT', 'REPUSDT', 'PSGUSDT', 'WTCUSDT', 'FORTHUSDT', 'BONDUSDT', 'ZRXUSDT', 'FIROUSDT',
            'SFPUSDT', 'VTHOUSDT', 'FIOUSDT', 'PERLUSDT', 'WINGUSDT', 'AKROUSDT', 'BAKEUSDT', 'ALPACAUSDT', 
            'FORUSDT', 'IDEXUSDT', 'PLAUSDT', 'VITEUSDT', 'DEGOUSDT', 'XNOUSDT', 'STMXUSDT', 'JUVUSDT', 'STRAXUSDT',
            'CITYUSDT', 'JASMYUSDT', 'DEXEUSDT', 'OMUSDT', 'MKRUSDT', 'FXSUSDT', 'ETHUSDT', 'ADAUSDT', 'BNBUSDT', 
            'SHIBUSDT']

dropdown = st.selectbox('Select a coin', tickers)
start = st.date_input('Start date', value=pd.to_datetime('2021-01-01'))
investment = st.number_input('Investment per month', value=1000)

# Get data
def getData(symbol, start):
    start = str(start)
    frame = pd.DataFrame(client.get_historical_klines(symbol, '1d', start))
    frame = frame.iloc[:,:6]
    frame.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame.set_index('Date', inplace=True)
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

df = getData(dropdown, start)

# Calculate buy dates
buydates = pd.date_range(df.index[0], df.index[-1], freq='1M')
#Calculate buy prices
buyprices = df[df.index.isin(buydates)]['Close']
# Calculate coin amount
coin_amt = investment / buyprices
# Calculate Lump Sum investment coin amount
coin_amt_ls = investment * len(buyprices) / buyprices[0]
# Calculate cumlated coin amount
coin_amt_sum = coin_amt.cumsum()
coin_amt_sum.name = 'coin_amt_DCA'
# Concat coin_amt_sum and df to know the value of the coin on each day
df_tog = pd.concat([coin_amt_sum, df], axis=1).ffill()
# Define column with coin_amt_LS
df_tog['coin_amt_LS'] = coin_amt_ls

# Calculate daily portfolio value
df_tog['Portfolio_DCA'] = df_tog['coin_amt_DCA'] * df_tog['Close']
df_tog['Portfolio_LS'] = df_tog['coin_amt_LS'] * df_tog['Close']

# Calculate performance for DCA and LS
performance_DCA = (df_tog['Portfolio_DCA'][-1] / (investment * len(buyprices))) - 1
performance_LS = (df_tog['Portfolio_LS'][-1] / (investment * len(buyprices))) - 1

# Visualization for DCA
st.line_chart(df_tog['Portfolio_DCA'])
st.write('DCA Performance: ' + str(round(performance_DCA * 100, 2)) + ' %')

# Visualization for LS
st.line_chart(df_tog['Portfolio_LS'])
st.write('Lump Sum Performance: ' + str(round(performance_LS * 100, 2)) + ' %')
