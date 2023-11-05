from flask import Flask, request, render_template, jsonify
from langchain.chat_models import ChatAnthropic
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.prompts import ChatPromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from inference import infer
from bravediscussionfetcher import fetchDiscussionPosts

app = Flask(__name__, template_folder="templates")

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/infer", methods=['POST'])
def infer_from_claude():
    data = request.json
    discussionData = fetchDiscussionPosts(data['message'])
    response = infer(data['message'])
    return jsonify(data=response, discussionData=discussionData)


# Comment this line before deploying
app.run(debug=True)