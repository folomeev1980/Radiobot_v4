import requests

chatId = 574990729
send = 'https://api.telegram.org/bot981624897:AAFD1wu7bBI4XCR3JHvf9iYqRLPZujpDLJM/sendMessage?chat_id=320870549&text="Hello'
getUpdate = 'https://api.telegram.org/bot981624897:AAFD1wu7bBI4XCR3JHvf9iYqRLPZujpDLJM/getUpdates?offset=5'

token = '574990729:AAHvFADSNg-LQ5RUSaPdbiQ2pOdDA7XI5Xc'

r = requests.get(getUpdate)
print(r.content)














