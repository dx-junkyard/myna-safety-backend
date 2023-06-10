import json
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)
from app.models.user_report.domain import CreateChatReport, ReportLevel


class ChatGPT:
    def __init__(self) -> None:
        self.chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        self.messages = [
            SystemMessage(content="あなたは世界で最も多く人を救ってきた、ボランティア団体の職員です"),
            SystemMessage(content="あなたは日本人で、多くの人から親しまれています。"),
            SystemMessage(content="300文字以内で回答してください。"),
        ]

    def request(self, sentence: str) -> str:
        self.messages.append(HumanMessage(content=sentence))
        response = self.chat(
            self.messages,
        )
        print(response)
        return response.content

    def create_report_title(self, content: str) -> CreateChatReport:
        if content == "":
            return CreateChatReport(
                title="タイトルなし", report_level=ReportLevel.UnKnown
            )

        report_title_prompt = [
            SystemMessage(
                content="""
次のフォーマットで値を抽出せよ。
{
  "title": 文章を15文字以下で要約したタイトル,
  "report_level": 防災の観点において緊急性を次から選択[High,Middle,Low]
}
キーは必ず含ませる。
JSON以外の情報は削除する。

要約して欲しい文章は次の値
"""
            ),
        ]
        report_title_prompt.append(HumanMessage(content=content))
        response = self.chat(
            report_title_prompt,
        )
        print(response)
        response_json = self._convert_json(response.content)
        return CreateChatReport.parse_obj(response_json)

    @staticmethod
    def _convert_json(response: str):
        try:
            return json.loads(response)
        except:
            return {}


chatGPT = ChatGPT()
# print(chatGPT.create_report_title("家族と逸れました、洪水の中一人で孤立していて大変です。誰か助けてください"))
# print(chatGPT.create_report_title("建物は少し損傷していますが、怪我はありません。食糧も確保できています。"))
