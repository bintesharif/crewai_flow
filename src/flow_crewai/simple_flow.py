from crewai.flow.flow import Flow, start, listen
import time

class Simple_flow(Flow):         
    @start()  
    def IN(self):
        topic = "AI"
        print("step1 input:" , topic) 
        return topic
        

    @listen(IN)
    def LLMCall1(self, topic):
        print(f"step2 LLM Call: {topic} for searching news"  )
        return topic + " news"
        
 
    @listen(LLMCall1) 
    def LLMCall2(self, topic_news):
        print(f"step3 LLM Call2: {topic_news} for searching artical"  )
        self.state['topic_news_artical'] = topic_news + " artical"


    @listen(LLMCall2)
    def LLMCall3(self):
        print(f"step4 LLM Call3: {self.state['topic_news_artical']} for searching summary"  )
        self.state['topic_news_artical_summary'] = self.state['topic_news_artical'] + " summary"

    @listen(LLMCall3)
    def OUT(self):
        print("step5 output")


def main():
    obj = Simple_flow()
    obj.kickoff() 
    obj.plot("simple_flow")
    