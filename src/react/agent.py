import os 
import json 
import logging
from typing import Callable , Dict , List 
import google.generativeai as genai
import sys
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # This is used for importing funtion from other modules

from .prompt import PROMPT_TEMPLATE
from .enums import Name  , Observation
from .models import Message, Choice


print(" All libraries Imported Successfully")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Tool:
    def __init__(self ,name:Name , func:Callable[[str],str]):
        self.name = name
        self.func = func

    def use(self ,query:str) -> Observation:
        try:
            return self.func(query)
        except Exception as e:
            logger.error(f"Error Executing tool {self.name}:{e}")
        return str(e)
    
class Agent:
    def __init__(self , api_key:str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        self.tools : Dict[Name , Tool] = {}
        self.messages:List[Message] = []
        self.query = ""
        self.max_iterations = 5
        self.current_iteration =0
        self.prompt_template = PROMPT_TEMPLATE


    def register(self ,name:Name ,func:Callable[[str],str]) -> None:
        self.tools[name] = Tool(name, func)

    def trace(self , role:str , content:str) -> None:
        self.messages.append(Message(role=role, content=content))

    def get_history(self) -> str:
        return "\n".join([f"{m.role}:{m.content}" for m in self.messages])
    
    def ask_gemini(self ,prompt:str) -> str:
        response = self.model.generate_content(prompt)
        logger.info(f"Gemini Response: {response.text}")
        return response.text
    
    def think(self) -> None:
        self.current_iteration +=1
        if self.current_iteration >= self.max_iterations:
            self.trace("system", "Max Iterations reached")
            return 
        prompt = self.prompt_template.format(
            query = self.query,
            history = self.get_history(),
            tools = ', '.join([str(t.name) for t in self.tools.values()])

        )
        response = self.ask_gemini(prompt)
        self.trace("assitant", f"Thought:{response}")
        self.decide(response)

    def decide(self, response:str) -> None:
        try:
            cleaned = response.strip().strip("`")
            if cleaned.startswith("json"):
                cleaned = cleaned[4:].strip()
             
            if not cleaned:
                raise ValueError("Empty response from model")
            
            parsed_response = json.loads(cleaned)

            if "action" in parsed_response:
                action = parsed_response["action"]
                tool_name = Name[action["name"].upper()]
                self.act(tool_name, action.get("input",self.query))
            elif "answer" in parsed_response:
                self.trace("assistant", f"Final Answer:{parsed_response['answer']}")
            else:
                raise ValueError("Invalid response format")
            
        except Exception as e:
            self.trace("system",f"Error in Decision:{str(e)}")
            self.think()

    def act(self, tool_name:Name , query:str) -> None:
        tool = self.tools.get(tool_name)
        if tool:
            result = tool.use(query)
            self.trace("system", f"Observation from {tool_name}:{result}")
            self.think()
        else:
            self.trace("system", f"No tool registered for:{tool_name}")
            self.think()

    def execute(self, query:str) -> str:
        self.query = query
        self.messages.clear()
        self.current_iteration =0
        self.trace("user", query)
        self.think()
        return self.get_history()
    





                   
        


        