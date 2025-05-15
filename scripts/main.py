import pandas as pd

# Carregar os três arquivos CSV
aliexpress_df = pd.read_csv('Meganium_Sales_Data_-_AliExpress.csv')
etsy_df = pd.read_csv('Meganium_Sales_Data_-_Etsy.csv')
shopee_df = pd.read_csv('Meganium_Sales_Data_-_Shopee.csv')

# Combinar os DataFrames
combined_df = pd.concat([aliexpress_df, etsy_df, shopee_df], ignore_index=True)

# Salvar o DataFrame combinado em um novo arquivo CSV
combined_df.to_csv('Meganium_Sales_Data_Combined.csv', index=False)

print("Arquivos combinados com sucesso! Salvo como 'Meganium_Sales_Data_Combined.csv'")