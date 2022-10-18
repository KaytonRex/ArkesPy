import os
import datetime

def LoggingFile(LogType, LogMessage):

    # Creates the logging file structure
    ArkesFolder = os.getcwd()
    LoggingFolder = os.path.join(ArkesFolder, "Logging")
    CurrentDateTime = datetime.datetime.now()
    LoggingFile = os.path.join(LoggingFolder, f"{CurrentDateTime.year}-{CurrentDateTime.month}-{CurrentDateTime.day}.txt")

    # Check if the folder and file exists, if fails, exit app
    LoggingFolderExists = os.path.exists(LoggingFolder)
    if not LoggingFolderExists:
        try:
            os.mkdir(LoggingFolder)
        except FileExistsError:
            LoggingFolderExists = True
        except (IOError, ValueError, EOFError) as e:
            print(f"{datetime.datetime.now()} \t Type: Error \t Process: Creating Log Folder ({str(LoggingFolder)}). Please fix this and try again! \n {e}")
            exit()

    LoggingFileExists = os.path.exists(LoggingFile)
    if not LoggingFileExists:
        try:
            f = open(LoggingFile,"w+")
            f.write(f"{datetime.datetime.now()} \t Type: Startup \t Process: Created Logging File {LoggingFile}")
            f.close()
        except (IOError, ValueError, EOFError) as e:
            print(f"{datetime.datetime.now()} \t Type: Error \t Process: Creating Log File {LoggingFile}. Please fix this and try again! \n {e}")


def FolderChecker(action, folderpath):
    if action == "CREATE":
        print("Create")
    elif action == "CHECK":
        print("Check")
    else:
        print("")

LoggingFile("Test", "Test")