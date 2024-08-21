import requests

url = https://drive.google.com/file/d/10Q7sLLI3dKHe2wL0KIrUM0KSaUFJyUz-/view?usp=sharing"
response = requests.get(url)
with open('ml_model.pkl', 'wb') as f:
    f.write(response.content)
