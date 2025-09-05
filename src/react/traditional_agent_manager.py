from typing import Callable , Dict , List , Optional , Union
from enum import Enum
import random 

#------ Mocked Tools--------

def wikipedia_search(query:str)-> str:
    mock_data = {

        "Cristiano Ronaldo" : "Cristiano Ronaldo was born on Feburary 5, 1985.",
        "Lionl Messi": "Lionel Messi was born on June 24, 1987.",
        "2022 FIFA World Cup" : "Argentina won the 2022 FIFA World Cup with Lionel Messi as captain.",
        "Rosario" : "Rosario is a city in Argentina.",
        "United States national dish" : "There is no official national dish of the U.S.  ,but hamburger and apple pie are popular."
    }
    return mock_data.get(query, f"No wikipedia data found for '{query}'")



def google_search(query:str)-> str:
    mock_data ={
        "average temperature in Buenos Aires:":" The Average temperatutre in Buenos Aires is approximately 18C (64F).",
        "top 5 counties by GDP and their national dishes":"USA:Burger , China:Peking Duck , Japan:Sushi , Germany:Sauerbraten ,Indian:Biryani",
        "Popular Dishes in United States":"Burger ,BBQ, ribs, Mac&Cheese , HotDog.",
        "common ingredients in United States Cusine":"Wheat , Corn , beef , chicken.",
        "Common ingredients in Indian Cusines"  : " Rice , Lentils ,Turmeric , cumin."


    }
    return mock_data.get(query , f"No Gooogle Data Found for '{query}'")



#--------------- Tools Abstractions  ------------------


class Name(str ,Enum):
    WIKIPEDIA = "wikipedia"
    GOOGLE = "google"


class Tool:
    def __init__(self, name:Name ,func:Callable[[str],str]) -> None:
        self.name = name 
        self.func = func 

    def use(self , query:str) -> str:
        return self.func(query)
    

class Choice:
    def __init__(self , name:Name , reason:str):
        self.name = name
        self.reason = reason



#-------- Rule Based Tool Manager---------------
class Manager:
    def __init__(self) -> None:
        self.tools : Dict[Name ,Tool] ={}

    def register(self , name:Name , func:Callable[[str],str]) -> None:
        self.tools[name] = Tool(name , func)

    def act(self ,name:Name , query:str) -> str:
        if name not in self.tools:
            raise ValueError(f"Tool {name} not registered")
        return self.tools[name].use(query)
    
    def choose(self , query:str) -> Choice:
        if query.startswith("/people"):
            return Choice(Name.WIKIPEDIA, "Query starts with /people , using wikipedia for biographical info.")
        elif query.startswith("/location"):
            return Choice(Name.GOOGLE, "Query starts with /location usinhg the Google for location info.")
        else:
            raise ValueError("Unsupported Query format , Use /people or /location")
        

#---- ReAct Agent Simulation --------------------

class ReactAgent:
    def __init__(self ,tools:Dict[Name,Tool]):
        self.tools = tools
        self.history:List[Dict] = []


    def reason_and_act(self ,query:str) -> str:
        print("Starting Query reasoning...\n")

        #Simulate ReAct Behavior
        if "older" in query and "Cristiano Ronaldo" in query:
            return self.compare_ages("Cristiano Ronaldo", "Lionel Messi")
        
        elif "average temperature" in query:
            return self.fifa_temp_reasoning()
        
        elif "common ingredient" in query:
            return self.common_ingredient_analysis()
        
        return "Sorry , I Couldn't understand the Query"
    
    def compare_ages(self, person1:str , person2:str) -> str:
        thought1 = f"Looking up birth date for {person1}"
        obs1 = self.tools[Name.WIKIPEDIA].use(person1)

        thought2 = f"Looking for birth date for {person2}."
        obs2 = self.tools[Name.WIKIPEDIA].use(person2)

        print(f"{thought1}\n Observation{obs1}\n")
        print(f"{thought2}\n Observation{obs2}\n")

        return f"{person1} is older than {person2} based on birth dates."
    

    def fifa_temp_reasoning(self) -> str:
        steps = [

            ("Get World Cup winnner info", Name.WIKIPEDIA, "2022 FIFA World Cup."),
            ("Get Captain's birthplace", Name.WIKIPEDIA, "Lionel Messi"),
            ("Get temprature of capital", Name.GOOGLE, "average temperature in Buenos Aires"),
        ]
        result = []
        for desc , tool , input_ in steps:
            thought = f"Step.{desc} | using : {tool.value} | Input:{input_}"
            obs = self.tools[tool].use(input_)
            result.append(f"{thought}\nObservation:{obs}\n")
        return "\n".join(result)
    

    def common_ingredient_analysis(self) -> str:
        themes = [

            "All Countries use starchy staples: rice , wheat, potatoes ,noodles",
            "Protein Sources vary but are always present",
            "Unique Spices define regional tastes"
        ]
        return "\n".join(["Analyzing the ingredients accross top GDP countries..."]+ themes)
    
#-------- Main Executions -------


def main():
    mgr = Manager()
    mgr.register(Name.WIKIPEDIA, wikipedia_search)
    mgr.register(Name.GOOGLE, google_search)

    try:
        choice = mgr.choose("/people Cristiano Ronaldo")
        print(f"Rule-Based: Choose {choice.name} because {choice.reason}")
        result = mgr.act(choice.name, "/people Cristiano Ronaldo")
        print("Result:", result)
    except ValueError as ve:
        print("Rule Error:", ve)

    print("\n------------------\n")

    #React agent usage
    agent = ReactAgent(mgr.tools)

    query1 = "Who is older , Cristiano Ronaldo or Lionel Messi?"
    print("ReAct Output 1:\n", agent.reason_and_act(query1))

    query2 ="What is the average temperature in the Capital City of Country where the current FIFA World Cup champions team captain was born?"
    print("ReAct Output 2:\n ", agent.reason_and_act(query2))

    query3 = "What is the most common ingredients in  the national dishes of the top 5 Countries by GDP?"
    print("ReAct Output 3:\n", agent.reason_and_act(query3))


if __name__ == "__main__":
    main()


