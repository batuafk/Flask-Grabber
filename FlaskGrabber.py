from flask import Flask, request
from user_agents import parse

app = Flask(__name__)

@app.route("/")
def index():
    ip = request.remote_addr
    user_agent_string = request.headers.get('User-Agent', '')

    user_agent = parse(user_agent_string)

    os = user_agent.os.family
    os_version = user_agent.os.version_string
    if os_version:
        os_version = f" {os_version}"
    browser = user_agent.browser.family
    browser_version = user_agent.browser.version_string

    accept_language = request.headers.get('Accept-Language', '')
    languages = [lang.split(';')[0] for lang in accept_language.split(',')]
    language = ', '.join(languages)

    with open("datas.txt", "a") as file:
        file.write(f"IP: {ip}, OS: {os}{os_version}, Browser: {browser} {browser_version}, Language: {language}\n")

    return ""

if __name__ == "__main__":
    app.run()
