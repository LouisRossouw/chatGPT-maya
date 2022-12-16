"""
    I connected openai chatGPT3 to Maya as a test,
    I was curious to see if we can get chatGPT to perform simple maya tasks based on the users input instructions,,

    By default i added "write maya python code that: " at the start of every user input, this kinda forces chatGPT to
    only return code and no unnecessary text, the returned code, which is a string, is then executed in maya.
    complicated requests don't work,
    but simple automation tasks works, specially if you communicate in a logical way and break down steps.

    To test out and play with it:

    - Maya needs openai installed: - in autodesk/maya/bin directory: run "mayapy -m pip install openai" with terminal.
    - API key is needed, so either directly add your key into the API variable below (Not recommended,
      your API keys should be kept private.) or put it in maya env under a variable called "OPENAI_API_KEY".

    Have fun!
    www.LouisRossouw.com
"""

import os
import openai
import maya.cmds as cmds


class ChatChatAI:

    def __init__(self):

        # UI
        self.window_title = 'ChatChatGPTEES playplay'
        self.UI_width_height = 303, 65

        # Colors
        self.buttonS_BG_col = (0, 1, 0.7)
        self.window_BG_col = (0.12, 0.12, 0.12)

        # OpenAI settings.
        self.START_PROMPT = "write maya python code that: "
        self.ENGINE = "text-davinci-003"
        self.MAX_TOKENS = 1024
        self.NUMBERS = 1
        self.STOP = None
        self.TEMP = 0.5

        API = os.getenv("OPENAI_API_KEY")
        openai.api_key = API



    def return_openai(self):
        """ Returns generated data from openAI GPT. """

        self.progress_bar(amount=5)

        prompt = cmds.textField(self.promptField, query=True, text=True)
        completions = openai.Completion.create(
                            engine=self.ENGINE,
                            prompt=self.START_PROMPT + prompt,
                            max_tokens=self.MAX_TOKENS,
                            n=self.NUMBERS,
                            stop=self.STOP,
                            temperature=self.TEMP
                            )

        self.progress_bar(amount=5)
        self.progress_bar(amount=-10)

        response = completions.choices[0].text
        print(response)

        return response



    def push_button_show(self, *args):
        """ Shows the generated code. """

        response = self.return_openai()
        self.show_code_ui(response)



    def push_button_run(self, *args):
        """ Executes the returned generated code from GPT. """

        response = f"{self.return_openai()}"

        # Execute returned generated code (that is a string.)
        exec(response)



    def progress_bar(self, amount):
        """ Updates Progress bar. """

        cmds.progressBar(self.progressControl, edit=True, step=amount)



    def show_code_ui(self, response):
        """ Builds basic UI with maya cmds. """

        cmds.window(
                    title=self.window_title,
                    widthHeight=(self.UI_width_height[0], 250),
                    bgc=self.window_BG_col)

        cmds.columnLayout(adjustableColumn=True)
        cmds.rowColumnLayout(numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(10, 100), (2, 250)])

        self.textField = cmds.text(response, width=250, height=250, al="left")

        cmds.setParent('..')
        cmds.showWindow()



    def main_ui(self):
        """ Builds main UI with maya cmds. """

        window = cmds.window(title=self.window_title,
                            widthHeight=(self.UI_width_height[0], self.UI_width_height[1]),
                            bgc=self.window_BG_col,
                            tlb=True)

        cmds.columnLayout(adjustableColumn=True)
        cmds.rowColumnLayout(numberOfColumns=1,
                             columnAttach=(1, 'left', 0),
                             columnWidth=[(10, 100), (2, 250)])

        self.promptField = cmds.textField(width=1050, ann="What you would like to do")
        self.progressControl = cmds.progressBar(maxValue=10, width=300)

        cmds.setParent('..')

        cmds.gridLayout(numberOfColumns=2,
                        cellWidthHeight=(150, 20))

        cmds.button(label='Run',
                    bgc=self.buttonS_BG_col,
                    command=self.push_button_run)

        cmds.button(label='Show Code',
                    bgc=self.buttonS_BG_col,
                    command=self.push_button_show)

        cmds.setParent('..')

        cmds.showWindow()



if __name__ == "__main__":

    ChatChatAI().main_ui()
