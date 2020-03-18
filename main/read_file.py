import simplefix as sf
import pandas as pd
df = open("/home/dominik/PycharmProjects/CMEData/6E_20060207.TXT", "r")

#print(df.read(555))


#df_sf = sf.message.FixMessage.encode(df)

df_sf = pd.array(df, bytes)

print(df_sf)