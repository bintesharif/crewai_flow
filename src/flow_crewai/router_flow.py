from crewai.flow.flow import Flow, start, listen, router, or_
from litellm import completion
import os
from dotenv import load_dotenv, find_dotenv
_: bool = load_dotenv(find_dotenv())
import random


class RoutingFlow(Flow):
    @start()
    def In(self):
        return random.choice(["medical", "finance", "sports"])
    
    @router(In)
    def LLM_call_router(self, topic):
        if topic == "medical":
            return "medicalRoute"
        elif topic == "finance":
            return "financeRoute"
        else:
            return "sportsRoute"

    @listen('medicalRoute')
    def Medical(self, topic):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {"role": "user", "content": f"Write a short summary of the latest developments in {topic}."}
            ],
        ) 
        return response["choices"][0]["message"]["content"]
    
    @listen('financeRoute')
    def Finance(self, topic):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {"role": "user", "content": f"Write a short summary of the latest developments in {topic}."}
            ],
        )
        return response["choices"][0]["message"]["content"]
    
    @listen('sportsRoute')
    def Sports(self, topic):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {"role": "user", "content": f"Write a short summary of the latest developments in {topic}."}
            ],
        )
        return response["choices"][0]["message"]["content"]

    @listen(or_(Medical, Finance, Sports))
    def Out(self, content):
        with open("response.md", "w") as f:
            f.write(content)

def kickoff():
    flow = RoutingFlow()
    flow.kickoff()
    flow.plot()
# class RouterFlow(Flow):
#     @start()
#     def IN(self):
#         print("step1 input")
#         self.state['topic'] = "AI"
#         print(f"step1 input {self.state['topic']}")

#     @router(IN)
#     def router(self):
#         print(f"step2 router {self.state['topic']}")
#         if self.state['topic'] == "AI":
#             return "ai_router"
#         elif self.state['topic'] == "AI_news":
#             return "ai_news_router"
#         elif self.state['topic'] == "AI_article":
#             return "ai_article_router"
    
#     @listen("ai_router")
#     def LLMCall1(self):
#         print(f"step3 listen {self.state['topic']}")
#         self.state['topic'] = "news"

#     @listen("ai_news_router")
#     def LLMCall2(self):
#         print(f"step4 listen {self.state['topic']}")
#         self.state['topic'] = "AI_article"

#     @listen("ai_article_router")
#     def LLMCall3(self):
#         print(f"step5 listen {self.state['topic']}")
#         self.state['topic'] = "summary" 

#     @listen(or_(LLMCall1, LLMCall2, LLMCall3))
#     def output(self):
#         print(f"step6 output {self.state['topic']}")


# def main():
#     flow = RouterFlow()  
#     flow.kickoff()  
#     flow.plot()  


        
