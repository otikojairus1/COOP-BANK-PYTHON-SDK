import requests
from requests.structures import CaseInsensitiveDict

url = "https://openapi-sandbox.co-opbank.co.ke/FundsTransfer/External/A2M/PesaLink/1.0.0/"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer eyJ4NXQiOiJNell5TlRrMVpEZ3laVFEyTmpBMlpUSXlNR1V5Wm1Rek5qZzFNVEV4TlRjeE16RTRPVGsyT0ROa1pERm1PVGRsWVRsa1ltUTNOVFpsTWpZMlltVTBPUSIsImtpZCI6Ik16WXlOVGsxWkRneVpUUTJOakEyWlRJeU1HVXlabVF6TmpnMU1URXhOVGN4TXpFNE9UazJPRE5rWkRGbU9UZGxZVGxrWW1RM05UWmxNalkyWW1VME9RX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJvdGlrb2phaXJ1c0BjYXJib24uc3VwZXIiLCJhdWQiOiJoZ2N5X19fcDlESnJsUkllMERqekdybDdrTzRhIiwibmJmIjoxNjQ4MTQxMzcyLCJhenAiOiJoZ2N5X19fcDlESnJsUkllMERqekdybDdrTzRhIiwic2NvcGUiOiJhbV9hcHBsaWNhdGlvbl9zY29wZSBkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL2RldmVsb3Blci5jby1vcGJhbmsuY28ua2U6OTQ0M1wvb2F1dGgyXC90b2tlbiIsImV4cCI6MTY0ODE0NDk3MiwiaWF0IjoxNjQ4MTQxMzcyLCJqdGkiOiI3Mzk4ZmUxZi0yNDM2LTRjNWYtOGQ0Ny0wZmExZTg4OGI2NWIifQ.bzNZvEzwRBcUF0zGR9yIxOpPDP4VL9tamJF7cXOCRvmEQkny4qEh98im1BEXbDZIxFhK85oVL_9F4hP6uVmPDxRUt_OO0FPpQMHb-mFCCUepNJK7eZDqjXnzOyr45kR3EewKQjqDHKGhsq2IBdAjqxcOwp3C0IYrMvqfRMMFSqSN-LPgF6C_-uqMrHzQE9sw9MPUcRqMSW0LOaPbjOAVpKY5HQKOKH9OFiU5HZnLcmP9E-uktvX6BiP5ECJLg3nl9wY_cNn_UYIuBwE7ikxmwFqF2Qbtib41szSQvgSnvp9o5MgfDsRGhD1u8z9FxBhOvZaX3jfp8kyVPJklUn_wPg"

data = '{"MessageReference":"40ca18c67x65086089a1","CallBackUrl":"https://yourdomain.com/ft-callback","Source":{"AccountNumber":"36001873000","Amount":777,"TransactionCurrency":"KES","Narration":"Supplier Payment"},"Destinations":[{"ReferenceNumber":"40ca18c67ss65086089a1_1","PhoneNumber":"0722753364","Amount":"777","TransactionCurrency":"KES","Narration":"Electricity Payment"}]}'


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

