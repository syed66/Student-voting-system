import tkinter as tk  # this is for Window creation
from tkinter import Tk, Label, Button, Menu, Entry, messagebox  # that is required in my application
# from tkinter import *
import os  # Python package os and it is used to know pwd


# Done by Yuling, Mohammed, Tejal and Shahzeb: Below are all classes are implemented as part of Object Oriented Programming.
class candidates:  # candidate call with all methods required for candidate
    # __init__ method is the first method that will be invoked when object will be created.
    def __init__(self, candi_name, Pin):
        self.candi_name = candi_name
        self.Pin = Pin
        self.votePrf = {}  # Dict count in all preference Preference1 = 20, Pref2 =2

    def updateVoteForCandidate(self, Prf):  # c1.updateVoteForCandidate("pref1")
        if Prf in self.votePrf:
            self.votePrf[Prf] = self.votePrf[Prf] + 1
        else:
            self.votePrf[Prf] = 1

    def reSetCount(self):  # Reset Count of all Preference
        for key in self.votePrf:
            self.votePrf[key] = 0
        # not in use


class voters:  # Votets Object
    def __init__(self, candi_name):
        self.candi_name = candi_name


class votes:  # Object for votes Votername, candidatname, given preference
    def __init__(self, VotersName, CandidateName, Preference):
        self.VotersName = VotersName
        self.CandidateName = CandidateName
        self.Preference = Preference


class winnerPin:  # Object to keep position and winner candidate name and its score
    def __init__(self, PinName, WinnerCandidateName, voteReceived):
        self.PinName = PinName
        self.WinnerCandidateName = WinnerCandidateName
        self.voteReceived = voteReceived


