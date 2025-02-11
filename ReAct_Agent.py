import os
os.environ['GROQ_API_KEY'] = "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"


from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-70b-8192",
)

print(chat_completion.choices[0].message.content)

class Agent:
    def __init__(self, client , system):
        self.client = client 
        self.system = system 
        self.messages = [] 
        if self.system is not None:
            self.messages.append({
                "role": "system",
                "content" : self.system,
            })
    def __call__(self,message=""):
        if message:
            self.messages.append({"role": "user", "content":message})
        result = self.execute()
        self.messages.append({"role": "assistant","content" : result})
        return result 
    
    def execute(self):
        completion = client.chat.completions.create(
        messages=self.messages,
        model="llama3-70b-8192",
        )
        return completion.choices[0].message.content
system_prompt = """
You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop you output an Answer
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Observation will be the result of running those actions.

Your available actions are:

calculate:
e.g. calculate: 4 * 7 / 3
Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary

get_planet_mass:
e.g. get_planet_mass: Earth
returns weight of the planet in kg

Example session:

Question: What is the mass of Earth times 2?
Thought: I need to find the mass of Earth
Action: get_planet_mass: Earth
PAUSE 

You will be called again with this:

Observation: 5.972e24

Thought: I need to multiply this by 2
Action: calculate: 5.972e24 * 2
PAUSE

You will be called again with this: 

Observation: 1,1944×10e25

If you have the answer, output it as the Answer.

Answer: The mass of Earth times 2 is 1,1944×10e25.

Now it's your turn:
""".strip()


def calculate(operation: str) -> float:
    return eval(operation)


def get_planet_mass(planet) -> float:
    if planet == "earth":
        return 5.972e24
    if planet == "mars":
        return 6.39e23
    if planet == "jupiter":
        return 1.898e27
    if planet == "saturn":
        return 5.683e26
    if planet == "uranus":
        return 8.681e25
    if planet == "neptune":
        return 1.024e26
    if planet == "mercury":
        return 3.285e23
    if planet == "venus":
        return 4.867e24
    return None

neil_tyson = Agent(client=client, system=system_prompt)


import re


def loop(max_iterations=10, query: str = ""):

    agent = Agent(client=client, system=system_prompt)

    tools = ["calculate", "get_planet_mass"]

    next_prompt = query

    i = 0
  
    while i < max_iterations:
        i += 1
        result = agent(next_prompt)
        print(result)

        if "PAUSE" in result and "Action" in result:
            action = re.findall(r"Action: ([a-z_]+): (.+)", result, re.IGNORECASE)
            chosen_tool = action[0][0]
            arg = action[0][1]

            if chosen_tool in tools:
                result_tool = eval(f"{chosen_tool}('{arg}')")
                next_prompt = f"Observation: {result_tool}"

            else:
                next_prompt = "Observation: Tool not found"

            print(next_prompt)
            continue

        if "Answer" in result:
            break


loop(query="What is the mass of Earth plus the mass of Saturn and all of that times 2?")





# result = neil_tyson("What is the mass of Mercury times 5?")
# print(result)

# result = neil_tyson()
# print(result)

# result = get_planet_mass("mercury")
# print(result)

# next_prompt = "Observation: {}".format(result)
# next_prompt

# result = neil_tyson(next_prompt)
# print(result)

# result = neil_tyson(next_prompt)
# print(result)

# result = calculate("3.285e23 * 5")
# print(result)


# next_prompt = "Observation: {}".format(result)
# next_prompt

# result = neil_tyson(next_prompt)
# result

# for msg in neil_tyson.messages:
#     print(msg['content'])