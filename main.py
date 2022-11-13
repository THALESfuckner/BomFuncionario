import pandas as pd 
import twilio as tw
from twilio.rest import Client

 
 #connection
account_sid = 'pegar na conta twilio'
auth_token = 'pegar na conta twilio'

# precisa instalar
# "pandas" . "openpyxl" para integracao do python com excel 
# "twilio" integracao do py ao sms




listaMeses = ['janeiro', 'fevereiro','março','abril','junho']


for mes in listaMeses:
    
    tabelaVenda= pd.read_excel(f'Arquivos para analise/{mes}.xlsx')

   
    if (tabelaVenda['Vendas'] > 55000).any(): 
        
       #verificacao dos valores nas tabelas
        vendedor = tabelaVenda.loc[tabelaVenda['Vendas'] > 55000,'Vendedor'].values[0]
        vendas =  tabelaVenda.loc[tabelaVenda['Vendas'] > 55000,'Vendas'].values[0]
        
        
        print(f'No mes de {mes} o(a) vendedor(a) {vendedor} bateu a meta vendendo {vendas}')
        client = Client(account_sid, auth_token)    
        message = client.messages.create(
            to = "colocar o numero ",
            from_ = "numero cruado pelo twilio",
            body= f'No mes de {mes} o(a) vendedor(a) {vendedor} bateu a meta vendendo {vendas} R$, e como premio terá uma viagem com um acompanhante para o Chile')
            
        print(message.sid)
        


        