# Done by Yulin and Mohammed This class is for UI / window
class VotingGUI:
    def __init__(self, master):  # constructor
        # master is variable for window that is created in starting of program
        self.master = master  # matster is storing window object in this class
        master.title("University of Greenwich Voting System")
        master.geometry('800x600')  # dimension
        # Start :  Menu related Configuration
        self.menubar = Menu(master)  # menu
        master.config(menu=self.menubar, bg='white', borderwidth=1)
        master.configure(background='white')
        # --menu created --
        self.menubar.add_command(label="Login with UID and password", command=self.UserLoginForm)  # A1 & A2
        self.menubar.add_command(label="Cast votes", command=self.CastVotes)
        self.menubar.add_command(label="Results", command=self.Results)
        self.menubar.add_command(label="Logout", command=self.Logout)
        # End :  Menu related Configuration
        self.Authe = 'false'  # if user is authenticated then its value would be TRUE
        self.WelcomeLabel = None
        self.UIDLabel = None
        self.PWDLabel = None
        self.UIDInput = None
        self.PWDInput = None
        self.Login = None  # UserName
        self.LoginFormDisplayed = 'false'  # if it is true then Login form is displayed on UI
        self.candidateList = []  # python list All candidates
        self.VotingPins = {}  # dict of all Positions and number of candidates
        self.CandidatePinDict = {}  # CandidatePositionDict stores Poistion and List Of employee contesting for that position
        self.LoadCandidates()  # A3 : Load candidate from text file
        self.voterList = []  # List of Voters
        self.listofLabels_Prf = {}  # List of candidate and given preference by voter
        self.voteObjectList = []  # list of vote Class Object
        self.WinnerCandidate = None
        self.winnerPinList = []
        self.DisplayedItem = []
        self.VoteDoneList = []

    def Display(self):  # Done by Shahzeb and Tejal A6
        self.removeVoteCastUI()  # Clean UI before adding element on Window
        xx = 20
        yy = 40
        hh = 20
        cc = 0
        aa = 0

        for key in self.winnerPinList:
            if key in self.DisplayedItem:
                continue
            else:
                self.DisplayedItem.append(key)
                totalVote = 0
                label = Label(self.master,
                              text="************************************************************************",
                              bg='white')
                label.place(x=xx + 40, y=yy, width=230, height=hh)
                self.listofLabels_Prf[label] = ""
                yy = yy + hh
                label = Label(self.master, text="Position : " + key.PinName, bg='white')
                self.listofLabels_Prf[label] = ""
                label.place(x=xx + 40, y=yy, width=130, height=hh)
                yy = yy + hh
                label = Label(self.master,
                              text="************************************************************************",
                              bg='white')
                self.listofLabels_Prf[label] = ""
                label.place(x=xx + 40, y=yy, width=230, height=hh)
                yy = yy + hh
                label = Label(self.master, text="Candidate ", bg='white')
                self.listofLabels_Prf[label] = ""
                label.place(x=xx + 40, y=yy, width=130, height=hh)
                cc = yy
                yy = yy + hh
                aa = xx
                for x in range(self.VotingPins[key.PinName]):
                    xx = xx + 130
                    label = Label(self.master, text="Preference " + str(x + 1), bg='white')
                    self.listofLabels_Prf[label] = ""
                    label.place(x=xx + 40, y=cc, width=130, height=hh)
                for c in self.candidateList:
                    if c.Pin == key.PinName:
                        xx = aa + 40
                        cc = cc + hh
                        label = Label(self.master, text=c.candi_name, bg='white')
                        self.listofLabels_Prf[label] = ""
                        label.place(x=xx, y=cc, width=130, height=hh)
                        for x in range(self.VotingPins[key.PinName]):
                            xx = xx + 130
                            print(c.votePrf)
                            if str(x + 1) in c.votePrf:
                                votecount = c.votePrf[str(x + 1)]
                                totalVote = totalVote + votecount
                            else:
                                votecount = 0
                            label = Label(self.master, text=votecount, bg='white')
                            self.listofLabels_Prf[label] = ""
                            label.place(x=xx + 40, y=cc, width=130, height=hh)

                label = Label(self.master,
                              text="**********************************************************************", bg='white')
                self.listofLabels_Prf[label] = ""
                cc = cc + hh
                label.place(x=60, y=cc, width=230, height=hh)
                label = Label(self.master, text="Winner :" + key.WinnerCandidateName, bg='white')
                self.listofLabels_Prf[label] = ""
                cc = cc + hh
                label.place(x=60, y=cc, width=130, height=hh)
                label = Label(self.master, text="Vote Received :" + str(key.voteReceived), bg='white')
                self.listofLabels_Prf[label] = ""
                cc = cc + hh
                label.place(x=60, y=cc, width=130, height=hh)
                label = Label(self.master, text="Total Vote cast :" + str(len(self.voterList)), bg='white')
                self.listofLabels_Prf[label] = ""
                cc = cc + hh
                label.place(x=60, y=cc, width=130, height=hh)
                self.validate = Button(self.master, text="Next", command=self.Display, bg='green', fg='white')
                self.validate.place(x=80, y=cc + 20, width=100, height=25)
                break

    def Results(self):
        self.clearWindow()  # clear window
        self.CountVotes()  # A5 count vote and do manipulation
        self.Display()  # A6

    def Logout(self):
        self.removeVoteCastUI()
        self.CandidatePinDict.clear()
        self.listofLabels_Prf.clear()
        self.clearWindow()
        self.Authe = 'false'
        self.Login = None
        self.LoginFormDisplayed = 'false'
        print(self.voterList)

    # Done by Mohammed A3 -Load All candidates from GSUCandidates.txt
    def LoadCandidates(self):  # A3 -Load All candidates from GSUCandidates.txt
        self.clearWindow()
        self.msg = Label(self.master, text="Welcome to UoG Voting System", font=('courier', 20, 'bold'), bg='white')
        self.msg.place(x=25, y=40, width=800, height=50)
        StudentVoters = open('GSUCandidates.txt', 'r')
        Lines = StudentVoters.readlines()
        for line in Lines:
            candi_name = " ".join(line.strip().split(" ")[1:])
            postn = line.strip().split(" ")[0].strip()
            recordfound = 'false'
            if len(self.candidateList) > 0:
                for c in self.candidateList:  # validate One candidate for one position
                    if c.candi_name == candi_name:
                        recordfound = 'true'
                if recordfound != 'true':
                    self.candidateList.append(candidates(candi_name, postn))
                else:
                    recordfound = 'false'

            else:
                self.candidateList.append(candidates(candi_name, postn))
                pass
            pass

        # returns candidate position and takes input as candidate name

    def findPinofCandidate(self, candi_name):
        for key in self.CandidatePinDict:
            if candi_name in self.CandidatePinDict[key]:
                return key

    # Done by Yulin, Tejal, Shahzeb and Mohammed A4 Cast votes
    def CastVotes(self):  # A.4
        if self.Authe != 'false':
            self.removeVoteCastUI()  # Clean UI before adding element on Window
            self.CandidatePinDict.clear()  # clean before initi
            self.clearWindow()  # Clear Window
            # CandidatePositionDict stores position and List Of employee contesting for that position
            for c in self.candidateList:
                if c.Pin in self.CandidatePinDict:
                    self.CandidatePinDict[c.Pin].append(c.candi_name)
                    pass
                else:
                    l = []
                    l.append(c.candi_name)
                    self.CandidatePinDict[c.Pin] = l

                    # Display list of candidate
            xx = 20
            yy = 40
            hh = 20
            byy = 0
            counter = 0
            for key in self.CandidatePinDict:
                label = Label(self.master, text="For " + key, bg="sea green", fg='white', font=('courier', 10, 'bold'))
                label.place(x=xx, y=yy, width=170, height=hh)
                yy = yy + hh
                self.listofLabels_Prf[label] = ""
                for c in self.CandidatePinDict[key]:
                    label = Label(self.master, text=c, bg="pale green")
                    label.place(x=xx, y=yy, width=120, height=hh)
                    Input = Entry(self.master, validate="key")
                    Input['validatecommand'] = (Input.register(self.testVal), '%P', '%d')
                    Input.place(x=xx + 121, y=yy, width=50, height=hh)
                    self.listofLabels_Prf[label] = Input
                    yy = yy + hh
                    counter = counter + 1
                self.VotingPins[key] = counter
                counter = 0
                xx = xx + 180
                if byy < yy:
                    byy = yy
                yy = 40
            self.validate = Button(self.master, text="Validate & Submit", command=self.ValidateVote, bg="green",
                                   fg='white')
            self.validate.place(x=xx, y=byy + 20, width=120, height=25)

        else:
            messagebox.showinfo("Error", "Please first Login with UID and password.")
            self.removeVoteCastUI()  # Clean UI before adding element on Window
            self.UserLoginForm()

        pass

    # Done by Shahzeb, Tejal, Yulin and Mohammed: part of A4 - After voter user click Validate & Submit
    # Done by Shahzeb, Tejal, Yulin and Mohammed: part of A4 - It will validate preferences and validate duplicate, uniquness and other criteria
    # Done by Shahzeb, Tejal, Yulin and Mohammed: part of A4 - after validation it will store vote in votes.txt
    def ValidateVote(self):
        l = []
        for key in self.listofLabels_Prf:
            if not isinstance(self.listofLabels_Prf[key], str):
                maxCount = self.VotingPins[self.findPinofCandidate(key.cget("text"))]
                if self.listofLabels_Prf[key].get() == "":
                    messagebox.showinfo("Error", key.cget("text") + " No preference?")
                    return ""
                if int(self.listofLabels_Prf[key].get()) > maxCount:
                    messagebox.showinfo("Error", key.cget(
                        "text") + " Preference is not correct. it should be less then or equal to  " + str(maxCount))
                    return ""
                if self.listofLabels_Prf[key].get() in l:
                    messagebox.showinfo("Error", key.cget("text") + " duplicate Preference issue.")
                    return ""
                else:
                    l.append(self.listofLabels_Prf[key].get())
            else:
                l = []
        self.CreateVotes()
        self.removeVoteCastUI()
        self.Logout()

    # Done by Tejal and Shahzeb A 5 : Function to count votes as per logic
    def CountVotes(self):  # A.5
        for candidate in self.candidateList:
            candidate.reSetCount()  # Reset Before doing reCount
        for votes in self.voteObjectList:
            for candidate in self.candidateList:
                if candidate.candi_name == votes.CandidateName:
                    candidate.updateVoteForCandidate(
                        votes.Preference)  # Update Preference and Count in each Candidate Object
                    print(candidate.votePrf)
        self.Winner()  # A.6

    # function to get candidate name based on position and preference
    def getCandidatename(self, winnerScore, Prf, post):
        for cand in self.candidateList:
            if str(Prf) in cand.votePrf:
                if cand.votePrf[str(Prf)] == winnerScore and cand.Pin == post:
                    return cand.candi_name
                # Done by Shahzeb and Tejal: part of A 5 : Calculate winner for each position

    def Winner(self):
        winnerCandidateScoreList = []
        self.winnerPinList.clear()
        winnerScore = 0
        preference = 0
        for post in self.VotingPins:  # All position and count of candidates on position
            print("Preference for post-", post, " is ", self.VotingPins[post])
            winnerCandidateScoreList.clear()
            for Prf in range(self.VotingPins[post]):  # loop through number of preference
                for cand in self.candidateList:
                    if cand.Pin == post:
                        if str(Prf + 1) in cand.votePrf:
                            winnerCandidateScoreList.append(cand.votePrf[str(Prf + 1)])
                winnerCandidateScoreList.sort(reverse=True)  # Sort List in Descending Order
                print("winnerCandidateScoreList :", winnerCandidateScoreList, Prf + 1)
                if len(winnerCandidateScoreList) > 1:
                    a, b, *_ = winnerCandidateScoreList
                    if a > b and a != b:
                        winnerScore = a
                        preference = Prf + 1
                        break
                else:
                    winnerScore, *_ = winnerCandidateScoreList
                    preference = Prf + 1
                    break

            self.winnerPinList.append(
                winnerPin(post, self.getCandidatename(winnerScore, preference, post), winnerScore))

    # Done by Shahzeb, Tejal, Yulin and Mohammed: part of A4 : Create vote object for after submit button

    def CreateVotes(self):
        for key in self.listofLabels_Prf:
            if not isinstance(self.listofLabels_Prf[key], str):
                self.voteObjectList.append(votes(self.Login, key.cget("text"), self.listofLabels_Prf[key].get()))
        self.writeVotetofile()  # store in file
        messagebox.showinfo("Done", "Your vote has been written in file " + os.getcwd() + "\Votes.txt")

        pass

    # Done by Yulin: part of A2 : method to show welcome message
    def welcomeUser(self, u):  # Invoked to show  welcome Caption after login
        self.clearWindow()  # UI is clean
        # now it is adding New labals
        self.WelcomeLabel = Label(self.master, text=u + "! You are Welcome.", font=('courier', 15, 'bold'), bg='white')
        self.WelcomeLabel.place(x=30, y=40, width=920, height=25)
        pass

    # Done by Yulin: part of A2 : method  to remove UI component
    def removeVoteCastUI(self):
        if len(self.listofLabels_Prf) > 0:
            self.validate.destroy()
        for key in self.listofLabels_Prf:
            if key:
                key.destroy()
                if not isinstance(self.listofLabels_Prf[key], str):
                    self.listofLabels_Prf[key].destroy()

    # Done by Yulin: part of A2 : remove Login/password/login button from UI and show welcome message
    def clearWindow(self):
        print("clearWindow")
        if self.UIDLabel:
            self.UIDLabel.destroy()
        if self.PWDLabel:
            self.PWDLabel.destroy()
        if self.UIDInput:
            self.UIDInput.destroy()
        if self.PWDInput:
            self.PWDInput.destroy()
        if self.Login:
            self.Login.destroy()
        if self.WelcomeLabel:
            self.WelcomeLabel.destroy()

    # Done by Shahzeb, Tejal, Yulin and Mohammed: part of A4 - Write vote in votes.txt. It stores votes.txt in directory
    def writeVotetofile(self):
        f = open('Votes.txt', 'w')

        for v in self.voteObjectList:
            s = self.findPinofCandidate(v.CandidateName) + " " + v.CandidateName + " " + v.Preference
            f.write(s + '\n')
        f.close()

    # part of A2 this ValidateUser method will internally call from UserLoginForm method to validate if user is valid for voting
    # part of A2 - Validates Login user after click login button and it will be invoked from UserLoginForm method
    # part of A2 it will cross check login user/ password from 'StudentVoters.txt' file
    # part of A2 - if user login / password is correct then it will show welcome message by calling welcomeUser method
    def ValidateUser(self):
        if self.UIDInput.get() not in self.VoteDoneList:
            self.VoteDoneList.append(self.UIDInput.get())
            if self.UIDInput.get() != "" and self.PWDInput.get() != "":
                # Read StudentVoters.txt readlines()
                StudentVoters = open('StudentVoters.txt', 'r')
                Lines = StudentVoters.readlines()
                for line in Lines:
                    u = line.strip().split(" ")[0].strip()
                    p = line.strip().split(" ")[1].strip()
                    if u == self.UIDInput.get():
                        if p == self.PWDInput.get():
                            self.Authe = 'true'
                            break
                if self.Authe == 'false':
                    messagebox.showinfo("Error", "Person is not eligible for vote.")
                else:
                    self.welcomeUser(u)  # A2 method to show welcome message for logged in user
                    self.voterList.append(voters(u))

            else:
                messagebox.showinfo("Error", "Please Enter UID / Password")
        else:
            messagebox.showinfo("Error", "You have already voted.")
            self.LoginFormDisplayed = 'false'
            self.clearWindow()  # Clears UI element of user Id/Password/Login button

    # this testVal method is to validate if user has input preference of candidate  must be digit
    def testVal(self, inStr, acttyp):
        if acttyp == '1':  # insert
            if not inStr.isdigit():
                return False

        return True

    # Done by Shahzeb, Tejal, Yulin and Mohammed: this is first method to show login password and part of A1 & A2
    # It will be invoked when user will click Login/Password menu
    # this method will internally call Function ValidateUser to validate if user is valid for voting
    def UserLoginForm(self):  # A1  & A2
        if self.LoginFormDisplayed == 'false':
            self.LoginFormDisplayed = 'true'
            if self.Authe == 'false':
                self.msg.destroy()
                self.UIDLabel = Label(self.master, text="UID :")
                self.UIDLabel.place(x=20, y=40, width=120, height=25)
                self.UIDInput = Entry(self.master)
                self.UIDInput.place(x=141, y=40, width=120, height=25)
                self.PWDLabel = Label(self.master, text="Password :")
                self.PWDLabel.place(x=20, y=67, width=120, height=25)
                self.PWDInput = Entry(self.master)
                self.PWDInput.place(x=141, y=67, width=120, height=25)
                self.Login = Button(self.master, text="Login", command=self.ValidateUser, bg="green",
                                    fg='white')  # Login Button click will call ValidateUser user method
                self.Login.place(x=200, y=100, width=60, height=25)
            else:
                messagebox.showinfo("Warning", "You are already authenticated.")
            value = 'default text'


# program will start from here.
root = Tk()  # this will create a window root
my_gui = VotingGUI(root)  # this class is taking input of window root
root.mainloop()
