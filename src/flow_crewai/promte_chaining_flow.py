from crewai.flow.flow import Flow, start, listen
import time 
from litellm import completion
import os
from dotenv import load_dotenv, find_dotenv

_: bool = load_dotenv(find_dotenv())

class PromptChainingFlow(Flow):
    @start()
    def function1(self):
        response = completion(
            model="gemini/gemini-1.5-flash",  
            messages=[
                {"role": "user", "content": "generate any random city name from pakistan only "}
            ]
        )
        city_name = response.choices[0].message.content
        print(city_name)
        return city_name

    @listen(function1)
    def function2(self,city_name):
        response = completion(
            model="gemini/gemini-1.5-flash",  
            messages=[
                {"role": "user", "content":f"write some fun fact about{city_name}city?output must be in the  markdown format"}
            ]
        )
        fun_fact = response.choices[0].message.content
        print(fun_fact)
        self.state['fun_fact']=fun_fact

    @listen(function2)
    def function3(self):
        with open("fun_fact.md","w") as f:
            f.write(self.state['fun_fact'])

        
def run_prompt_chaining_flow():
    obj = PromptChainingFlow()
    obj.kickoff()
    obj.plot()




    
