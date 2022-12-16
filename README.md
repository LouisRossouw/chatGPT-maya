# chatGPT-maya

I connected openai chatGPT3 to Maya as a test,
I was curious to see if we can get chatGPT to perform simple maya tasks based on the users input instructions,,

By default i added "write maya python code that: " at the start of every user input, this kinda forces chatGPT to
only return code and no unnecessary text, the returned code, which is a string, is then executed in maya.
complicated requests don't work,
but simple automation tasks works, specially if you communicate in a logical way and break down steps.

To test out and play with it:

- Maya needs openai installed: - in autodesk/maya/bin directory: run "mayapy -m pip install openai" with terminal.
- an openai API key is needed, so either directly add your key into the API variable below (Not recommended,
  your API keys should be kept private.) or put it in maya env under a variable called "OPENAI_API_KEY".
  
  
