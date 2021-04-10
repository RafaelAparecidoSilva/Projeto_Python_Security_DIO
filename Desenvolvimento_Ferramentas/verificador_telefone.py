import phonenumbers as ph
from phonenumbers import geocoder


# phone = input('Digite um número de telefone no formato "+551199998888": ')
phone = '+551239468908'
phone_number = ph.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))




