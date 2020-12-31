# GUI Madness: An Exploration into the World of Graphical UI
This is an exploration into the GUI making capabilities of multiple languages. Here we will compare Python, Java, C++, C#, and even the Electron framework. Strap in!

## A Quick Note/Methodology ##
I am going to layout some basic ground rules and the methodology behind how each language will be compared. I don't intend on really judging each language or assigning a score/ranking beyond my personal thoughts or preference. My goal is primarily to educate myself more on the capability of each language, and to serve as a resource for anyone who happens to stumble on this repo. With that being said, let me breakdown how this will work.

With each language, I am going to pick the top packages/modules used for making a desktop app. With each of these packages, and their respective languages, we are going to examine a variety of areas. 

The first thing we will do with each language is create a basic window that mimics the windows notepad menu. The requirements to do that are as follows:
1. Toolbar w/ Cascading Menus
 - File (New, New Window, Open..., Save, Save As..., Print..., Exit)
 - Edit (Undo, Cut, Copy, Paste, Delete, Search with Bing..., Find..., Find Next, Find Previous, Replace, Go To..., Select All, Time/Date
 - Format (Word Wrap, Font...)
 - View (Zoom > Zoom In > Zoom Out > Restore Default Zoom, [x] Status Bar)
 - Help (View Help, Send Feedback, About Notepad)
 
 At first, none of these buttons except for exit actually have to do anything. However, we'll make them actually do something as a second project so we can compare the languages for their ability to add functionality in addition to their visuals. The NotePad project benchmark will be one of a couple different projects we use to compare the languages.
 
 After the NotePad benchmark, we'll build the following: Simple Password Manager and Calculator. Beyond those, it will vary by each language. We could do retro kind of games like hungry snake, hangman, tic-tac-toe, pong, space invaders, etc. but that might stay language specific depending on the capability of some languages to do things like that.
 
 ## The Rules ##
 We are going to lay down some ground rules just to make sure one language doesn't have an advantage over the other. For each language, we'll use the language plus the package we're using and any other common packages used to make things simpler. At the beginning, we won't use things like CSS or other styling/mark-up. We'll do this just to compare the basic look of what each language can create.
 
 ## The Languages & Packages ##
 Python: PyQT, Tkinter, wxPython, PySimpleGUI
 
 Java: JavaFX, Swing, AWT, QtJambi
 
 C++: Qt, wxWidgets, JUCE, CEF
 
 C#: WPF, WinForms
 
 ### Special Addition: Electron.js Framework ###
 Okay so, I know Electron isn't a language but rather a framework that utilizes HTML, CSS, and JavaScript. With that being said, some of the biggest apps today are built using in like: WhatsApp, Visual Studio Code, Twitch, Microsoft Teams, and thousands more. Because of this, I felt like it would be a mistake to leave it off even if it isn't a language.
