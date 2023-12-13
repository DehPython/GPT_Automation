from chatgpt_selenium_automation import ChatGPTAutomation

# A sintaxe r'\"...\"' é necessária por causa do espaço em "Program Files" no caminho do chrome
chrome_path = r'/usr/bin/google-chrome'

# Crie uma instância
chatgpt = ChatGPTAutomation(chrome_path)

# Defina um prompt e envie-o para chatgpt
prompt = "ESCREVA AQUI O SEU PROMPT"
chatgpt.send_prompt_to_chatgpt(prompt)

# Recupere a última resposta do ChatGPT
response = chatgpt.return_last_response()
print(response)

# Salve a conversa em um arquivo de texto
file_name = "conversation.txt"
chatgpt.save_conversation(file_name)

# Feche o navegador e encerre a sessão do WebDriver
chatgpt.quit()
