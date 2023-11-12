import sys
import os
from InstallWindow import InstallWindow  # Import the InstallWindow class
from LoginWindow import LoginScreen  # Import the LoginScreen class
from PyQt5.QtWidgets import QApplication, QSplashScreen, QLabel  # Import necessary PyQt5 widgets
from PyQt5.QtGui import QPixmap  # Import the QPixmap class from PyQt5
from PyQt5.QtCore import Qt, QTimer  # Import necessary modules


class MainScreen():
    def showSplashScreen(self):
        # Load the image for the splash screen
        self.pix = QPixmap("splash_img.png")
        self.splash = QSplashScreen(self.pix, Qt.WindowStaysOnTopHint)  # Create a QSplashScreen object     
        self.splash.show()  # Display the splash screen


def showSetupWindow():
    # Close the splash screen and display the installation window
    mainScreen.splash.close()
    installWindow.show()


def showLoginWindow():
    # Close the splash screen and display the login window
    mainScreen.splash.close()
    login.showLoginScreen()


app = QApplication(sys.argv)  # Create a PyQt application
login = LoginScreen()  # Instantiate the LoginScreen
mainScreen = MainScreen()  # Instantiate the MainScreen
mainScreen.showSplashScreen()  # Show the splash screen
installWindow = InstallWindow()  # Instantiate the InstallWindow

# Check if a configuration file exists, and then decide which window to show after a delay
if os.path.exists("./config.json"):
    QTimer.singleShot(3000, showLoginWindow)  # If config file exists, show login window after 3 seconds
else:
    QTimer.singleShot(3000, showSetupWindow)  # If config file doesn't exist, show setup window after 3 seconds

sys.exit(app.exec_())  # Execute the application


app=QApplication(sys.argv)
login=LoginScreen()
mainScreen=MainScreen()
mainScreen.showSplashScreen()
installWindow=InstallWindow()

if os.path.exists("./config.json"):
    QTimer.singleShot(3000,showLoginWindow)
else:
    QTimer.singleShot(3000,showSetupWindow)


sys.exit(app.exec_())