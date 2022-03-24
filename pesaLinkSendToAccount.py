import requests
from requests.structures import CaseInsensitiveDict

url = "https://openapi-sandbox.co-opbank.co.ke/FundsTransfer/External/A2A/PesaLink/1.0.0/"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer eyJ4NXQiOiJNell5TlRrMVpEZ3laVFEyTmpBMlpUSXlNR1V5Wm1Rek5qZzFNVEV4TlRjeE16RTRPVGsyT0ROa1pERm1PVGRsWVRsa1ltUTNOVFpsTWpZMlltVTBPUSIsImtpZCI6Ik16WXlOVGsxWkRneVpUUTJOakEyWlRJeU1HVXlabVF6TmpnMU1URXhOVGN4TXpFNE9UazJPRE5rWkRGbU9UZGxZVGxrWW1RM05UWmxNalkyWW1VME9RX1JTMjU2IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJvdGlrb2phaXJ1c0BjYXJib24uc3VwZXIiLCJhdWQiOiJoZ2N5X19fcDlESnJsUkllMERqekdybDdrTzRhIiwibmJmIjoxNjQ4MTQwODYzLCJhenAiOiJoZ2N5X19fcDlESnJsUkllMERqekdybDdrTzRhIiwic2NvcGUiOiJhbV9hcHBsaWNhdGlvbl9zY29wZSBkZWZhdWx0IiwiaXNzIjoiaHR0cHM6XC9cL2RldmVsb3Blci5jby1vcGJhbmsuY28ua2U6OTQ0M1wvb2F1dGgyXC90b2tlbiIsImV4cCI6MTY0ODE0NDQ2MywiaWF0IjoxNjQ4MTQwODYzLCJqdGkiOiI0OGMxMjBlNS01YjY5LTQ2NjQtODY1MC01MmMyMjY1ZWM3NWMifQ.Cn6jgcWmITGjoWvWL3T-sENqlETtvYr9NPfVvy5gbq1rR01Rj0SLLnZ4ko-lTRszIODqK4V42a0u8p4Q_z0J_dA4baSC38uCv_mlSglOlet93nnVJstfu3uf0XP-cJfysgUAp1eKpZq2bFdukmhp57reg7zL06ZSUjiZJYzHKwJ5mqsvPjVgH0vShRM0B9nvPWF6krDI6eK0Gn9mmbaPl360ZMKV2JugAc660d03g146-HQsG0mpKlPacph4bQGNvZRQZ6Vtvs0FaPxDLaR8ZNt3d0LyeU6NPnCWlK7YVChvDf_uNMvt0_fDsBadP58WFfMGz4sJvqu5eBLJkGLB1A"

data = '{"MessageReference":"40ca18c676sjjs5086089a1","CallBackUrl":"https://yourdomain.com/ft-callback","Source":{"AccountNumber":"36001873000","Amount":777,"TransactionCurrency":"KES","Narration":"Supplier Payment"},"Destinations":[{"ReferenceNumber":"40ca18cksk6765086089a1_1","AccountNumber":"54321987654321","BankCode":"11","Amount":"777","TransactionCurrency":"KES","Narration":"Electricity Payment"}]}'


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)

