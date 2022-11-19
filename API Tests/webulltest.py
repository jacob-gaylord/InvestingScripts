from webull import paper_webull
import json

wb = paper_webull()
print(wb.get_mfa('+1-6512618311'))
mfaCode = input("MFA Code: ")
print(wb.get_security('+1-6512618311'))
answer = input('Security Question Answer: ')
questionId = input("Question: ")
data = wb.login('+1-6512618311','wgm7rhu2QZJ*zyt5jtj', 'PythonTest', mfaCode, questionId, answer)
print(wb.get_trade_token('180505'))

wb.place_order(stock='ADBE', orderType='LMT', price=0, quant=0.767624679508263)