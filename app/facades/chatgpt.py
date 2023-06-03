from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)


class ChatGPT:
    def __init__(self) -> None:
        self.chat = ChatOpenAI(model_name="gpt-3.5-turbo")
        self.messages = [
            SystemMessage(content="あなたは世界で最も多く人を救ってきた、ボランティア団体の職員です"),
            SystemMessage(content="あなたは日本人で、多くの人から親しまれています。"),
            SystemMessage(content="300文字以内で回答してください。"),
        ]

    def request(self, sentence) -> str:
        self.messages.append(HumanMessage(content=sentence))
        response = self.chat(
            self.messages,
        )
        print(response)
        return response.content