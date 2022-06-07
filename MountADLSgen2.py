#Montaje de ADLS Gen 2 para databricks

cuenta = <"nombre ADLSgen2">
ruta = "/mnt/{}".format(<"Mount Point">)
container = <"nombre container dentro ADLSgen2">

ADLSgen2EndPoint ="abfss://{}@{}.dfs.core.windows.net/".format(container, cuenta)
print ('Ruta ='+ruta)

#ClientId, TenantId y Secret. Datos del Service Principal generado en AAD como Application registration. Otorgar permisos de Storage Blob Data Contributor dentro del ADLSgen2 
clientID ="xxx-xx-xx-xx-xxx"
tenantID ="xx-xx-xx-xx-xx"
clientSecret ="xxx-xx-xxxxx"
oauth2Endpoint = "https://login.microsoftonline.com/{}/oauth2/token".format(tenantID)


configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": clientID,
           "fs.azure.account.oauth2.client.secret": clientSecret,
           "fs.azure.account.oauth2.client.endpoint": oauth2Endpoint}

try:
  dbutils.fs.mount(
  source = ADLSgen2EndPoint,
  mount_point = ruta,
  extra_configs = configs)
except:
    print("La ruta ya está montada...."+ruta)
