Tharoor= { "snollygoster": "https://en.wiktionary.org/wiki/snollygoster",
          "rodomontade":"https://en.wiktionary.org/wiki/rodomontade",
          "puerile":"https://en.wiktionary.org/wiki/puerility",
          "farrago":"https://en.wikipedia.org/wiki/Farrago"}
word=input("Select a word from the above dictionary: ")
print("Kindly go to the link, it will give you much more information than just meaning and synonyms of",word,"\n",   "Here is the link: ", Tharoor.get(word))


d2 = {"Cause-and-effect diagram":"https://en.wikipedia.org/wiki/Ishikawa_diagram",
      "Check sheet":"https://en.wikipedia.org/wiki/Check_sheet",
      "Control chart":"https://en.wikipedia.org/wiki/Control_chart",
      "Histogram":"https://en.wikipedia.org/wiki/Histogram",
      "Pareto chart":"https://en.wikipedia.org/wiki/Pareto_chart",
      "Scatter diagram":"https://en.wikipedia.org/wiki/Scatter_plot",
    "Stratification":"https://en.wikipedia.org/wiki/Stratification"}
print("Enter the QC Tool Name:")
print(d2[input()])