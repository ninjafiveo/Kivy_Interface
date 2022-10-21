#region imports
from time import sleep
from tkinter import Label
from matplotlib.pyplot import text
from web3 import Web3
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from numpy import size
from kivy.metrics import dp # needed to density pixels size.
#endregion

#connect to Ganache... needs to be open.
ganache_url = 'HTTP://127.0.0.1:7545' #! On Ganache App

# Test the connection. True = connected.
web3=Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())
print(web3.eth.block_number)

# Send some currency

account_1 = "0x99B637cEaf2c897De729ed020A30E21A3DC52F8c"
account_2 = "0x91e65D0EdE66F7B25A33AaC78F98cde6E5DDd8fc"
private_key_to_account_1 = "b3341c0b71eb623509d0099d2438cd33a35f478865783118c9c53663cbd70185" #?Tells web3 it's ok to send money. Validates permission. Use this to sign transactions


# get the nonce --> Prevents you from sending a transaction 2x's
nonce = web3.eth.getTransactionCount(account_1)
# build a transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value':web3.toWei(1, 'ether'),
    'gas': 200000, #limits amount of gas you'll pay.
    'gasPrice' : web3.toWei('50', 'gwei') #gwei > wei, gwei < ethereum
}
# sign the transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key_to_account_1)

# send the transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash
print(tx_hash)
print(web3.toHex(tx_hash)) # Converts it to a readable hash.

#! Interface Below

class GanacheAppLayout(GridLayout):
    pass

class GanacheApp(App):
    pass

GanacheApp().run()