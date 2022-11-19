import pandas as pd

mtl_vol = pd.read_html('https://coinmarketcap.com/currencies/volume/monthly/')
stablecoins = pd.read_html('https://coinmarketcap.com/view/stablecoin/')[0]['Name']
stablecoins = [x[-4:] for x in stablecoins]
def remove(list):
    list = [''.join(x for x in i if x.isalpha() or x.isupper()) for i in list]
             
    return list
stablecoins = remove(stablecoins)
mtl_vol_df = pd.DataFrame(mtl_vol[2])
mtl_vol_df = mtl_vol_df[~mtl_vol_df.Symbol.isin(stablecoins)]

buylist = mtl_vol_df.Symbol.head(11)
buylist